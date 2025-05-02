import unittest
from datetime import date
from warehouse.product import Product
from warehouse.warehouse import Warehouse
from warehouse.supplier import Supplier

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()
        self.supplier = Supplier("sup1", "Postach Ltd", "test@example.com")
        self.warehouse.add_supplier(self.supplier)

    def test_create_valid_product(self):
        product = Product("Кава", 10, 99.99, date.today(), "sup1", self.warehouse)
        self.assertEqual(product.name, "Кава")
        self.assertEqual(product.quantity, 10)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Product("Чай", 5, -10.0, date.today(), "sup1", self.warehouse)

    def test_missing_supplier(self):
        with self.assertRaises(ValueError):
            Product("Сік", 3, 30.0, date.today(), "sup2", self.warehouse)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            Product("Молоко", -1, 10.0, date.today(), "sup1", self.warehouse)

    def test_invalid_date_type(self):
        with self.assertRaises(TypeError):
            Product("Хліб", 2, 15.0, "2024-01-01", "sup1", self.warehouse)

if __name__ == '__main__':
    unittest.main()
