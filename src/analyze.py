import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/raw/handm.csv")

# Create recycled-material indicator
df["has_recycled"] = df["materials"].str.contains(
    "Recycled", case=False, na=False
)

# Create output directory
import os
os.makedirs("outputs", exist_ok=True)

# 1. Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=30)
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.title("Distribution of H&M Product Prices")
plt.tight_layout()
plt.savefig("outputs/price_distribution.png")
plt.close()

# 2. Most common materials
df["composition"] = (
    df["materials"]
    .str.split("ADDITIONAL MATERIAL INFORMATION").str[0]
    .str.replace("\n", " ", regex=False)
    .str.replace("COMPOSITION", "", regex=False)
    .str.strip()
)

materials = df["composition"].fillna("").str.findall(
    r"([A-Za-z]+(?:\s+[A-Za-z]+)?)\s+\d+(?:\.\d+)?%"
)

material_counts = pd.Series(
    [material for row in materials for material in row]
).value_counts()

plt.figure(figsize=(10, 5))
material_counts.head(10).plot(kind="bar")
plt.xlabel("Material")
plt.ylabel("Number of Mentions")
plt.title("Most Common Materials in H&M Products")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("outputs/material_frequency.png")
plt.close()

# 3. Recycled material vs average price
price_comparison = df.groupby("has_recycled")["price"].mean()

plt.figure(figsize=(7, 5))
price_comparison.plot(kind="bar")
plt.xlabel("Contains Recycled Material")
plt.ylabel("Average Price")
plt.title("Average Price by Recycled-Material Mention")
plt.xticks([0, 1], ["No", "Yes"], rotation=0)
plt.tight_layout()
plt.savefig("outputs/recycled_price_comparison.png")
plt.close()

print("Analysis completed successfully.")
print(f"Total products analysed: {len(df)}")
print(f"Products with recycled-material mention: {df['has_recycled'].sum()}")