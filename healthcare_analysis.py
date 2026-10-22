
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "1776250375-P2-Healthcare Analytics for Doctor Visits (1).csv"
)

# Set graph style
sns.set_theme(style="whitegrid")

# Count records for each number of visits
visit_counts = df["visits"].value_counts().sort_index()

# Create the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(
    x=visit_counts.index,
    y=visit_counts.values,
    color="steelblue"
)

plt.title("Distribution of Doctor Visits", fontsize=16)
plt.xlabel("Number of Doctor Visits", fontsize=12)
plt.ylabel("Number of Records", fontsize=12)

plt.tight_layout()
plt.savefig("doctor_visits_distribution.png", dpi=300)
plt.show()

print("Graph created and saved successfully!")
print("\nRecords for each visit count:")
print(visit_counts.sort_index())
