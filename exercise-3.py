# =====================================================
# Exercise 3: Product Inventory Analyzer
# =====================================================

products = [
    ("Laptop", 15, 70000),
    ("Mouse", 50, 1200),
    ("Keyboard", 30, 2500),
    ("Monitor", 10, 15000),
    ("USB", 100, 500)
]


def total_inventory_value(product_list):
    """
    Calculate total inventory value.
    quantity * price
    """
    return sum(quantity * price for _, quantity, price in product_list)
print(total_inventory_value(products))
pass


def most_expensive_product(product_list):
    """
    Return most expensive product.
    """
    return max(product_list, key=lambda x: x[2])
print(most_expensive_product(products))
pass


def low_stock_products(product_list):
    """
    Return products with quantity < 20.
    """
    return list(filter(lambda x: x[1] < 20, product_list))
print(low_stock_products(products))
pass


def increase_prices(product_list):
    """
    Increase prices by 15% using map().
    """
    return list(map(lambda x: (x[0], x[2] * 1.15), product_list))
print(increase_prices(products))
pass


def sort_products_by_quantity(product_list):
    """
    Sort products by quantity.
    """
    return sorted(product_list, key=lambda x: x[1])
print(sort_products_by_quantity(products))
pass


def process_quantities(product_list):
    """
    Square even quantities.
    Cube odd quantities.
    """
    return [(product[0], product[1] ** 2) if product[1] % 2 == 0 else (product[0], product[1] ** 3) for product in product_list]
print(process_quantities(products)) 
pass


def expensive_products(product_list):
    """
    Use filter() to get products costing above 5000.
    """
    return list(filter(lambda x: x[2] > 5000, product_list))
print(expensive_products(products))
pass



import numpy as np
print("NumPy imported successfully!")

arr = np.array([1, 2, 3, 4])
print(arr * 2)
