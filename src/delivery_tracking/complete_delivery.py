def complete_delivery(order_data):
    order_data["status"] = "Completed"
    print(f"Заказ {order_data['order_id']} завершен и помечен как 'Completed'.")
    return order_data
