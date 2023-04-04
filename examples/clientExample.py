import sys
sys.path.append("..")

from src.demoapi.api import DemoAPi

client = DemoAPi(base_url='https://dummyjson.com')
Alltodos = client.todo.all()
SpecificTodo = client.todo.get(id=2)
AllProducts = client.todo.all()
SpecificProduct = client.todo.get(id=4)

print(Alltodos,SpecificProduct,SpecificTodo,AllProducts)