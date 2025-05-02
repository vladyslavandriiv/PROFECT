import unittest
from warehouse.supplier import Supplier

class TestSupplier(unittest.TestCase):

    def test_create_valid_supplier(self):
        supplier = Supplier("sup1", "Postach Ltd", "contact@postach.com")
        self.assertEqual(supplier.supplier_id, "sup1")
        self.assertEqual(supplier.name, "Postach Ltd")
        self.assertEqual(supplier.contact, "contact@postach.com")

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError):
            Supplier("sup2", "Vendor Co", "invalid-email")

    def test_invalid_phone_format(self):
        with self.assertRaises(ValueError):
            Supplier("sup3", "Vendor Corp", "12345")

if __name__ == '__main__':
    unittest.main()
