import numpy as np
from pandas import DataFrame
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

Data = {
    "x": [25, 34, 22, 27, 33, 24, 35, 32, 26],

    "y": [72, 51, 53, 78, 59, 61, 64, 68, 57]
}

# print(Data)

df = DataFrame(Data, columns=["x", "y"])

# print(df)

kmeans = KMeans(n_clusters=3).fit(df)
# print(kmeans)

centroids = kmeans.cluster_centers_
# print(centroids)

labels = kmeans.labels_
print(labels)

dnew = np.array([[26, 70], [33, 40], [25, 50], [40, 30]])
print(dnew)

# predicting new values according to the model
prv = kmeans.predict(dnew)
print(prv)

plt.scatter(df['x'], df['y'], c=labels.astype(float), s=50, alpha=0.5)

# adding th centroids to the scatter plot
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100)

# annotate the plot, enumerate values to clusters
for index, value in enumerate(labels):
    plt.annotate(value, (df['x'][index], df['y'][index]))

plt.scatter(dnew[:, 0], dnew[:, 1], c='green', s=50)
plt.show()
for i, txt in enumerate(prv):
    #    plt.annotate(txt, dnew[:,0][i], dnew[:,1][i])
    plt.annotate(txt, dnew['x'][i], dnew['y'][i])

# change the value of clusters and see
# use roc curves
