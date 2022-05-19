from abc import ABCMeta, abstractmethod

class LoadBalancer(metaclass=ABCMeta):
    
    @abstractmethod
    def get_server(self):
        pass