# 1. Carica il dataset Wine Carica il dataset Wine dal modulo datasets di scikit-learn. 
# 2. Standardizza le caratteristiche Standardizza le caratteristiche utilizzando StandardScaler per portare tutte le feature su una scala comune. 
# 3. Suddividi i dati in training e test set Suddividi i dati in due set: il 70% per il training e il 30% per il test. 
# 4. Applica un algoritmo di classificazione Applica l'algoritmo DecisionTreeClassifier per la classificazione. 
# 5. Valuta la performance del modello Valuta la performance del modello utilizzando il classification_report, con metriche come precisione, recall e F1-score. 
# 6. Visualizza la matrice di confusione Genera e visualizza la matrice di confusione per valutare la qualità della classificazione.

# Importa le librerie necessarie
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il dataset Wine
wine = load_wine()
X = wine.data
y = wine.target

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
report = classification_report(y_test, y_pred, target_names=wine.target_names)
print("Classification Report:\n", report)

# Visualizza la matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
