import uuid

def create_order(customer_id, details):
    order_id = str(uuid.uuid4())
    order_data = {
        "order_id": order_id,
        "customer_id": customer_id,
        "details": details,
        "status": "Created"
    }
    print(f"Создан заказ: {order_data}")
    return order_data
