from matplotlib import pyplot as plt
import pandas as pd
import scipy.stats as ss
from statsmodels.graphics.mosaicplot import mosaic as sm

# creating data set - do not enter row & column totals
data = {'Uninfected': [1, 49],
        'Lightly infected': [10, 35],
        'Highly infected': [37, 9]}

# creating a dataframe
table = pd.DataFrame(data, index=['Eaten by birds', 'Not eaten by birds'])
print(table)

# draw the mosaic plot
mosaic = sm(data=table.stack())
plt.title("Mosaic plot of the frequencies of fish eaten or not eaten by birds according to trematode infection level")
plt.show()

# chi square test
chi2, p, dof, expected = ss.chi2_contingency(table)

print(f"chi2 statistic:     {chi2:.5g}")
print(f"p-value:            {p:.5g}")
print(f"degrees of freedom: {dof}")


# printing the expected frequencies
expected_values = pd.DataFrame(expected)
print("expected frequencies:")
print(expected_values)
