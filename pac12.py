
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create customer dataset
np.random.seed(42)
n = 200

df = pd.DataFrame({
    "CustomerID": range(1, n + 1),
    "Age": np.random.randint(18, 70, n),
    "Tenure": np.random.randint(1, 72, n),
    "MonthlyCharges": np.random.uniform(20, 120, n).round(2),
    "TotalCharges": np.random.uniform(100, 8000, n).round(2),
    "Contract": np.random.choice(
        ["Month-to-month", "One year", "Two year"], n),
    "InternetService": np.random.choice(
        ["DSL", "Fiber optic", "No"], n),
    "Churn": np.random.choice(["Yes", "No"], n, p=[0.3, 0.7])
})

# Add missing values
df.loc[[5, 15, 25, 35], "Age"] = np.nan
df.loc[[10, 20, 30], "MonthlyCharges"] = np.nan
df.loc[[12, 22], "Contract"] = np.nan

print("Original Dataset:")
print(df.head())

# 2. Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns.tolist())

# 3. Remove duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Value Percentage:")
print((df.isnull().mean() * 100).round(2))

# 5. Handle missing values
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include="object").columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 6. Summary statistics
print("\nNumerical Summary:")
print(df.describe().round(2))

print("\nCategorical Summary:")
print(df.describe(include="object"))

# 7. Overall churn rate
churn_rate = (df["Churn"] == "Yes").mean() * 100
print("\nOverall Churn Rate:")
print(round(churn_rate, 2), "%")

# 8. Churn by contract
print("\nChurn by Contract:")
print(pd.crosstab(
    df["Contract"], df["Churn"],
    normalize="index"
) * 100)

# 9. Churn by internet service
print("\nChurn by Internet Service:")
print(pd.crosstab(
    df["InternetService"], df["Churn"],
    normalize="index"
) * 100)

# 10. Average customer details
print("\nAverage Customer Details:")
print(df.groupby("Churn")[
    ["Age", "Tenure", "MonthlyCharges", "TotalCharges"]
].mean().round(2))

# 11. Churn distribution
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# 12. Churn by contract
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Customer Churn by Contract")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=15)
plt.show()

# 13. Tenure and churn
sns.boxplot(data=df, x="Churn", y="Tenure")
plt.title("Tenure Distribution by Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure")
plt.show()

# 14. Monthly charges and churn
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.show()

# 15. Correlation heatmap
corr = df[
    ["Age", "Tenure", "MonthlyCharges", "TotalCharges"]
].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 16. Pattern analysis
df["ChurnFlag"] = (df["Churn"] == "Yes")

print("\nChurn Rate by Contract:")
print(df.groupby("Contract")["ChurnFlag"].mean() * 100)

print("\nAverage Tenure by Churn:")
print(df.groupby("Churn")["Tenure"].mean())

print("\nAverage Monthly Charges by Churn:")
print(df.groupby("Churn")["MonthlyCharges"].mean())

# 17. Save cleaned dataset
df.drop(columns=["ChurnFlag"]).to_csv(
    "cleaned_customer_churn.csv", index=False
)

print("\nCleaned Dataset Saved Successfully!")
