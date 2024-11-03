class SmartContract:
    def __init__(self):
        self.balances = {}

    def add_funds(self, client_id, amount):
        if client_id not in self.balances:
            self.balances[client_id] = 0
        self.balances[client_id] += amount
        print(f"Баланс клиента {client_id} пополнен на {amount}. Текущий баланс: {self.balances[client_id]}")

    def execute_payment(self, client_id, order_status):
        payment_required = 0
        if order_status == "Отправлено":
            payment_required = 100
        elif order_status == "Доставлено":
            payment_required = 200

        if payment_required > 0 and self.balances.get(client_id, 0) >= payment_required:
            self.balances[client_id] -= payment_required
            payment_status = f"Платеж {payment_required} выполнен для клиента {client_id} при статусе {order_status}."
            print(payment_status)
            return payment_status
        else:
            print("Недостаточно средств или неверный статус заказа.")
            return "Платеж не выполнен"

    def get_balance(self, client_id):
        balance = self.balances.get(client_id, 0)
        print(f"Текущий баланс клиента {client_id}: {balance}")
        return balance
