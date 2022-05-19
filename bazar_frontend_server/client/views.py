from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .LoadBalancing.RoundRobinLoadBalancer import RoundRobinLoadBalancer
import requests
from pymemcache.client import base
import json

catalog_servers = ['catalog-instance1:9000', 'catalog-instance2:9000']
order_servers = ['order-instance1:9002', 'order-instance2:9002']


catalog_load_balancer = RoundRobinLoadBalancer(catalog_servers)
order_load_balancer = RoundRobinLoadBalancer(order_servers)


client = base.Client(('my-memcache', 11211))


def is_cached_value(cache_result):
    
    if cache_result is not None:
        return True
    return False


   

@api_view(['GET'])
def search(request, topic):
    cache_result = client.get(str(topic).replace(' ', ''))
    if is_cached_value(cache_result):
        print(f'topic cache result for {topic}: {cache_result}')
        my_json_result = bytes(cache_result).decode('utf8').replace("'", '"')
        return Response(json.loads(my_json_result))

    else:
        search_response = requests.get(
            f'http://{catalog_load_balancer.get_server()}/catalog/search/{topic}'
        )

        client.set(str(topic).replace(' ', ''), search_response.json())
        return Response(search_response.json())


@api_view(['GET'])
def info(request, pk):

    cache_result = client.get(str(pk))
    if is_cached_value(cache_result):
        print('From Cache')
        my_json_result = bytes(cache_result).decode('utf8').replace("'", '"')
        return Response(json.loads(my_json_result))

    else:

        info_response = requests.get(
            f'http://{catalog_load_balancer.get_server()}/catalog/info/{pk}'
        )
        client.set(str(pk),info_response.json())
        return Response(info_response.json())


@api_view(['POST'])
def purchase(request, pk):
    purcha_response = requests.post(
        f'http://{order_load_balancer.get_server()}/order-server/purchase/{pk}'
    )
    if is_cached_value(client.get(str(pk))):
        client.delete(str(pk))
        topic = dict(purcha_response.json()).get('book').get('topic')
        topic = str(topic).replace(' ', '')
        cache_result = client.get(str(topic))
        if is_cached_value(cache_result):
            client.delete(str(topic))

    return Response(purcha_response.json())
