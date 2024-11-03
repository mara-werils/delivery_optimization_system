# Blockchain Log Documentation

## Введение
Модуль блокчейн-логирования используется для записи данных о каждом этапе доставки. Это обеспечивает неизменяемость данных и возможность отслеживания на каждом этапе.

## Структура блока
Каждый блок включает следующие данные:
- **index**: Порядковый номер блока в цепочке.
- **timestamp**: Временная метка создания блока.
- **data**: Данные о заказе, включая идентификатор, текущий статус и маршрут.
- **previous_hash**: Хэш предыдущего блока для поддержания целостности цепочки.
- **hash**: Хэш текущего блока, вычисленный на основе данных и предыдущего хэша.

## Пример использования

```python
from blockchain.blockchain_log import BlockchainLog

blockchain = BlockchainLog()
order_data = {
    "order_id": "e3f8d6d9-abc2-4c28-914d-5b7c9e2e8923",
    "status": "Delivered",
    "route": "Route A"
}
blockchain.add_record(order_data)
blockchain.display_chain()
