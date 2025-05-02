import re


class Supplier:
    """
    Клас постачальника.
    Атрибути:
        supplier_id (str): унікальний ідентифікатор
        name (str): назва компанії
        contact (str): контактна інформація (email або телефон)
    """

    def __init__(self, supplier_id: str, name: str, contact: str):
        if not isinstance(supplier_id, str) or not supplier_id.strip():
            raise ValueError("Supplier ID must be a non-empty string")
        if not isinstance(name, str) or not (1 <= len(name) <= 100):
            raise ValueError("Supplier name must be between 1 and 100 characters")
        if not self._is_valid_contact(contact):
            raise ValueError(f"Invalid contact information: {contact}")

        self.supplier_id = supplier_id
        self.name = name
        self.contact = contact

    def _is_valid_contact(self, contact: str) -> bool:
        """
        Перевіряє, чи контакт є дійсним email або українським номером телефону.
        """
        email_pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w{2,4}$'
        phone_pattern = r'^\\+?\\d{10,13}$'
        return re.match(email_pattern, contact) or re.match(phone_pattern, contact)
