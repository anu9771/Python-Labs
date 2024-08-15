"""
Implementation of KNearest neighbors algorithm to predict labels the species names of neighbor iris plants.
input: iris data set
output: predicted labels and species names of neighbor iris plants.
date: 11/02/2022
author: Anushka Udara
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset
iris = load_iris()
features = iris.data

# extracting labels
labels = iris.target

# standardizing data
scaler = StandardScaler().fit(features)
features_standardized_data = scaler.transform(features)

# creating test data
test_data = [[4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]]

# standardizing test data
standardized_test_data = scaler.transform(test_data)

# extracting sepal data
sepal_data = features_standardized_data[:, 0:2]

# creating a dictionary to match labels and species.
mappings = {}
unique_labels = pd.unique(labels)
unique_names = iris.target_names

for i in range(0, 3):
    mappings[unique_labels[i]] = unique_names[i]

# using only sepal measurements------------------------------------------------------------------------

# find two nearest neighbors ------------------------------------
nearest_neighbors = NearestNeighbors(n_neighbors=2).fit(sepal_data)

# selecting sepal measurements from test data
test_sepal_data = standardized_test_data[:, 0:2]

# predicting two nearest neighbors of sepal data
distances, indices = nearest_neighbors.kneighbors(test_sepal_data)

print("\nsepal data- two nearest neighbors\n")
print("indexes are: ", indices)
# data values
print("Data values", features[indices])
# labels
predicted_labels = iris['target'][indices]
print("predicted labels of plant 1 neighbors", predicted_labels[0])
print("predicted labels of plant 2 neighbors", predicted_labels[1], "\n")

# printing species names of predicted neighbors
for plant in predicted_labels:
    for neighbor in plant:
        print(neighbor, " :", mappings[neighbor])

# find five nearest neighbors ------------------------------------
nearest_neighbors = NearestNeighbors(n_neighbors=5).fit(sepal_data)

# predicting two nearest neighbors of sepal data
distances, indices = nearest_neighbors.kneighbors(test_sepal_data)

print("\nsepal data- five nearest neighbors\n")
print("indexes are: ", indices)
# data values
print("Data values", features[indices])
# labels
predicted_labels = iris['target'][indices]
print("predicted labels of plant 1 neighbors", predicted_labels[0])
print("predicted labels of plant 2 neighbors", predicted_labels[1], "\n")

predicted_new_labels = []
for plant in predicted_labels:
    for neighbor in plant:
        predicted_new_labels.append(neighbor)

# printing species names of predicted neighbors
for plant in predicted_labels:
    for neighbor in plant:
        print(neighbor, " :", mappings[neighbor])

# entering true labels of both plants' neighbors to one list
y_true = []
for plant in labels[indices]:
    for neighbor in plant:
        y_true.append(neighbor)

# Probability of each plant species.
knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(sepal_data, labels)
probability = knn.predict_proba(sepal_data)
print(probability)

# using only petal measurements-----------------------------------------------------------------------------------

# extracting petal data
petal_data = features_standardized_data[:, 2:4]

# find two nearest neighbors ------------------------------------
nearest_neighbors = NearestNeighbors(n_neighbors=2).fit(petal_data)

# selecting sepal measurements from test data
test_petal_data = standardized_test_data[:, 2:4]

# predicting two nearest neighbors of sepal data
distances, indices = nearest_neighbors.kneighbors(test_petal_data)

print("\npetal data- two nearest neighbors\n")
print("indexes are: ", indices)
# data values
print("Data values", features[indices])
# labels
predicted_labels = iris['target'][indices]
print("predicted labels of plant 1 neighbors", predicted_labels[0])
print("predicted labels of plant 2 neighbors", predicted_labels[1], "\n")

# printing species names of predicted neighbors
for plant in predicted_labels:
    for neighbor in plant:
        print(neighbor, " :", mappings[neighbor])

# find five nearest neighbors ------------------------------------
nearest_neighbors = NearestNeighbors(n_neighbors=5).fit(petal_data)

# predicting two nearest neighbors of sepal data
distances, indices = nearest_neighbors.kneighbors(test_petal_data)

print("\npetal data- five nearest neighbors\n")
print("indexes are: ", indices)
# data values
print("Data values", features[indices])
# labels
predicted_labels = iris['target'][indices]
print("predicted labels of plant 1 neighbors", predicted_labels[0])
print("predicted labels of plant 2 neighbors", predicted_labels[1], "\n")

# printing species names of predicted neighbors
for plant in predicted_labels:
    for neighbor in plant:
        print(neighbor, " :", mappings[neighbor])

# entering true labels of both plants' neighbors to one list
y_true = []
for plant in labels[indices]:
    for neighbor in plant:
        y_true.append(neighbor)


knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(petal_data, labels)
probability = knn.predict_proba(petal_data)
print(probability)

# using both measurements-------------------------------------------------------------------------

# find two nearest neighbors ------------------------------------
nearest_neighbors = NearestNeighbors(n_neighbors=2).fit(features_standardized_data)

# predicting two nearest neighbors of sepal data
distances, indices = nearest_neighbors.kneighbors(standardized_test_data)

print("\nSepal & Petal data- two nearest neighbors\n")
print("indexes are: ", indices)
# data values
print("Data values", features[indices])
# labels
predicted_labels = iris['target'][indices]
print("predicted labels of plant 1 neighbors", predicted_labels[0])
print("predicted labels of plant 2 neighbors", predicted_labels[1], "\n")

# printing species names of predicted neighbors
for plant in predicted_labels:
    for neighbor in plant:
        print(neighbor, " :", mappings[neighbor])

# find five nearest neighbors ------------------------------------
nearest_neighbors = NearestNeighbors(n_neighbors=5).fit(features_standardized_data)

# predicting two nearest neighbors of sepal data
distances, indices = nearest_neighbors.kneighbors(standardized_test_data)

print("\nSepal & Petal- five nearest neighbors\n")
print("indexes are: ", indices)
# data values
print("Data values", features[indices])
# labels
predicted_labels = iris['target'][indices]
print("predicted labels of plant 1 neighbors", predicted_labels[0])
print("predicted labels of plant 2 neighbors", predicted_labels[1], "\n")

# printing species names of predicted neighbors
for plant in predicted_labels:
    for neighbor in plant:
        print(neighbor, " :", mappings[neighbor])

# entering true labels of both plants' neighbors to one list
y_true = []
for plant in labels[indices]:
    for neighbor in plant:
        y_true.append(neighbor)

# probability = accuracy_score(y_true, predicted_new_labels)
# print("probability of each plant categorizing into each species\n", probability)
knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(features_standardized_data, labels)
probability = knn.predict_proba(features_standardized_data)
print(probability)
