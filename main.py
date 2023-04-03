from demoapi.api import DemoAPi
client = DemoAPi(base_url='https://dummyjson.com')
response = client.get_product(3)

print(response)