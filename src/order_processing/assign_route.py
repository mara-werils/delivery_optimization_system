def assign_route(order_data):
    routes = ["Route A", "Route B", "Route C"]
    order_data["route"] = routes[hash(order_data["order_id"]) % len(routes)]
    print(f"Назначен маршрут: {order_data['route']} для заказа {order_data['order_id']}")
    return order_data
