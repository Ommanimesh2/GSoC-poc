import argparse
from demoapi.api import DemoAPi

parser = argparse.ArgumentParser(description="CLI tool to interact with DummyAPI")

parser.add_argument("command", type=str, choices=["get", "post"], help="Command to execute")
parser.add_argument("--id", type=int, help="ID of product to fetch/update")
parser.add_argument("--data", type=str, help="Data to send in POST request")

args = parser.parse_args()

if args.command == "get":
    if args.id is None:
        # Get all products from /products/1
        api = DemoAPi("https://dummyjson.com")
        result = api.get_all_products()
        print(result)
    else:
        # Get product by ID from /products/:id
        api = DemoAPi("https://dummyjson.com")
        result = api.get_product(args.id)
        print(result)
elif args.command == "post":
    if args.id is None:
        print("Error: --id argument is required for POST command")
    elif args.data is None:
        print("Error: --data argument is required for POST command")
    else:
        # Update product by ID with data from POST request to /products/:id
        api = DemoAPi("https://dummyjson.com")
        result = api.post(f"products/{args.id}", data=args.data)
        print(result)
