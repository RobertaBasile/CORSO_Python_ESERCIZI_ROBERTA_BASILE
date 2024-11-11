# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.



# Esercizio:


# Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# Verifica il tipo di dato dell'array e stampa il risultato.
# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# Stampa la forma dell'array.
# 1. versione senza oggetto
# import numpy as np

# # Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49
# array = np.arange(10, 50)

# # Verifica il tipo di dato dell'array e stampa il risultato
# print("Tipo di dato dell'array:", array.dtype)

# # Cambia il tipo di dato dell'array in float64
# array = array.astype(np.float64)

# # Verifica di nuovo il tipo di dato e stampa il risultato
# print("Nuovo tipo di dato dell'array:", array.dtype)

# # Stampa la forma dell'array
# print("Forma dell'array:", array.shape)

#versione con oggetto

import numpy as np

class gestoreArray:
    def __init__(self):
        self.array = None

    def crea_array(self, start, end):
        self.array = np.arange(start, end)
        return self.array

    def verifica_tipo(self):
        return self.array.dtype

    def cambia_tipo(self, nuovo_tipo):
        self.array = self.array.astype(nuovo_tipo)
        return self.array

    def stampa_forma(self):
        return self.array.shape


def main():
    gestore = gestoreArray()

    # Creare un array di numeri interi da 10 a 49
    array = gestore.crea_array(10, 50)
    print("Array creato:", array)

    # Verifica il tipo di dato dell'array e stampa il risultato
    tipo = gestore.verifica_tipo()
    print("Tipo di dato dell'array:", tipo)

    # Cambia il tipo di dato dell'array in float64
    array = gestore.cambia_tipo(np.float64)

    # Verifica di nuovo il tipo di dato e stampa il risultato
    nuovo_tipo = gestore.verifica_tipo()
    print("Nuovo tipo di dato dell'array:", nuovo_tipo)

    # Stampa la forma dell'array
    forma = gestore.stampa_forma()
    print("Forma dell'array:", forma)

# Avvia il programma
x = gestoreArray()
main()
