import pandas as pd

# 1. Charger les données
df = pd.read_csv("data.csv")

# 2. Aperçu des données
print("Aperçu des données :")
print(df)

# 3. Calcul du chiffre d'affaires
df["revenue"] = df["quantity"] * df["price"]

# 4. Chiffre d'affaires total
total_revenue = df["revenue"].sum()
print("\nChiffre d'affaires total :", total_revenue)

# 5. Chiffre d'affaires par produit
revenue_by_product = df.groupby("product")["revenue"].sum()
print("\nChiffre d'affaires par produit :")
print(revenue_by_product)
