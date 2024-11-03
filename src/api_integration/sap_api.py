import requests

class SAPAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_order_status(self, order_id):
        url = f"{self.base_url}/orders/{order_id}/status"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else None

    def update_order_status(self, order_id, status):
        url = f"{self.base_url}/orders/{order_id}/status"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        data = {"status": status}
        response = requests.put(url, json=data, headers=headers)
        return response.json() if response.status_code == 200 else None
