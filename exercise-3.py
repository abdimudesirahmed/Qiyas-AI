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
    pass


def increase_prices(product_list):
    """
    Increase prices by 15% using map().
    """
    pass


def sort_products_by_quantity(product_list):
    """
    Sort products by quantity.
    """
    pass


def process_quantities(product_list):
    """
    Square even quantities.
    Cube odd quantities.
    """
    pass


def expensive_products(product_list):
    """
    Use filter() to get products costing above 5000.
    """
    pass