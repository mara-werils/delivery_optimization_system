from .co2_calculator import calculate_co2_emission

def optimize_route(possible_routes, vehicle_type="truck"):
    """
    Выбирает оптимальный маршрут на основе минимального времени доставки и выбросов CO2.
    
    :param possible_routes: Список маршрутов с их параметрами
    :param vehicle_type: Тип транспортного средства ("truck" или "airplane")
    :return: Лучший маршрут с учётом времени и выбросов CO2
    """
    best_route = None
    min_time = float('inf')
    min_co2 = float('inf')

    for route in possible_routes:
        route_time = route['estimated_time']
        route_distance = route['distance']  # Добавляем расстояние для расчёта CO2
        co2_emission = calculate_co2_emission(route_distance, vehicle_type)

        if route_time < min_time and co2_emission < min_co2:
            min_time = route_time
            min_co2 = co2_emission
            best_route = route
            best_route['co2_emission'] = co2_emission  # Добавляем выбросы в данные маршрута

    return best_route

routes = [
    {"route_id": "A", "estimated_time": 30, "distance": 100},
    {"route_id": "B", "estimated_time": 45, "distance": 200},
    {"route_id": "C", "estimated_time": 25, "distance": 150}
]
best_route = optimize_route(routes, vehicle_type="truck")
print(f"Best Route: {best_route['route_id']} with CO2 Emissions: {best_route['co2_emission']} kg")