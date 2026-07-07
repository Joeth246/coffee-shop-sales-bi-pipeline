from pathlib import Path

import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw_sales.csv"

CLEAN_DATA = PROJECT_ROOT / "data" / "cleaned_sales.csv"

# --------------------------------------------------
# Load
# --------------------------------------------------

df = pd.read_csv(RAW_DATA)

print("Dataset Loaded\n")

print(df.info())

print("\nMissing Values\n")

print(df.isnull().sum())

print("\nDuplicate Rows:")

print(df.duplicated().sum())


# Remove Duplicates

df.drop_duplicates(inplace=True)

# Fill Missing Values

df["PaymentMethod"] = df["PaymentMethod"].fillna("Unknown")

df["CustomerType"] = df["CustomerType"].fillna("Guest")

df["StoreLocation"] = df["StoreLocation"].fillna("Unknown")

# Clean Text Columns

text_columns = [
    "StoreLocation",
    "ProductCategory",
    "ProductName",
    "PaymentMethod",
    "CustomerType"
]

for column in text_columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
        .str.title()
    )

# Verify

print("\nAfter Cleaning\n")

print(df.isnull().sum())

print("\nDuplicates Remaining:")

print(df.duplicated().sum())

# Save

df.to_csv(CLEAN_DATA, index=False)

print("\nClean dataset saved successfully!")

print(df.head())
print(df)