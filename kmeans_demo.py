#https://www.w3schools.com/python/python_ml_getting_started.asp

#tools > manage packages > install matplotlib 
import matplotlib.pyplot as plt
#tools > manage packages > install scikit-learn
from sklearn.cluster import KMeans
import random


x = [1, 1, 2, 8, 9]
y = [2, 4, 3, 8, 10]


# x1 = [random.randrange(0,700) for i in range(500)]
# y1 = [random.randrange(400,1000) for i in range(500)]
# x2 = [random.randrange(400,1000) for i in range(500)]
# y2 = [random.randrange(0,700) for i in range(500)]
# x = x1 + x2
# y = y1 + y2


plt.scatter(x, y)
plt.show()

data = list(zip(x, y))


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()
