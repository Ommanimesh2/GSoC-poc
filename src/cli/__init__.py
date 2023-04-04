import argparse
import sys
 

sys.path.append("..")
 
# import method from sibling
# module
from demoapi.api import DemoAPi

parser = argparse.ArgumentParser(description="CLI tool to interact with DummyAPI")

parser.add_argument("command", type=str, choices=["get", "post"], help="Command to execute")
parser.add_argument("--id", type=int, help="ID of product to fetch/update")
parser.add_argument("--data", type=str, help="Data to send in POST request")
parser.add_argument("--type", type=str, help="Type of product to fetch/update")

args = parser.parse_args()

if args.command == "get":
    if args.id is None and args.type is not None:

        if(args.type=="todo"):
            api = DemoAPi("https://dummyjson.com")
            result = api.todo.get()
            print(result)

        elif(args.type=="product"):
            api = DemoAPi("https://dummyjson.com")
            result = api.product.get()
            print(result)

    elif args.id is not None and args.type is not None:
        if(args.type=="todo"):
            api = DemoAPi("https://dummyjson.com")
            result = api.todo.get(args.id)
            print(result)
        if(args.type=="product"):
            api = DemoAPi("https://dummyjson.com")
            result = api.product.get(args.id)
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
