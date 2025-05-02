import unittest
from datetime import date
from warehouse.transaction import Transaction
from warehouse.product import Product
from warehouse.supplier import Supplier
from warehouse.warehouse import Warehouse

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()
        self.supplier = Supplier("sup1", "Postach Ltd", "test@example.com")
        self.warehouse.add_supplier(self.supplier)
        self.product = Product("Кава", 10, 99.99, date.today(), "sup1", self.warehouse)

    def test_create_transaction(self):
        transaction = Transaction("надходження", "Кава", 5, "sup1", "склад")
        self.assertEqual(transaction.product_name, "Кава")
        self.assertEqual(transaction.quantity, 5)
        self.assertEqual(transaction.transaction_type, "надходження")
        self.assertEqual(transaction.date, date.today())

    def test_invalid_transaction_type(self):
        with self.assertRaises(ValueError):
            Transaction("невірний тип", "Кава", 5, "sup1", "склад")

    def test_transaction_with_invalid_product(self):
        with self.assertRaises(ValueError):
            Transaction("надходження", "Неіснуючий товар", 5, "sup1", "склад")

if __name__ == '__main__':
    unittest.main()
