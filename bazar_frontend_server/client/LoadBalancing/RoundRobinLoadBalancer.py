from . import LoadBalancer

class RoundRobinLoadBalancer:

    def __init__(self, servers):
        self.server_index = 0
        self.servers = servers

    def get_server(self):
        server = self.servers[self.server_index]
        self.server_index = (self.server_index+1) % len(self.servers)
        return server
  
