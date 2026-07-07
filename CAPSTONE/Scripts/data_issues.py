import random
from pathlib import Path

import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw_sales.csv"

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(RAW_DATA)

print(f"Loaded {len(df)} rows.")

# --------------------------------------------------
# 1. Duplicate 20 random rows
# --------------------------------------------------

duplicates = df.sample(20, random_state=42)

df = pd.concat([df, duplicates], ignore_index=True)

print("Added duplicate rows.")

# --------------------------------------------------
# 2. Missing Payment Method
# --------------------------------------------------

payment_index = df.sample(30, random_state=1).index

df.loc[payment_index, "PaymentMethod"] = None

print("Added missing PaymentMethod values.")

# --------------------------------------------------
# 3. Missing Customer Type
# --------------------------------------------------

customer_index = df.sample(25, random_state=2).index

df.loc[customer_index, "CustomerType"] = None

print("Added missing CustomerType values.")

# --------------------------------------------------
# 4. Missing Store Location
# --------------------------------------------------

store_index = df.sample(15, random_state=3).index

df.loc[store_index, "StoreLocation"] = None

print("Added missing StoreLocation values.")

# --------------------------------------------------
# 5. Extra Spaces
# --------------------------------------------------

space_index = df.sample(40, random_state=4).index

df.loc[space_index, "ProductName"] = (
    " " + df.loc[space_index, "ProductName"] + " "
)

print("Added extra spaces.")

# --------------------------------------------------
# 6. Mixed Capitalization
# --------------------------------------------------

caps_index = df.sample(40, random_state=5).index

df.loc[caps_index, "ProductName"] = (
    df.loc[caps_index, "ProductName"].str.lower()
)

print("Added inconsistent capitalization.")

# --------------------------------------------------
# Save Updated Dataset
# --------------------------------------------------

df.to_csv(RAW_DATA, index=False)

print("\nData quality issues introduced successfully.")
print(df.head())