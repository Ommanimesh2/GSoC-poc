import sys
sys.path.append("..")

from demoapi.api import DemoAPi

client = DemoAPi(base_url='https://dummyjson.com')
Alltodos = client.todo.get()
SpecificTodo = client.todo.get(2)
AllProducts = client.todo.get()
SpecificProduct = client.todo.get(4)

print(Alltodos,SpecificTodo,AllProducts,SpecificProduct)