import unittest
from warehouse.warehouse import Warehouse
from warehouse.supplier import Supplier
from warehouse.product import Product

class TestWarehouse(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()
        self.supplier = Supplier("sup1", "Postach Ltd", "test@example.com")
        self.warehouse.add_supplier(self.supplier)

    def test_add_supplier(self):
        self.assertEqual(len(self.warehouse.suppliers), 1)
        self.assertEqual(self.warehouse.suppliers[0].name, "Postach Ltd")

    def test_add_product(self):
        product = Product("Кава", 10, 99.99, "2025-01-01", "sup1", self.warehouse)
        self.warehouse.add_product(product)
        self.assertEqual(len(self.warehouse.products), 1)
        self.assertEqual(self.warehouse.products[0].name, "Кава")

    def test_remove_product(self):
        product = Product("Чай", 5, 20.0, "2025-01-01", "sup1", self.warehouse)
        self.warehouse.add_product(product)
        self.warehouse.remove_product("Чай")
        self.assertEqual(len(self.warehouse.products), 0)

    def test_sort_products_by_name(self):
        product1 = Product("Кава", 10, 99.99, "2025-01-01", "sup1", self.warehouse)
        product2 = Product("Чай", 15, 35.0, "2025-01-01", "sup1", self.warehouse)
        self.warehouse.add_product(product1)
        self.warehouse.add_product(product2)
        sorted_products = self.warehouse.sort_products("name")
        self.assertEqual(sorted_products[0].name, "Чай")
        self.assertEqual(sorted_products[1].name, "Кава")

if __name__ == '__main__':
    unittest.main()
