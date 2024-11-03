import hashlib
import time

def generate_order_id(order_data):
    unique_string = f"{order_data['customer_name']}{order_data['email']}{time.time()}"
    order_id = hashlib.sha256(unique_string.encode()).hexdigest()[:10]  # Берем только первые 10 символов хэша
    return order_id

order_data = {
    "customer_name": "John Doe",
    "email": "john@example.com"
}
order_id = generate_order_id(order_data)
print(f"Order ID: {order_id}")
