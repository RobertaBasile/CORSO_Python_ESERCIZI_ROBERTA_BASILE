# import numpy as np
# # # # Creazione di un array unidimensionale
# # # arr = np.array([1, 2, 3, 4, 5])

# # # # Creazione di un array bidimensionale
# # # arr2d = np.array([[1, 2, 3], [4, 5, 6]])
# # #------------------------------------------------------------------------------------------

# # # import numpy as np

# # # # Creazione di un array
# # # arr = np.array([1, 2, 3, 4, 5])


# # # # Utilizzo di alcuni metodi
# # # print("Forma dell'array:", arr.shape)  # Output: (5,)
# # # print("Dimensioni dell'array:", arr.ndim)  # Output: 1
# # # print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)
# # # print("Numero di elementi:", arr.size)  # Output: 5
# # # print("Somma degli elementi:", arr.sum())  # Output: 15
# # # print("Media degli elementi:", arr.mean())  # Output: 3.0
# # # print("Valore massimo:", arr.max())  # Output: 5
# # # print("Indice del valore massimo:", arr.argmax())  # Output: 4

# # #-----------------------------------------------------------------------

# # # Il dtype specifica il tipo di dati contenuti nell'array. 

# # # Può essere int, float, bool, etc.



# # # Esempio:

# # # arr = np.array([1, 2, 3], dtype='int32')
# # # print(arr.dtype)  # Output: int32






# # # La shape di un array indica le sue dimensioni. 

# # # È una tupla che rappresenta il numero di elementi in ciascuna dimensione.



# # # Esempio:

# # # arr = np.array([[1, 2, 3], [4, 5, 6]])
# # # print(arr.shape)  # Output: (2, 3)

# # #---------------------------------------------------

# # # La funzione arange crea un array contenente una sequenza di numeri, simile a range di Python.



# # # Esempio:

# # # arr = np.arange(10)
# # # print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]






# # # La funzione reshape cambia la forma di un array senza modificarne i dati.



# # # Esempio:

# # # arr = np.arange(6)
# # # # #reshaped_arr = arr.reshape((2, 3))
# # # # reshaped_arr = arr.reshape((6, 1))
# # # print(reshaped_arr)
# # # Output:  [[0 1 2] [3 4 5]]
# # Gli array NumPy possono essere indicizzati e affettati in modo simile alle liste Python, ma con funzionalità aggiuntive.



# # Esempio:

# # arr = np.array([1, 2, 3, 4, 5])

# # # Indexing
# # print(arr[0])  # Output: 1

# # # Slicing
# # print(arr[1:3])  # Output: [2 3]

# # # Boolean Indexing
# # print(arr[arr > 2])  # Output: [3 4 5]

# #Gli array NumPy supportano il slicing e il fancy indexing, 
# # permettendo di estrarre porzioni di array e modificare 
# # il loro contenuto in modo efficiente.

# #Esempio:

# # arr_2d = np.array([[1, 2, 3, 4],
# #                    [5, 6, 7, 8],
# #                    [9, 10, 11, 12]])
# # # Slicing sulle righe
# # print(arr_2d[1:3])  # Output: [[ 5  6  7  8]
# #                    #          [ 9 10 11 12]]
# # # Slicing sulle colonne
# # print(arr_2d[:, 1:3])  # Output: [[ 2  3]
# #                        #          [ 6  7]
# #                        #          [10 11]]
# # # Slicing misto
# # print(arr_2d[1:, 1:3])  # Output: [[ 6  7]
# #                         #          [10 11]]

# # import numpy as np
# # arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# # # Slicing di base
# # print(arr[2:7])  # Output: [2 3 4 5 6]

# # # Slicing con passo
# # print(arr[1:8:2])  # Output: [1 3 5 7]

# # # Omettere start e stop
# # print(arr[:5])  # Output: [0 1 2 3 4]
# # print(arr[5:])  # Output: [5 6 7 8 9]

# # # Utilizzare indici negativi
# # print(arr[-5:])  # Output: [5 6 7 8 9]
# # print(arr[:-5])  # Output: [0 1 2 3 4]

# # Fancy Indexing in NumPy

# Fancy indexing è una tecnica che permette di selezionare elementi di un array utilizzando array di indici interi. 

# Questo consente una selezione complessa e flessibile di elementi rispetto allo slicing normale.



# Sintassi della Fancy Indexing



# arr = np.array([10, 20, 30, 40, 50])

# # Utilizzo di un array di indici
# indices = np.array([1, 3])
# print(arr[indices])  # Output: [20 40]

# # Utilizzo di una lista di indici
# indices = [0, 2, 4]
# print(arr[indices])  # Output: [10 30 50]

#Differenze tra Slicing e F.Indexing
# Slicing:

# È limitato a selezioni rettangolari.
# Restituisce una vista dell'array originale (non crea una copia).
# Utilizza indici di inizio, fine e passo.


# Fancy Indexing:

# Può selezionare elementi non contigui e in ordine arbitrario.
# Crea sempre una copia dei dati selezionati.
# Utilizza array di indici interi.





