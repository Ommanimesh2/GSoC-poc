from core import ApiBase

class OgcApi(ApiBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_collections(self):
        endpoint = "/collections"
        return self.get(endpoint)

    def get_collection(self, collection_id):
        endpoint = f"/collections/{collection_id}"
        return self.get(endpoint)

    def post_collection(self, collection_data):
        endpoint = "/collections"
        return self.post(endpoint, collection_data)

    def get_features(self, collection_id, params=None):
        endpoint = f"/collections/{collection_id}/features"
        return self.get(endpoint, params=params)

    def post_features(self, collection_id, feature_data):
        endpoint = f"/collections/{collection_id}/features"
        return self.post(endpoint, feature_data)
