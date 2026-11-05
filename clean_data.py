import pandas as pd

# 1. Read the raw dataset
df = pd.read_csv("raw_customer_dataset.csv")

print("Original Dataset:")
print(df.head())

# 2. Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Remove extra spaces from text columns
text_columns = [
    "customer_name",
    "gender",
    "country",
    "city",
    "customer_segment"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

# 5. Standardize Gender
df["gender"] = (
    df["gender"]
    .str.lower()
    .replace({
        "m": "male",
        "f": "female"
    })
    .str.title()
)

# 6. Standardize Country
df["country"] = (
    df["country"]
    .str.lower()
    .replace({
        "india": "India",
        "usa": "United States",
        "u.s.a.": "United States",
        "united states": "United States",
        "uk": "United Kingdom",
        "united kingdom": "United Kingdom",
        "canada": "Canada"
    })
    .str.title()
)

# 7. Standardize City
df["city"] = (
    df["city"]
    .str.lower()
    .replace({
        "bangalore": "Bengaluru",
        "mysore": "Mysuru"
    })
    .str.title()
)

# 8. Convert numeric columns
numeric_columns = [
    "age",
    "annual_income",
    "purchase_amount"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 9. Convert purchase date
df["purchase_date"] = pd.to_datetime(
    df["purchase_date"],
    errors="coerce",
    dayfirst=True
)

# 10. Fill missing numeric values with median
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# 11. Fill missing categorical values with mode
categorical_columns = [
    "gender",
    "country",
    "city",
    "customer_segment"
]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# 12. Format date consistently
df["purchase_date"] = df["purchase_date"].dt.strftime("%d-%m-%Y")

# 13. Save cleaned dataset
df.to_csv("cleaned_customer_dataset.csv", index=False)

print("\nCleaning completed successfully!")
print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nCleaned Dataset:")
print(df.head())