from order_processing.create_order import create_order
from order_processing.validate_order import validate_order
from order_processing.assign_route import assign_route
from delivery_tracking.track_delivery import track_delivery
from delivery_tracking.complete_delivery import complete_delivery
from blockchain.blockchain_log import BlockchainLog
from route_optimization.route_optimization import optimize_route
from route_optimization.co2_calculator import calculate_co2_emission


def main():
    customer_id = input("Введите ID клиента: ")
    details = {"product": "Aviation Part", "quantity": 5}
    order = create_order(customer_id, details)

    validate_order(order)

    possible_routes = [
        {"route_id": "A", "estimated_time": 30, "distance": 100},
        {"route_id": "B", "estimated_time": 45, "distance": 200},
        {"route_id": "C", "estimated_time": 25, "distance": 150},
    ]
    best_route = optimize_route(possible_routes, vehicle_type="truck")
    print(
        f"Best Route: {best_route['route_id']} with CO2 Emissions: {best_route['co2_emission']} kg"
    )

    order["assigned_route"] = best_route

    track_delivery(order)

    complete_delivery(order)

    blockchain = BlockchainLog()
    blockchain.add_record(order)
    blockchain.display_chain()


if __name__ == "__main__":
    main()
