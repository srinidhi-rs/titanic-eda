import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("titanic.csv")

# Drop missing Embarked values
data.dropna(subset=["Embarked"], inplace=True)

# Fill missing Cabin values with "Unknown"
data["Cabin"].fillna("Unknown", inplace=True)

# Fill missing Age values with the mean age
data["Age"].fillna(data["Age"].mean(), inplace=True)

# Check for and drop duplicates if needed (though none exist here)
print("Number of duplicate rows:", data.duplicated().sum())

# Plot: Age distribution
plt.figure(figsize=(6, 3))
sns.histplot(data["Age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Plot: Survival by Gender
plt.figure(figsize=(6, 3))
sns.countplot(data=data, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", loc="upper right")
plt.tight_layout()
plt.show()

# Plot: Scatter of Age vs Fare colored by Survival
plt.figure(figsize=(6, 3))
sns.scatterplot(data=data, x="Age", y="Fare", hue="Survived")
plt.title("Scatter Plot of Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend(title="Survived")
plt.tight_layout()
plt.show()
