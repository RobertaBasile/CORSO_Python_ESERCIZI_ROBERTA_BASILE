# Esercizio su NumPy Slicing



# Consegna:

# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
# Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
# Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
# Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
# Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
# Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.


# Obiettivo:

# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.

import numpy as np

class gestoreArray:
    def __init__(self):
        self.array = None

    def crea_array(self, start, end, size):
        self.array = np.random.randint(start, end, size=size)
        return self.array
# La sintassi base per lo slicing in NumPy è:
# array[start:stop:step]
    def estrai_primi_10(self):
        return self.array[:10]

    def estrai_ultimi_5(self):
        return self.array[-5:]

    def estrai_indici_5_15(self):
        return self.array[5:15]

    def estrai_ogni_terzo(self):
        return self.array[::3]

    def modifica_indici_5_10(self):
        print ("prima ",self.array)
        self.array[5:10] = 99
        return self.array

    def stampa_array(self):
        print("Array originale:", self.array)
        print("Primi 10 elementi:", self.estrai_primi_10())
        print("Ultimi 5 elementi:", self.estrai_ultimi_5())
        print("Elementi dall'indice 5 all'indice 15 (escluso):", self.estrai_indici_5_15())
        print("Ogni terzo elemento:", self.estrai_ogni_terzo())
        print("Array modificato (indici 5-10 assegnati a 99):", self.modifica_indici_5_10())

# Esempio di utilizzo
def main():
    gestore = gestoreArray()

    # Creare un array NumPy 1D di 20 numeri interi casuali 
    # compresi tra 10 e 50
    array = gestore.crea_array(10, 51, 20)
    gestore.stampa_array()

# Avvia il programma
x = gestoreArray()
main()

    