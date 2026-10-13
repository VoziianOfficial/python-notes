from product import Product

from product import Product

product = Product("Laptop", 1000)

print("Start price:", product.price)


product.price = 1200

print("New price:", product.price)

product.price = -500

print("Price after invalid change:", product.price)
