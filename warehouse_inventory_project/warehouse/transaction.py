from datetime import datetime

class Transaction:
    """
    Клас для представлення операцій зі складом.
    Атрибути:
        date (datetime): дата й час операції
        transaction_type (str): тип операції ('надходження', 'відвантаження', 'переміщення')
        product_name (str): назва товару
        quantity (int): кількість товару
        source (str): джерело (наприклад, постачальник або склад)
        destination (str): місце призначення (наприклад, інший склад або клієнт)
    """
    def __init__(self, transaction_type: str, product_name: str, quantity: int, source: str = "", destination: str = ""):
        valid_types = {'надходження', 'відвантаження', 'переміщення'}
        if transaction_type not in valid_types:
            raise ValueError(f"Invalid transaction type '{transaction_type}'. Must be one of {valid_types}")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if not isinstance(product_name, str) or not product_name.strip():
            raise ValueError("Product name must be a non-empty string")

        self.date = datetime.now()
        self.transaction_type = transaction_type
        self.product_name = product_name
        self.quantity = quantity
        self.source = source
        self.destination = destination
