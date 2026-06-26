import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Roberton Dataset.xlsx")

# Summary statistics
print(df.describe())
print(df.info())

# Age distribution
df['Age'].hist(bins=15, color="skyblue")
plt.title("Age Distribution")
plt.show()

# Reaction time distribution
df['Reac. Time'].hist(bins=15, color="orange")
plt.title("Reaction Time Distribution")
plt.show()

# Group comparisons
print("Quick vs Slow:", df.groupby("Reaction time (quick/slow)")["Reac. Time"].mean())
print("Gender differences:", df.groupby("Gender")["Reac. Time"].mean())
print("Handedness differences:", df.groupby("Handedness")["Reac. Time"].mean())

# Relationships
sns.scatterplot(x="Phys. Act.", y="Reac. Time", hue="Reaction time (quick/slow)", data=df)
plt.title("Physical Activity vs Reaction Time")
plt.show()

sns.scatterplot(x="Age", y="Reac. Time", hue="Reaction time (quick/slow)", data=df)
plt.title("Age vs Reaction Time")
plt.show()

print("Correlation matrix:\n", df[["Age","Phys. Act.","Reac. Time"]].corr())
