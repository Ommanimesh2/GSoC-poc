import sys
 

sys.path.append("..")
from core.api import ApiBase
from demoapi.todos.api import Todo
from demoapi.products.api import Product

class DemoAPi(ApiBase):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.todo = Todo(f"{base_url}/todos")
        self.product=Product(f"{base_url}/products")

   

