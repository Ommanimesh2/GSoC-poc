import sys
 

sys.path.append("..")
from core.api import ApiBase

class Todo(ApiBase):
    def __init__(self,base_url):
        self.base_url=base_url
        
    def get(self,todo_id=None):
        if todo_id is None:
            endpoint = ""
            return ApiBase.get(self,endpoint)
        else:
            endpoint = todo_id
            return ApiBase.get(self,endpoint)
        

 
        