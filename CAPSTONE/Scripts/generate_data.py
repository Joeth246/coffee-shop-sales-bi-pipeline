
# Bean & Brew Coffee Co. (This Parent company operates a couple of stores and these stores have different locations as shown through the code)
# Q1 2026 Sales Data Generator
# Creator - Joeth246

# Purpose - Generate realistic synthetic coffee shop sales data for analytics using Python, SQLite, SQL and Power BI.

import pandas as pd
import random
from datetime import datetime, timedelta

# Data structure -


NUMBER_OF_TRANSACTIONS = 7500
START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 3, 31)

# Stores operated and their location

STORES = [
    {"StoreID": 101, "StoreLocation": "Downtown Toronto"},
    {"StoreID": 102, "StoreLocation": "North York"},
    {"StoreID": 103, "StoreLocation": "Mississauga"},
    {"StoreID": 104, "StoreLocation": "Vaughan"},
    {"StoreID": 105, "StoreLocation": "Hamilton"},
    {"StoreID": 106, "StoreLocation": "Ottawa"}
]

# Products sold by these stores 

PRODUCTS = [

    # Coffee
    {"Category": "Coffee", "Product": "Espresso", "Price": 3.25},
    {"Category": "Coffee", "Product": "Americano", "Price": 3.75},
    {"Category": "Coffee", "Product": "Latte", "Price": 5.50},
    {"Category": "Coffee", "Product": "Cappuccino", "Price": 5.25},
    {"Category": "Coffee", "Product": "Flat White", "Price": 5.75},
    {"Category": "Coffee", "Product": "Mocha", "Price": 5.95},

    # Tea
    {"Category": "Tea", "Product": "Green Tea", "Price": 3.50},
    {"Category": "Tea", "Product": "Earl Grey", "Price": 3.50},
    {"Category": "Tea", "Product": "Chai Latte", "Price": 5.50},
    {"Category": "Tea", "Product": "Matcha Latte", "Price": 5.95},

    # Cold Drinks
    {"Category": "Cold Drinks", "Product": "Cold Brew", "Price": 4.95},
    {"Category": "Cold Drinks", "Product": "Iced Coffee", "Price": 4.75},
    {"Category": "Cold Drinks", "Product": "Iced Latte", "Price": 5.75},
    {"Category": "Cold Drinks", "Product": "Lemonade", "Price": 4.25},
    {"Category": "Cold Drinks", "Product": "Strawberry Refresher", "Price": 5.25},

    # Bakery
    {"Category": "Bakery", "Product": "Croissant", "Price": 3.95},
    {"Category": "Bakery", "Product": "Blueberry Muffin", "Price": 3.75},
    {"Category": "Bakery", "Product": "Chocolate Muffin", "Price": 3.75},
    {"Category": "Bakery", "Product": "Bagel", "Price": 3.50},
    {"Category": "Bakery", "Product": "Cookie", "Price": 2.75},
    {"Category": "Bakery", "Product": "Brownie", "Price": 3.50},

    # Breakfast
    {"Category": "Breakfast", "Product": "Breakfast Sandwich", "Price": 6.95},
    {"Category": "Breakfast", "Product": "Oatmeal", "Price": 4.95},
    {"Category": "Breakfast", "Product": "Yogurt Parfait", "Price": 5.25}

]


# Generating time customers come in for their orders
def generate_random_time():
    time_blocks = [
        (7, 10),   # Morning rush
        (11, 14),  # Lunch peak
        (14, 17),  # Afternoon
        (17, 21)   # Evening
    ]

    weights = [0.35, 0.30, 0.20, 0.15]

    chosen_block = random.choices(time_blocks, weights=weights, k=1)[0]

    hour = random.randint(chosen_block[0], chosen_block[1] - 1)
    minute = random.randint(0, 59)

    return f"{hour:02d}:{minute:02d}:00"

# Select a random store

def get_random_store():
    return random.choice(STORES)

def get_discount():
    return random.choices(
        population=[0, 5, 10, 15, 20],
        weights=[0.80, 0.10, 0.05, 0.03, 0.02],
        k=1
    )[0]


# Select a random product
def get_random_product():
    return random.choice(PRODUCTS)

data = []

def get_product_details():
    return random.choice(PRODUCTS)

# Quantity function.
def get_quantity():
    return random.choices(
        population=[1, 2, 3, 4, 5],
        weights=[0.55, 0.25, 0.10, 0.06, 0.04],
        k=1
    )[0]

# customer payments
def get_payment_method():
    return random.choices(
        population=["Card", "Mobile", "Cash"],
        weights=[0.50, 0.35, 0.15],
        k=1
    )[0]

# customer_types
def get_customer_type():
    return random.choices(
        ["Member", "Guest"],
        weights=[0.60, 0.40],
        k=1
    )[0]

# Generate random date in Q1
def generate_random_date():
    start_date = datetime(2026, 1, 1)
    end_date = datetime(2026, 3, 31)

    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    return start_date + timedelta(days=random_days)

# CSV Generation Loop

for i in range(NUMBER_OF_TRANSACTIONS):

    transaction_id = f"BB{100000 + i}"

    store = random.choice(STORES)
    product = get_product_details()

    quantity = get_quantity()
    discount = get_discount()

    unit_price = product["Price"]

    subtotal = unit_price * quantity
    final_price = subtotal * (1 - discount / 100)

    transaction_date = generate_random_date()
    transaction_time = generate_random_time()

    record = {
        "TransactionID": transaction_id,
        "TransactionDate": transaction_date.date(),
        "TransactionTime": transaction_time,
        "StoreID": store["StoreID"],
        "StoreLocation": store["StoreLocation"],
        "ProductCategory": product["Category"],
        "ProductName": product["Product"],
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "DiscountPercent": discount,
        "SalesAmount": round(final_price, 2),
        "PaymentMethod": get_payment_method(),
        "CustomerType": get_customer_type(),
        "Month": transaction_date.month,
        "Weekday": transaction_date.strftime("%A"),
        "Hour": int(transaction_time.split(":")[0])
    }

    data.append(record)

# Export to CSV

df = pd.DataFrame(data)

df.to_csv("raw_sales.csv", index=False)

print("Dataset generated successfully!")
print(df.head())