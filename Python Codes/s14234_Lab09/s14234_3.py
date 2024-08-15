# ----------------question 3------------
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as ss
import numpy as np
import statsmodels.api as sm

# import the dataset
data = pd.read_csv("BlackbirdTestosterone.csv")
print(data)

# statistics
print(data.describe())
# mean = data['log before'].mean()
# print('log before mean: ', mean)
# std = data['log before'].std()
# print('log before std: ', std)
#
# mean = data['log after'].mean()
# print('log after mean: ', mean)
# std = data['log after'].std()
# print('log after std: ', std)
#
# mean = data['dif in logs'].mean()
# print('log difference mean: ', mean)
# std = data['dif in logs'].std()
# print('log difference std: ', std)

# Histogram
log_dif = data.iloc[0:, 4]
print(log_dif)
histogram = sns.histplot(data=log_dif)
plt.title("Histogram of the log difference variable")
plt.show()

# QQ plot of log diiference
QQplot = sm.qqplot(data=log_dif)
plt.title("Quantile-Quantile plot of the log difference variable")
plt.show()

# Normality test
nt = ss.shapiro(log_dif)
print(nt,"\n")

# box plots
box1 =sns.boxplot(data=data.iloc[0:, 2])
plt.title("Box plot of the log before variable")
plt.show()

box2 =sns.boxplot(data=data.iloc[0:, 3])
plt.title("Box plot of the log after variable")
plt.show()

# violin plots
vio1 = sns.violinplot(data=data.iloc[0:, 2])
plt.title("Violin plot of the log before variable")
plt.show()

vio1 = sns.violinplot(data=data.iloc[0:, 3])
plt.title("Violin plot of the log after variable")
plt.show()

# paired t-test
t_test = ss.ttest_rel(a=data.iloc[0:, 2], b=data.iloc[0:, 3], alternative='less')
print(t_test)















