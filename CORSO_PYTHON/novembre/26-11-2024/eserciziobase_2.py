# Carica il dataset Iris.
# Standardizza le caratteristiche
# utilizzando StandardScaler.
# Suddividi i dati in training e test set
# (70% training, 30% test).
# Applica l'algoritmo
# DecisionTreeClassifier.
# Valuta la performance del modello
# utilizzando il classification_report
# (precisione, recall, F1-score).
# Visualizza la matrice di confusione.

# Importa le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Standardizza le caratteristiche utilizzando StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Suddividi i dati in training e test set (70% training, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Applica l'algoritmo DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predici le etichette per il set di test
y_pred = clf.predict(X_test)

# Valuta la performance del modello utilizzando il classification_report
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

# Visualizza la matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
