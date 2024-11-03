import time
import random

def simulate_delay():
    delay_chance = random.uniform(0, 1)
    if delay_chance < 0.2:
        delay_time = random.uniform(2, 5)
        print(f"Задержка на этапе: ожидание {delay_time:.2f} секунд.")
        time.sleep(delay_time)

def track_delivery(order_data):
    stages = ["Подготовка к отправке", "Отправлено", "На складе транзита", "В пути", "На конечном складе", "Доставлено"]
    for stage in stages:
        simulate_delay()
        order_data["status"] = stage
        print(f"Заказ {order_data['order_id']} - текущий статус: {stage}")
        time.sleep(random.uniform(1, 3))

    order_data["status"] = "Завершено"
    print(f"Заказ {order_data['order_id']} успешно доставлен.")
    return order_data
