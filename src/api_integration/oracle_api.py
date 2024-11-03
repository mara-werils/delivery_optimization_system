import requests

class OracleAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_route_info(self, route_id):
        url = f"{self.base_url}/routes/{route_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else None

    def create_delivery_order(self, order_data):
        url = f"{self.base_url}/orders"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(url, json=order_data, headers=headers)
        return response.json() if response.status_code == 201 else None
