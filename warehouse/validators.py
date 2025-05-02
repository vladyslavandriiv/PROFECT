
import re
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .warehouse import Warehouse

def validate_name(name: str):
    """
    Перевіряє, що name — це непорожній рядок.
    """
    if not isinstance(name, str):
        raise TypeError(f"Name must be a string, got {type(name)}")
    if not name.strip():
        raise ValueError("Name cannot be empty or whitespace")

def validate_price(price: float):
    """
    Перевіряє, що price — невід’ємне число.
    """
    if not (isinstance(price, int) or isinstance(price, float)):
        raise TypeError(f"Price must be a number, got {type(price)}")
    if price < 0:
        raise ValueError(f"Price must be non-negative, got {price}")

def validate_supplier_exists(supplier_id: str, warehouse: "Warehouse"):
    """
    Перевіряє, що supplier_id — рядок і існує в warehouse.suppliers.
    Імпорт Warehouse виконується всередині, щоб уникнути циклічної залежності.
    """
    # імпортуємо тут, щоб не створювати коло імпортів на рівні модуля
    from .warehouse import Warehouse

    if not isinstance(supplier_id, str):
        raise TypeError(f"Supplier ID must be a string, got {type(supplier_id)}")
    if not isinstance(warehouse, Warehouse):
        raise TypeError("Second argument must be a Warehouse instance")
    if supplier_id not in warehouse.suppliers:
        raise ValueError(f"Supplier with ID '{supplier_id}' does not exist in warehouse")
