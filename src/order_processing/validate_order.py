def validate_order(order_data):
    if not order_data.get("customer_id") or not order_data.get("details"):
        raise ValueError("Ошибка валидации: отсутствует ID клиента или детали заказа.")
    print("Валидация заказа успешна.")
    return True
