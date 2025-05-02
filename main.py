from datetime import datetime
from warehouse.product import Product
from warehouse.supplier import Supplier
from warehouse.warehouse import Warehouse
from warehouse.transaction import Transaction

def main():
    warehouse = Warehouse()
    transactions = []

    while True:
        print("\n--- СКЛАДСЬКИЙ ОБЛІК ---")
        print("1. Додати постачальника")
        print("2. Додати товар")
        print("3. Переглянути список товарів")
        print("4. Переглянути постачальників")
        print("5. Видалити товар")
        print("6. Оновити інформацію про товар")
        print("7. Переглянути товари постачальника")
        print("8. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            supplier_id = input("ID постачальника: ")
            name = input("Назва компанії: ")
            contact = input("Контакт (email або телефон): ")
            try:
                supplier = Supplier(supplier_id, name, contact)
                warehouse.add_supplier(supplier)
                print("✅ Постачальника додано.")
            except Exception as e:
                print(f"❌ Помилка: {e}")

        elif choice == "2":
            name = input("Назва товару: ")
            quantity = int(input("Кількість: "))
            price = float(input("Ціна: "))
            arrival_date = datetime.strptime(input("Дата надходження (YYYY-MM-DD): "), "%Y-%m-%d").date()
            supplier_id = input("ID постачальника: ")
            try:
                product = Product(name, quantity, price, arrival_date, supplier_id, warehouse)
                warehouse.add_product(product)
                transactions.append(Transaction("надходження", name, quantity, supplier_id, "склад"))
                print("✅ Товар додано.")
            except Exception as e:
                print(f"❌ Помилка: {e}")

        elif choice == "3":
            sort_key = input("Сортувати за (name/quantity/price або Enter): ")
            products = warehouse.list_products(sort_by=sort_key if sort_key else None)
            if not products:
                print("📦 Немає товарів.")
            else:
                for p in products:
                    print(f"{p.name} | Кількість: {p.quantity} | Ціна: {p.price} | Дата: {p.arrival_date} | Постачальник: {p.supplier_id}")

        elif choice == "4":
            suppliers = warehouse.list_suppliers()
            if not suppliers:
                print("🙅‍ Немає постачальників.")
            else:
                for s in suppliers:
                    print(f"{s.supplier_id} | {s.name} | {s.contact}")

        elif choice == "5":
            name = input("Назва товару для видалення: ")
            warehouse.remove_product(name)
            print("🗑️ Товар видалено.")

        elif choice == "6":
            name = input("Назва товару для оновлення: ")
            new_price = float(input("Нова ціна (або Enter для пропуску): ") or 0)
            new_quantity = input("Нова кількість (або Enter для пропуску): ")
            try:
                updates = {}
                if new_price > 0:
                    updates["price"] = new_price
                if new_quantity.isdigit():
                    updates["quantity"] = int(new_quantity)
                warehouse.update_product(name, **updates)
                print("✅ Товар оновлено.")
            except Exception as e:
                print(f"❌ Помилка: {e}")

        elif choice == "7":
            supplier_id = input("ID постачальника: ")
            items = warehouse.get_supplier_products(supplier_id)
            if not items:
                print("📭 У постачальника немає товарів.")
            else:
                for p in items:
                    print(f"{p.name} | Кількість: {p.quantity} | Ціна: {p.price}")

        elif choice == "8":
            print("👋 Завершення роботи.")
            break

        else:
            print("❗ Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
