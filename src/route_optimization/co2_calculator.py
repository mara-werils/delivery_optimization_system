def calculate_co2_emission(distance_km, vehicle_type="truck"):
    """
    Рассчитывает выбросы CO2 на основе расстояния и типа транспортного средства.
    
    :param distance_km: Расстояние маршрута в километрах
    :param vehicle_type: Тип транспортного средства ("truck" или "airplane")
    :return: Оценка выбросов CO2 в килограммах
    """
    # Коэффициенты выбросов для разных типов транспорта
    emission_factors = {
        "truck": 0.27,       # кг CO2 за км для грузовика
        "airplane": 1.15     # кг CO2 за км для самолёта
    }
    
    emission_factor = emission_factors.get(vehicle_type, 0.27)  # По умолчанию грузовик
    co2_emission = distance_km * emission_factor
    return co2_emission

distance = 500  # Пример расстояния в км
vehicle_type = "airplane"
co2_emission = calculate_co2_emission(distance, vehicle_type)
print(f"Estimated CO2 Emissions for {distance} km by {vehicle_type}: {co2_emission} kg")
