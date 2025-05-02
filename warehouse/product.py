from datetime import date
from .validators import validate_price, validate_name, validate_supplier_exists

class Product:
    """
    Клас товару на складі.
    Атрибути:
        name (str): найменування товару
        quantity (int): кількість на складі
        price (float): ціна за одиницю
        arrival_date (date): дата надходження
        supplier_id (str): ідентифікатор постачальника
    """
    def __init__(self, name: str, quantity: int, price: float, arrival_date: date, supplier_id: str, warehouse):
        # Валідація вхідних даних
        validate_name(name)
        validate_price(price)
        validate_supplier_exists(supplier_id, warehouse)
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError(f"Quantity must be non-negative integer, got {quantity}")
        if not isinstance(arrival_date, date):
            raise TypeError("arrival_date must be a datetime.date object")
        # Ініціалізація атрибутів
        self.name = name
        self.quantity = quantity
        self.price = price
        self.arrival_date = arrival_date
        self.supplier_id = supplier_id