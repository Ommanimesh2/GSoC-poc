import sys
sys.path.append("..")
from core.api import ApiBase

class Product(ApiBase):
    def __init__(self,base_url):
        self.base_url=base_url
        
    def get(self,product_id=None):
        if product_id is None:
            endpoint = ""
            return ApiBase.get(self,endpoint)
        else:
            endpoint = product_id
            return ApiBase.get(self,endpoint)
    

 
        