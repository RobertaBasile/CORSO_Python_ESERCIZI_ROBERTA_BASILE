# Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:
# Restituite la somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi;
# Unite i 2 array secondo l'asse 1
import numpy as np

# Creazione dei due array bidimensionali 4x4 con valori interi casuali
array1 = np.random.randint(0, 10, (4, 4))
array2 = np.random.randint(0, 10, (4, 4))

print("Array 1:\n", array1)
print("Array 2:\n", array2)

# Somma degli elementi nell'ultima riga dalla seconda colonna in poi
somma_array1 = np.sum(array1[-1, 1:])
somma_array2 = np.sum(array2[-1, 1:])

print("Somma degli elementi nell'ultima riga di Array 1 dalla seconda colonna in poi:", somma_array1)
print("Somma degli elementi nell'ultima riga di Array 2 dalla seconda colonna in poi:", somma_array2)

# Unione dei due array secondo l'asse 1
array_unito = np.concatenate((array1, array2), axis=1)

print("Array unito:\n", array_unito)
