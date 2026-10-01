from order import Order
from utils import create_order_number, get_order_date
from product import Product
from customer import Customer

import reports

# ---------------------------------
# 1. СОЗДАЁМ ТОВАРЫ
# ---------------------------------

laptop = Product("Laptop", 800, 5)
mouse = Product("Mouse", 50, 20)
keyboard = Product("Keyboard", 100, 10)
headphones = Product("Headphones", 150, 8)

products = [laptop, mouse, keyboard, headphones]


# ---------------------------------
# 2. СОЗДАЁМ ПОКУПАТЕЛЯ
# ---------------------------------

customer = Customer("Yuliia", 3000)


# ---------------------------------
# 3. ПОКАЗЫВАЕМ СКЛАД
# ---------------------------------

print("\n--- INVENTORY ---")

reports.show_inventory(products)


# ---------------------------------
# 4. ИЩЕМ НУЖНЫЕ ТОВАРЫ
# ---------------------------------

selected_laptop = reports.find_product(products, "Laptop")
selected_mouse = reports.find_product(products, "Mouse")
selected_headphones = reports.find_product(products, "Headphones")


# ---------------------------------
# 5. СОЗДАЁМ ЗАКАЗ
# ---------------------------------

order = Order(customer, [], "new", create_order_number(), get_order_date())


# ---------------------------------
# 6. ДОБАВЛЯЕМ ТОВАРЫ
# ---------------------------------

if selected_laptop is not None:
    order.add_product(selected_laptop, 1)

if selected_mouse is not None:
    order.add_product(selected_mouse, 2)

if selected_headphones is not None:
    order.add_product(selected_headphones, 1)


# ---------------------------------
# 7. ПОКАЗЫВАЕМ КОРЗИНУ
# ---------------------------------

print("\n--- CART ---")

order.show_items()

total = order.calculate_total()

print("Order total:", total)


# ---------------------------------
# 8. СОХРАНЯЕМ ДАННЫЕ ДО ОПЛАТЫ
# ---------------------------------

balance_before = customer.balance

laptop_stock_before = laptop.stock
mouse_stock_before = mouse.stock
headphones_stock_before = headphones.stock


# ---------------------------------
# 9. CHECKOUT
# ---------------------------------

print("\n--- CHECKOUT ---")

if order.checkout():
    print("Order successful")
    print("Order number:", order.order_number)
    print("Order date:", order.order_date)
    print("Customer:", customer.name)

    print("\nProducts:")
    order.show_items()

    print("Total:", order.calculate_total())
    print("Status:", order.status)

    print("Balance before:", balance_before)
    print("Balance after:", customer.balance)

else:
    print("Order failed")


# ---------------------------------
# 10. ПРОВЕРЯЕМ ОСТАТКИ ПОСЛЕ ОПЛАТЫ
# ---------------------------------

print("\n--- STOCK CHANGES ---")

print("Laptop:", laptop_stock_before, "->", laptop.stock)
print("Mouse:", mouse_stock_before, "->", mouse.stock)
print("Headphones:", headphones_stock_before, "->", headphones.stock)


print("\n--- INVENTORY AFTER CHECKOUT ---")

reports.show_inventory(products)


# ---------------------------------
# 11. ОТМЕНЯЕМ ЗАКАЗ
# ---------------------------------

print("\n--- CANCEL ORDER ---")

if order.cancel():
    print("Order cancelled")
    print("Status:", order.status)
    print("Balance after refund:", customer.balance)

else:
    print("Order cannot be cancelled")


# ---------------------------------
# 12. ПРОВЕРЯЕМ СКЛАД ПОСЛЕ ОТМЕНЫ
# ---------------------------------

print("\n--- INVENTORY AFTER CANCELLATION ---")

reports.show_inventory(products)

print("Customer balance:", customer.balance)


# ---------------------------------
# 13. ПОВТОРНАЯ ОТМЕНА
# ---------------------------------

print("\n--- SECOND CANCELLATION TEST ---")

if order.cancel():
    print("Order cancelled again")

else:
    print("Order cannot be cancelled again")


# ---------------------------------
# 14. ТЕСТ: НЕДОСТАТОЧНО ТОВАРА
# ---------------------------------

print("\n--- NOT ENOUGH STOCK TEST ---")

stock_test_order = Order(customer, [], "new", create_order_number(), get_order_date())

selected_keyboard = reports.find_product(products, "Keyboard")

if selected_keyboard is not None:
    added = stock_test_order.add_product(selected_keyboard, 100)

    if added:
        print("Product added")
    else:
        print("Not enough stock")


print("Keyboard stock:", keyboard.stock)


# ---------------------------------
# 15. ТЕСТ: НЕДОСТАТОЧНО ДЕНЕГ
# ---------------------------------

print("\n--- NOT ENOUGH MONEY TEST ---")

poor_customer = Customer("Anna", 100)

poor_order = Order(poor_customer, [], "new", create_order_number(), get_order_date())

expensive_product = reports.find_product(products, "Laptop")

if expensive_product is not None:
    poor_order.add_product(expensive_product, 1)


poor_balance_before = poor_customer.balance
laptop_stock_before_test = laptop.stock


if poor_order.checkout():
    print("Payment successful")

else:
    print("Payment failed correctly")


print("Balance before:", poor_balance_before)
print("Balance after:", poor_customer.balance)

print("Laptop stock before:", laptop_stock_before_test)
print("Laptop stock after:", laptop.stock)


# ---------------------------------
# 16. ТЕСТ: ПУСТОЙ ЗАКАЗ
# ---------------------------------

print("\n--- EMPTY ORDER TEST ---")

empty_order = Order(customer, [], "new", create_order_number(), get_order_date())

if empty_order.checkout():
    print("Empty order paid")

else:
    print("Empty order rejected correctly")


# ---------------------------------
# 17. ПРОВЕРЯЕМ ОБЪЕКТ PRODUCT
# ---------------------------------

print("\n--- PRODUCT OBJECT ---")

print(type(laptop))
print(isinstance(laptop, Product))
print(vars(laptop))
print(hasattr(laptop, "price"))
print(getattr(laptop, "stock"))


# ---------------------------------
# 18. ПРОВЕРЯЕМ CUSTOMER
# ---------------------------------

print("\n--- CUSTOMER OBJECT ---")

print(type(customer))
print(isinstance(customer, Customer))
print(vars(customer))
print(hasattr(customer, "balance"))
print(getattr(customer, "name"))


# ---------------------------------
# 19. ПРОВЕРЯЕМ ORDER
# ---------------------------------

print("\n--- ORDER OBJECT ---")

print(type(order))
print(isinstance(order, Order))
print(vars(order))
print(hasattr(order, "status"))
print(getattr(order, "status"))


# ---------------------------------
# 20. DOCSTRING
# ---------------------------------

print("\n--- DOCUMENTATION ---")

print(Product.__doc__)
print(Customer.__doc__)
print(Order.__doc__)
