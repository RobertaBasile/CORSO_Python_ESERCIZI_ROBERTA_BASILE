import numpy as np

class GestoreArray:
    def __init__(self):
        self.array = None

    def crea_array(self, start, end, size):
        self.array = np.random.randint(start, end, size=size)
        return self.array

    def estrai_primi_10(self):
        return self.array[:10]

    def estrai_ultimi_5(self):
        return self.array[-5:]

    def estrai_indici_5_15(self):
        return self.array[5:15]

    def estrai_ogni_terzo(self):
        return self.array[::3]

    def modifica_indici_5_10(self):
        self.array[5:10] = 99
        return self.array

    def stampa_array(self):
        print("Array originale:", self.array)
        print("Primi 10 elementi:", self.estrai_primi_10())
        print("Ultimi 5 elementi:", self.estrai_ultimi_5())
        print("Elementi dall'indice 5 all'indice 15 (escluso):", self.estrai_indici_5_15())
        print("Ogni terzo elemento:", self.estrai_ogni_terzo())
        print("Array modificato (indici 5-10 assegnati a 99):", self.modifica_indici_5_10())

def mostra_menu():
    print("\nMenu:")
    print("1. Crea un array di numeri interi casuali")
    print("2. Estrarre i primi 10 elementi dell'array")
    print("3. Estrarre gli ultimi 5 elementi dell'array")
    print("4. Estrarre gli elementi dall'indice 5 all'indice 15 (escluso)")
    print("5. Estrarre ogni terzo elemento dell'array")
    print("6. Modificare gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99")
    print("7. Stampare l'array originale e tutti i sottoarray ottenuti tramite slicing")
    print("8. Esci")

def main():
    gestore = GestoreArray()
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            start = int(input("Inserisci il valore iniziale: "))
            end = int(input("Inserisci il valore finale: "))
            size = int(input("Inserisci la dimensione dell'array: "))
            gestore.crea_array(start, end, size)
            print("Array creato.")
        elif scelta == "2":
            print("Primi 10 elementi:", gestore.estrai_primi_10())
        elif scelta == "3":
            print("Ultimi 5 elementi:", gestore.estrai_ultimi_5())
        elif scelta == "4":
            print("Elementi dall'indice 5 all'indice 15 (escluso):", gestore.estrai_indici_5_15())
        elif scelta == "5":
            print("Ogni terzo elemento:", gestore.estrai_ogni_terzo())
        elif scelta == "6":
            gestore.modifica_indici_5_10()
            print("Elementi dall'indice 5 all'indice 10 (escluso) modificati a 99.")
        elif scelta == "7":
            gestore.stampa_array()
        elif scelta == "8":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvia il programma
x = GestoreArray()
main()
