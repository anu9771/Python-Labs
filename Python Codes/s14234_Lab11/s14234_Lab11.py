"""
Implementing an ANN using the iris dataset
input: iris data csv file
Output: predicted labels, classfication report and confusion matrix
date: 8/02/2022
author: Anushka Udara
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np

# Load iris data from the csv
iris = pd.read_csv("iris.csv")
print(iris)
# dividing the dataset into X and Y variables.
X = iris.iloc[:, 0:4]

Y = iris.iloc[:, 5]

# Replace Y variable with integer values
# printing unique labels
labels = pd.unique(Y)
print(labels)

encoder = LabelEncoder()
# fit the whole data set
encoder.fit(Y)

Y = encoder.transform(Y)

# Splitting dataset into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)
print(Y_train)
print(Y_test)

# Standardizing the training and test data
scaler = StandardScaler()
# data scale is fit for training dataset. same scale is used for both X datasets
scaler.fit(X_train)
# then that scale is used standardization of test dataset also.
standardized_X_train = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)
# no need to standardize Y data, because it contains only labels.

# implementing the ANN
clf = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
Y_train = np.ravel(Y_train)
clf.fit(X_train, Y_train)

# predicting the species labels for test data using the trained ANN
predictions = clf.predict(X_test)
print(predictions)

# making a dictionary with labels and predictions
mappings = {}

Y_values = encoder.transform(labels)
for i in Y_values:
    mappings[i] = labels[i]

# printing the classification report and confusion matrix
print(classification_report(Y_test, predictions))
print(confusion_matrix(Y_test, predictions))

# predicting the labels for new samples
# inserting new data to a pandas dataframe
data = [[5.9, 3.0, 7.0, 5.0], [4.6, 3.0, 1.5, 0.2], [6.2, 3.0, 4.1, 1.2]]
new_data = pd.DataFrame(data=data, index=[1, 2, 3])

# standardizing new data
standardized_new_data = scaler.transform(new_data)

# predicting species names for new data
new_predictions = clf.predict(standardized_new_data)
print(new_predictions)

# printing the species of predicted labels
for prediction in new_predictions:
    print(prediction, ": ", mappings[prediction])

# implementing the ANN with 3 hidden layers with 2 nodes.
clf = MLPClassifier(hidden_layer_sizes=(2, 2, 2), max_iter=1000)
Y_train = np.ravel(Y_train)
clf.fit(X_train, Y_train)

# predicting the species labels for test data using the trained ANN
predictions = clf.predict(X_test)
print(predictions)

# printing the classification report and confusion matrix
print(classification_report(Y_test, predictions))
print(confusion_matrix(Y_test, predictions))
