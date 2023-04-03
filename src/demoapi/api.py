from core.api import ApiBase

class DemoAPi(ApiBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_product(self,product_id):
        endpoint = f"/products/{product_id}"
        return self.get(endpoint)

    def get_all_products(self):
        endpoint = "/products"
        return self.get(endpoint)

    def post_product(self, collection_data):
        endpoint = "/products/add"
        return self.post(endpoint, collection_data)

