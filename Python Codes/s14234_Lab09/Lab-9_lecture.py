import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as ss
import statsmodels.api as sm

data = pd.read_csv("HornedLizards.csv")

data = data.dropna()

survived = data.loc[data['Survive'] == "survived"]
survived = survived.iloc[:, 0]
print(survived)
print(np.array([1, 2, 3, 4]))

a1 = np.array([[1, 2, 3], [4, 5, 6]])

print(a1)
print(a1.shape)

print(a1[0, :])

print(a1.dtype)

# a2 = np.array([[1,2,3],[4,5,6],[0,7,8,9,0]])
#
# print(a2.dtype)

print(np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32))
print(np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64))
print(np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex64))

a3 = np.array([1, 2, 3])
print(a3.mean())

# Generating random numbers
a4 = np.random.rand(10)
print(a4)

# plotting a standard normal distribution
rn1 = np.random.randn(10000)
print(rn1)

# visualization


# histogram -
plt.hist(a4)
plt.title("Histogram of random numbers")

# plt.show()
plt.savefig("Histogram.jpg")
# ---------------------------------
plt.hist(rn1)
plt.title("Histogram of random numbers")

# plt.show()
plt.savefig("Histogram1.jpg")

# within brackets, we have metioned we need 1row and two columns for two plots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
axs[0].hist(rn1)
axs[0].set_title("Histogram of random numbers")
axs[1].hist(a4)
axs[1].set_title("Histogram of random numbers")
# plt.show()

# Boxplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
axs[0].boxplot(rn1)
axs[0].set_title("Boxplot of random numbers")
axs[1].boxplot(a4)
axs[1].set_title("Boxplot of random numbers")
# plt.show()

# using seaborn
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(rn1, bins=30, kde=True, ax=axs[0])
axs[0].set_title("Boxplot of random numbers")
sns.histplot(a4, bins=30, kde=True, ax=axs[1])
axs[1].set_title("Boxplot of random numbers")
# plt.show()

# pandas
# data = ["Ishani",70,90]
df = pd.DataFrame([["Ishani", 70, 90], ["hansi", 75, 85]], columns=["student name", "Chem marks", "Phy marks"])
print(df)
print("\n")

# Using a data file
marks = pd.read_csv("student_marks.csv")
print(marks)

# plotting
print(marks.info())
print(marks.describe())

fig, axs = plt.subplots(figsize=(8, 8))
sns.boxplot(data=marks[["Student name"], ["chem marks"], ["Phy marks"]], ax=axs)
plt.show()
