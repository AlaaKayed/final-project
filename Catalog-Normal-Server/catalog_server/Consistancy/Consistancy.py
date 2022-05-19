import requests

class BookStoreConsistancyManager:
        
    def __init__(self, primary_server):
        self.primary_server = primary_server

    def forward_decrement_request(self,book_id):
        response = requests.put(f'http://{self.primary_server}/catalog/update/{book_id}')