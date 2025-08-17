import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("worldpopulationdata_50.csv")

# --- Distribution by Continent (Categorical Variable) ---
plt.figure(figsize=(8,6))
sns.countplot(x="Continent", data=df, palette="Set2")
plt.title("Distribution of Countries by Continent")
plt.xlabel("Continent")
plt.ylabel("Number of Countries")
plt.show()

# --- Distribution of 2022 Population (Continuous Variable) ---
plt.figure(figsize=(10,6))
plt.hist(df["2022 Population"], bins=10, edgecolor="black")
plt.title("Distribution of Population in 2022")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.show()

# Take the 2022 population for analysis
df["2022 Population"] = df["2022 Population"].astype(int)

# --- Simulate Gender Distribution ---
male_percentage = 0.51
female_percentage = 0.49

df["Male Population"] = (df["2022 Population"] * male_percentage).astype(int)
df["Female Population"] = (df["2022 Population"] * female_percentage).astype(int)

# --- Simulate Age Distribution (approx split by UN data) ---
age_bins = {
    "0-14": 0.25,   # 25%
    "15-24": 0.16,  # 16%
    "25-54": 0.40,  # 40%
    "55-64": 0.10,  # 10%
    "65+": 0.09     # 9%
}

for group, perc in age_bins.items():
    df[group] = (df["2022 Population"] * perc).astype(int)

# --- Visualization: Gender Distribution ---
plt.figure(figsize=(6,6))
gender_totals = [df["Male Population"].sum(), df["Female Population"].sum()]
plt.bar(["Male", "Female"], gender_totals, color=["blue","pink"])
plt.title("World Gender Distribution (Simulated)")
plt.ylabel("Population (Billions)")
plt.show()

# --- Visualization: Age Group Distribution ---
plt.figure(figsize=(8,6))
age_totals = [df[age].sum() for age in age_bins.keys()]
plt.bar(age_bins.keys(), age_totals, color="green")
plt.title("World Age Group Distribution (Simulated)")
plt.xlabel("Age Group")
plt.ylabel("Population (Billions)")
plt.show()