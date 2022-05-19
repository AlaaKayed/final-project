import requests

class BookStoreConsistancyManager:
        
    def __init__(self, servers):
        self.servers = servers
        self.acks = []
         

    def update_replicas_decrement(self,book_id):
        for server in self.servers:
            response = requests.put(f'http://{server}/catalog/update/{book_id}')
    #         self.acks.append(response.status_code)

    #     if self.check_write_completed():
    #         return True
    #     return False

    # def check_write_completed(self):
    #     result = all((element == 201 or element==200) for element in self.acks)
    #     return result    