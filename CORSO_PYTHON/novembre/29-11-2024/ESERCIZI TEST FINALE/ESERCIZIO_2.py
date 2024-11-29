# Esercizio 2: ML
# Caricamento del dataset:
# Importa il dataset Iris utilizzando from sklearn.datasets import load_iris.
# Esplora brevemente i dati per capire le caratteristiche e le target.
# Preprocessing dei dati:
# Dividi i dati in set di addestramento e di test utilizzando train_test_split di scikit-learn (ad esempio, 70% training e 30% test).
# Costruzione del modello:
# Scegli un algoritmo di classificazione (ad esempio, K-Nearest Neighbors, Decision Tree, Support Vector Machine).
# Addestra il modello utilizzando il set di training.
# Valutazione del modello:
# Predici le specie nel set di test.
# Valuta le prestazioni del modello utilizzando metriche come accuratezza, precisione, richiamo e la matrice di confusione.
# Visualizzazione dei risultati:
# In fine crea grafici per visualizzare i risultati (ad esempio, plot della matrice di confusione).

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay

# Caricamento del dataset
iris = load_iris()
X = iris.data
y = iris.target

# Esplorazione dei dati
print("Caratteristiche:", iris.feature_names)
print("Target:", iris.target_names)

# Preprocessing dei dati
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Costruzione del modello
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Valutazione del modello
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuratezza: {accuracy}")
print(f"Precisione: {precision}")
print(f"Richiamo: {recall}")

# Visualizzazione dei risultati
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=iris.target_names)
disp.plot()
plt.show()
