from api_integration.sap_api import SAPAPI
from api_integration.oracle_api import OracleAPI

class APISync:
    def __init__(self, sap_api, oracle_api):
        self.sap_api = sap_api
        self.oracle_api = oracle_api

    def sync_order_status(self, order_id):
        sap_status = self.sap_api.get_order_status(order_id)
        if sap_status:
            print(f"SAP статус для заказа {order_id}: {sap_status}")
            self.oracle_api.update_order_status(order_id, sap_status['status'])

    def sync_routes(self, route_id):
        route_info = self.oracle_api.get_route_info(route_id)
        if route_info:
            print(f"Информация о маршруте из Oracle для маршрута {route_id}: {route_info}")

# Пример использования
if __name__ == "__main__":
    sap_api = SAPAPI(base_url="https://api.sap.com", api_key="your_sap_api_key")
    oracle_api = OracleAPI(base_url="https://api.oracle.com", api_key="your_oracle_api_key")
    api_sync = APISync(sap_api, oracle_api)

    # Синхронизация статуса заказа
    api_sync.sync_order_status(order_id="123")

    # Синхронизация информации о маршруте
    api_sync.sync_routes(route_id="A1")
