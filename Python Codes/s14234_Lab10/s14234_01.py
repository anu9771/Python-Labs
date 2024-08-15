"""
Implementation of KMeans clustering algorithm to predict labels the species names of iris dataset.
input: iris data set
output: predicted labels and species names
date: 11/02/2022
author: Anushka Udara
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# implement kmeans model for sepal width and sepal length.
# insert csv data to a pandas dataframe
iris = pd.read_csv("iris.csv")
iris = iris.dropna()

# use pd.iloc to give data rows and columns
iris_data = iris.iloc[:, 0:2]
# setting up standard scaler using iris data
scaler = StandardScaler().fit(iris_data)


standardized_data = scaler.transform(iris_data)
# implementing kmeans setting up three clusters
kmeans = KMeans(n_clusters=3, random_state=None).fit(standardized_data)

# centroids
centroids = kmeans.cluster_centers_
print(centroids)

labels = kmeans.labels_

# deciding the variety of new data using k means algorithm
new_data = [[4.6, 3.0], [6.2, 3.0]]
new_data = pd.DataFrame(data=new_data, index=[1, 2])

# standardization of data
new_standardized_data = scaler.transform(new_data)

# predicting the species of new data
new_labels = kmeans.predict(new_standardized_data)
print("new labels", new_labels)

# getting original species names using iris.
unique_labels = pd.unique(labels)
unique_names = pd.unique(iris.iloc[:, 5])

# inserting unique names and labels to a dictionary
mappings = {}
for i in range(0, 3):
    mappings[unique_labels[i]] = unique_names[i]

# Drawing the scatter plot
# insert data points
plt.scatter(standardized_data[:, 0], standardized_data[:, 1], c=labels.astype(float), alpha=0.8)
# insert assigned labels for the data points
# please modify arrow details
for index, text in enumerate(kmeans.labels_):
    # insert standardized data points
    plt.text(standardized_data[:, 0][index], standardized_data[:, 1][index], s=text)
    # adding arrows and species names to data points
    plt.annotate(str(mappings[text]), (standardized_data[:, 0][index], standardized_data[:, 1][index]),
                 xytext=(standardized_data[:, 0][index] + 0.09, standardized_data[:, 1][index] + 0.4),
                 color="gray", arrowprops={"arrowstyle": "<-", "color": "gray"})

# insert centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=50, c="red", alpha=0.8)
# insert new data points
for index, text in enumerate(new_labels):
    plt.scatter(new_standardized_data[:, 0], new_standardized_data[:, 1], c="green")
    # insert arrows and species names
    plt.annotate(str(mappings[text]), (new_standardized_data[:, 0][index], new_standardized_data[:, 1][index]),
                 xytext=(new_standardized_data[:, 0][index] + 0.09, new_standardized_data[:, 1][index] + 0.4),
                 color="green", arrowprops={"arrowstyle": "<-", "color": "green"})
plt.show()


# printing species names for new labels
for label in new_labels:
    print(label, ": ", mappings.get(label))

# --------------------------------------------------------------------------------------------------------------------
# implement kmeans model for petal width and petal length.
# use pd.iloc to give data rows and columns
iris_data = iris.iloc[:, 2:4]

# standardization of data - fitting the scaler
scaler = StandardScaler().fit(iris_data)

standardized_data = scaler.transform(iris_data)

# implementing kmeans setting up three clusters
kmeans = KMeans(n_clusters=3, random_state=None).fit(standardized_data)

centroids = kmeans.cluster_centers_
print(centroids)

labels = kmeans.labels_

# deciding the variety of new data using k means algorithm
new_data = [[1.5, 0.2], [4.1, 1.2]]
new_data = pd.DataFrame(data=new_data, index=[1, 2])

# standardization of data
new_standardized_data = scaler.transform(new_data)

# predicting the species of new data
new_labels = kmeans.predict(new_standardized_data)
print("labels", new_labels)

# getting original species names using iris.
unique_labels = pd.unique(labels)
unique_names = pd.unique(iris.iloc[:, 5])

# inserting unique names and labels to a dictionary
mappings = {}
for i in range(0, 3):
    mappings[unique_labels[i]] = unique_names[i]

# Drawing the scatter plot
# insert data points
plt.scatter(standardized_data[:, 0], standardized_data[:, 1], c=labels.astype(float), alpha=0.8)
# insert assigned labels for the data points
# please modify arrow details
for index, text in enumerate(kmeans.labels_):
    # insert standardized data points
    plt.text(standardized_data[:, 0][index], standardized_data[:, 1][index], s=text)
    # adding arrows and species names to data points
    plt.annotate(str(mappings[text]), (standardized_data[:, 0][index], standardized_data[:, 1][index]),
                 xytext=(standardized_data[:, 0][index] + 0.09, standardized_data[:, 1][index] + 0.4),
                 color="gray", arrowprops={"arrowstyle": "<-", "color": "gray"})

# insert centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=50, c="red", alpha=0.8)
# insert new data points
for index, text in enumerate(new_labels):
    plt.scatter(new_standardized_data[:, 0], new_standardized_data[:, 1], c="green")
    # insert arrows and species names
    plt.annotate(str(mappings[text]), (new_standardized_data[:, 0][index], new_standardized_data[:, 1][index]),
                 xytext=(new_standardized_data[:, 0][index] + 0.09, new_standardized_data[:, 1][index] + 0.4),
                 color="green", arrowprops={"arrowstyle": "<-", "color": "green"})
plt.show()

# printing species names for new labels
for label in new_labels:
    print(label, ": ", mappings.get(label))


