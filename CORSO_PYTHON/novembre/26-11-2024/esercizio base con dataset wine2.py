# Carica il dataset Wine
# Utilizza il modulo datasets di scikit-learn per caricare il dataset Wine.
# Esplora il dataset
# Visualizza il numero di campioni per ciascuna classe e calcola le statistiche di base delle feature.
# Visualizzazione: crea un grafico a barre per mostrare la distribuzione delle classi.
# Riduci la dimensionalità  ***
# Applica la PCA (Principal Component Analysis) per ridurre le dimensioni delle feature a 2 componenti
# principali.
# Visualizzazione: crea un grafico scatter 2D per rappresentare i dati trasformati, con i punti colorati in
# base alla classe.
# Sudddividi i dati in training e test set
# Dividi i dati in due set: l'80% per il training e il 20% per il test.
# Applica un algoritmo di classificazione
# Utilizza un modello RandomForestClassifier per la classificazione.
# Valuta la performance del modello
# Valuta le prestazioni utilizzando le metriche di accuratezza, precisione, recall e F1-score.
# Visualizza l'importanza delle feature / caratteristiche
# Visualizza le feature più importanti del dataset Wine secondo il modello Random Forest, utilizzando un
# grafico a barre.
# Visualizza la matrice di confusione
# Genera e visualizza la matrice di confusione per valutare la qualità della classificazione.
# Visualizzazione: utilizza una heatmap per rappresentare la matrice di confusione in modo più chiaro.
# Ottimizza l'algoritmo  
# Utilizza la GridSearchCV per ottimizzare i parametri del Random Forest (ad esempio: numero di estimatori e
# profondità massima dell'albero).
# Importa le librerie necessarie

'''Il processo inizia importando le librerie necessarie come `numpy`, `pandas`, `matplotlib` e `seaborn` per manipolare e visualizzare i dati, 
mentre `scikit-learn` fornisce strumenti per il caricamento del dataset Wine, la PCA, la suddivisione dei dati, 
la classificazione con Random Forest e la valutazione delle prestazioni. 
Il dataset Wine viene caricato con `load_wine` e diviso in caratteristiche (`X`) e classi (`y`), 
per poi essere esplorato con statistiche descrittive e visualizzato tramite un grafico a barre per la distribuzione delle classi. 
Successivamente, viene applicata la PCA per ridurre le dimensioni delle caratteristiche a due componenti principali, 
rendendo possibile un grafico scatter 2D colorato in base alla classe. I dati sono poi divisi in training set (80%) e test set (20%) usando `train_test_split`. 
Un modello `RandomForestClassifier` viene addestrato con i dati di training e utilizzato per fare previsioni sul test set. 
Le prestazioni sono valutate con il report di classificazione, includendo metriche come precisione, recall, F1-score e accuratezza. 
L'importanza delle feature viene calcolata con `feature_importances_` e visualizzata come un grafico a barre. 
La matrice di confusione viene generata con `confusion_matrix` e rappresentata graficamente come una heatmap. 
Infine, `GridSearchCV` è utilizzato per ottimizzare i parametri del modello (ad esempio, numero di alberi e profondità massima), 
migliorando così le prestazioni del modello finale. Tutti i passi sono accompagnati da visualizzazioni per comprendere meglio i risultati.'''
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Carica il dataset
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name='class')

# Mostra le prime righe e statistiche base
print(X.head())
print(X.describe())

# Numero di campioni per classe
print(y.value_counts())

# Visualizza la distribuzione delle classi
y.value_counts().plot(kind='bar', color=['red', 'green', 'blue'])
plt.title('Distribuzione delle classi')
plt.xlabel('Classi')
plt.ylabel('Numero di campioni')
plt.show()

# Applica la PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Grafico scatter 2D
plt.figure(figsize=(8, 6))
for i, color in zip(range(3), ['red', 'green', 'blue']):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=f'Classe {i}', color=color)
plt.xlabel('Componente principale 1')
plt.ylabel('Componente principale 2')
plt.title('Dati ridotti a 2 dimensioni con PCA')
plt.legend()
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# Inizializza il modello
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predizioni
y_pred = model.predict(X_test)

# Valutazione delle performance
print('Report di classificazione:\n', classification_report(y_test, y_pred))


# Importanza delle feature
importances = pd.Series(model.feature_importances_, index=wine.feature_names)
importances.sort_values(ascending=False).plot(kind='bar', figsize=(10, 6))
plt.title('Importanza delle feature')
plt.show()


# Genera la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

# Heatmap della matrice
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.xlabel('Predizione')
plt.ylabel('Vero')
plt.title('Matrice di confusione')
plt.show()

# Definizione dei parametri da ottimizzare
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}

# Ottimizzazione
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Migliori parametri e performance
print('Migliori parametri:', grid_search.best_params_)
best_model = grid_search.best_estimator_
y_pred_optimized = best_model.predict(X_test)
print('Accuracy con modello ottimizzato:', accuracy_score(y_test, y_pred_optimized))
