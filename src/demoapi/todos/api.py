import sys
 

sys.path.append("..")
from core.api import ApiBase

class Todo(ApiBase):
    def __init__(self,base_url):
        self.base_url=base_url
        
    def get(self,id=None):
        endpoint = id
        return ApiBase.get(self,endpoint)
   
    def all (self):
        endpoint=""
        return ApiBase.get(self,endpoint)

 
        