from .product import Product
from .supplier import Supplier

class Warehouse:
    """
    Клас складу, що зберігає товари та постачальників.
    """
    def __init__(self):
        self.products = []  # список обʼєктів Product
        self.suppliers = {}  # словник постачальників: supplier_id -> Supplier

    def add_supplier(self, supplier: Supplier):
        """
        Додає постачальника до складу.
        """
        if supplier.supplier_id in self.suppliers:
            raise ValueError(f"Supplier with ID {supplier.supplier_id} already exists")
        self.suppliers[supplier.supplier_id] = supplier

    def add_product(self, product: Product):
        """
        Додає товар до складу.
        """
        self.products.append(product)

    def remove_product(self, name: str):
        """
        Видаляє товар за назвою.
        """
        self.products = [p for p in self.products if p.name != name]

    def update_product(self, name: str, **kwargs):
        """
        Оновлює атрибути товару: ціна, кількість тощо.
        """
        for product in self.products:
            if product.name == name:
                for key, value in kwargs.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                return
        raise ValueError(f"No product found with name '{name}'")

    def list_products(self, sort_by=None):
        """
        Повертає список товарів, відсортований за вказаним критерієм.
        """
        if sort_by and hasattr(Product, sort_by):
            return sorted(self.products, key=lambda p: getattr(p, sort_by))
        return self.products

    def list_suppliers(self):
        """
        Повертає список постачальників.
        """
        return list(self.suppliers.values())

    def get_supplier_products(self, supplier_id: str):
        """
        Повертає товари від конкретного постачальника.
        """
        return [p for p in self.products if p.supplier_id == supplier_id]
