import hashlib
import time

class BlockchainLog:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', data="Genesis Block")

    def create_block(self, data, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(data, previous_hash)
        }
        self.chain.append(block)
        return block

    def hash_block(self, data, previous_hash):
        block_string = f"{data}{previous_hash}{time.time()}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_record(self, order_data):
        previous_block = self.chain[-1]
        new_block = self.create_block(data=order_data, previous_hash=previous_block['hash'])
        print(f"Добавлено в блокчейн: {new_block}")
        return new_block

    def display_chain(self):
        for block in self.chain:
            print(block)

class SmartContract:
    def __init__(self):
        self.balances = {}

    def add_funds(self, client_id, amount):
        if client_id not in self.balances:
            self.balances[client_id] = 0
        self.balances[client_id] += amount
        print(f"Фонд клиента {client_id} пополнен на {amount}. Текущий баланс: {self.balances[client_id]}")

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

if __name__ == "__main__":
    blockchain = BlockchainLog()
    smart_contract = SmartContract()

    client_id = "client_123"
    smart_contract.add_funds(client_id, 300)

    order_data = {"order_id": "123", "status": "Отправлено"}
    blockchain.add_record(order_data)
    payment_status = smart_contract.execute_payment(client_id, order_data["status"])
    blockchain.add_record({"order_id": order_data["order_id"], "payment_status": payment_status})

    order_data["status"] = "Доставлено"
    blockchain.add_record(order_data)
    payment_status = smart_contract.execute_payment(client_id, order_data["status"])
    blockchain.add_record({"order_id": order_data["order_id"], "payment_status": payment_status})

    blockchain.display_chain()
