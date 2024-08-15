from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as ss
import numpy as np
import statsmodels.api as sm

#  ------------------Question 1-------------------------------
# importing csv data to a pandas dataframe
data = pd.read_csv("Temperature.csv")

# printing mean, standard deviation, count, max, min
print(data.describe())

# drawing the histogram
histogram = sns.histplot(data=data)
plt.title("Histogrm of temperature dataset")
plt.show()

# QQ plot
QQplot = sm.qqplot(data=data['temperature'])
plt.title("Quantile-Quantile plot")
plt.show()

# normality test
nt = ss.shapiro(x=data)
print(nt)

# perform one sample T-test
one_sampt = ss.ttest_1samp(a=data, popmean=98.6, alternative="two-sided")
print(one_sampt)


