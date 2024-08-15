from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as ss
import numpy as np
import statsmodels.api as sm

#  ------------------Question 2-------------------------------
# importing csv data to a pandas dataframe
data2 = pd.read_csv("HornedLizards.csv")

# dividing survived and dead row data based on column value
data2 = data2.dropna()
survived = data2.loc[data2["Survive"] == "survived"]
# loc gets rows (and/or columns) with particular labels. iloc gets rows (and/or columns) at integer locations.
# need to avoid first string column. therefore start
survived = survived.iloc[0:, 0]
print(survived)

dead = data2.loc[data2["Survive"] == "dead"]
dead = dead.iloc[:, 0]
print(dead)

# statistics for survived
print(survived.describe())

# statistics for dead
print(dead.describe())

# histogram for survived & dead
histogram = sns.histplot(data=survived, color="green")
histogram = sns.histplot(data=dead, color="red")
plt.title("Histogrm of survived horned lizards dataset")
plt.legend()
plt.savefig("figure 1")
plt.show()

# QQ plot for sample 1 & 2
fig, ax = plt.subplots(figsize=(8, 3))
sm.qqplot(data=survived, color="green", ax=ax)
sm.qqplot(data=dead, color="red", ax=ax)
plt.title("Quantile-Quantile plot of survived & dead dataset")
plt.show()

# histogram for both samples
histogram = sns.histplot(data=survived, color="green")
histogram = sns.histplot(data=dead, color="red")
plt.title("Histogrm of horned lizards dataset")
plt.legend()
plt.show()

# normality test

nt_survived = ss.shapiro(x=survived)
print(nt_survived)
nt_dead = ss.shapiro(x=dead)
print(nt_dead)

# Boxplots for both datasets
box1 = plt.boxplot(x=survived)
plt.title("Boxplot of survived horned lizards")
plt.show()

box2 = plt.boxplot(x=dead)
plt.title("Boxplot of dead horned lizards")
plt.show()

# violin plots
violin1 = plt.violinplot(dataset=survived)
violin2 = plt.violinplot(dataset=dead)
plt.title("Violin plot of survived horned lizards")
plt.legend()
plt.show()

violin2 = plt.violinplot(dataset=dead)
plt.title("Violin of dead horned lizards")
plt.show()

# testing tharuka sir's example
fig, ax = plt.subplots(figsize=(8, 3))
sns.histplot(survived, bins=30, kde=True, color="green", label="Survived", ax=ax)
sns.histplot(dead, bins=30, kde=True, color="red", label="dead", ax=ax)
plt.title("Histogram of lizard horn lengths for dead vs surviving lizards")
plt.legend()
plt.savefig("my histogram")
plt.show()

# boxplots
fig, ax = plt.subplots()
ax.boxplot([survived, dead], notch=True, capwidths=[0.01, 0.2])
plt.xlabel("Samples")
plt.ylabel("data")
plt.title("Boxplot of survived & dead horned lizards")
plt.show()

# two sample t-test
t_test = ss.ttest_ind(a=survived, b=dead, equal_var=True, alternative='two-sided')
print(t_test)
