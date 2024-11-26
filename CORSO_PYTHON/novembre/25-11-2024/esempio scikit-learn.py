from sklearn.datasets import load_iris
data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target

#-------------------------------------------------

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#-------------------------------------------------
#regressione lineare

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

#-------------------------------------------------
#k nearest neighbors

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
predictions = knn.predict(X)