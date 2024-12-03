# Esercizio 3: Pandas e Numpy e Visualizzazione 
# Descrizione: Crea un dataset autogenerandolo monolineare con 50 posizioni matematica e cambia la sua forma 
# in 10 file da 5, normalizza i valori e rendili interi , 
# nessun valore deve essere uguale a un altro sulla stessa linea della collezione  
# dopodiché stampa un grafico che lo rappresenti. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generazione del dataset monolineare con 50 posizioni
data = np.random.randint(1, 100, size=50)

# Cambia la forma del dataset in 10 file da 5
data_reshaped = data.reshape(10, 5)

# Normalizzazione dei valori e conversione in interi
# (data_reshaped - np.min(data_reshaped)): Sottrae il valore minimo del dataset da ogni elemento.

# /(np.max(data_reshaped) - np.min(data_reshaped)): 
# Divide ogni elemento per la differenza tra il valore massimo e il valore minimo del dataset.
data_normalized = (data_reshaped - np.min(data_reshaped)) / (np.max(data_reshaped) - np.min(data_reshaped))
#(data_normalized * 100).astype(int): Moltiplica i valori normalizzati per 100 e li converte in interi utilizzando astype(int).
data_normalized = (data_normalized * 100).astype(int)

### Assicurarsi che nessun valore sia uguale a un altro sulla stessa linea

# 1. **Iterazione sulle righe**:
#    - `for row in data_normalized:`: Questo ciclo `for` itera su ogni riga del dataset `data_normalized`. Ogni riga è rappresentata dalla variabile `row`.

# 2. **Controllo di unicità**:
#    - `while len(set(row)) != len(row):`: Questo ciclo `while` verifica se tutti i valori in una riga sono unici. La funzione `set()` converte la riga in un insieme (che contiene solo valori unici). Se la lunghezza dell'insieme (`len(set(row))`) è diversa dalla lunghezza della riga (`len(row)`), significa che ci sono valori duplicati nella riga.

# 3. **Generazione di nuovi valori**:
#    - `row[:] = np.random.choice(np.arange(1, 101), size=row.shape, replace=False)`: 
# Se ci sono valori duplicati, questa riga di codice genera una nuova riga di valori casuali unici tra 1 e 100 (inclusi) 
# e sostituisce la riga corrente con questi nuovi valori. La funzione `np.random.choice()` 
# viene utilizzata per generare i valori casuali, con l'argomento `replace=False` che garantisce che i valori siano unici.


#------------------------------
for row in data_normalized:
    while len(set(row)) != len(row):
        row[:] = np.random.choice(np.arange(1, 101), size=row.shape, replace=False)

# Creazione del DataFrame
df = pd.DataFrame(data_normalized, columns=[f'Colonna {i+1}' for i in range(5)])

# Visualizzazione del DataFrame
print(df)

# Stampa del grafico
plt.figure(figsize=(10, 6))
for i in range(df.shape[1]):
    plt.plot(df.index, df.iloc[:, i], marker='o', label=f'Colonna {i+1}')
plt.title('Grafico del Dataset Normalizzato')
plt.xlabel('Indice')
plt.ylabel('Valori Normalizzati')
plt.legend()
plt.grid(True)
plt.show()
