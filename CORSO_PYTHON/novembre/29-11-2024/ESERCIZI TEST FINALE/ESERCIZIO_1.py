# Esercizio 1: Oggetti
# Descrizione:  Crea un programma in Python per gestire una semplice libreria di libri. Il programma dovrebbe presentare un menu all'utente con le seguenti opzioni:
# Aggiungere un nuovo libro: L'utente può inserire il titolo, l'autore e l'anno di pubblicazione del libro e quantità.
# Visualizzare tutti i libri: Mostra una lista di tutti i libri attualmente nella libreria.
# Cercare un libro per titolo: L'utente inserisce un titolo e il programma cerca e mostra i dettagli del libro se trovato.
# Gestione libri: Far rimuovere modificare e/o aggiungere una compia in più del libro
# Uscire dal programma: Termina l'esecuzione del programma.

class Libro:
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita

class Libreria:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def visualizza_libri(self):
        for libro in self.libri:
            print(f"Titolo: {libro.titolo}, Autore: {libro.autore}, Anno: {libro.anno}, Quantità: {libro.quantita}")

    def cerca_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo.lower() == titolo.lower():
                print(f"Titolo: {libro.titolo}, Autore: {libro.autore}, Anno: {libro.anno}, Quantità: {libro.quantita}")
                return libro
        print("Libro non trovato.")
        return None

    def gestisci_libro(self, titolo, azione):
        libro = self.cerca_libro(titolo)
        if libro:
            if azione == "rimuovi":
                self.libri.remove(libro)
                print("Libro rimosso.")
            elif azione == "modifica":
                nuovo_titolo = input("Nuovo titolo: ")
                nuovo_autore = input("Nuovo autore: ")
                nuovo_anno = input("Nuovo anno: ")
                nuova_quantita = int(input("Nuova quantità: "))
                libro.titolo = nuovo_titolo
                libro.autore = nuovo_autore
                libro.anno = nuovo_anno
                libro.quantita = nuova_quantita
                print("Libro modificato.")
            elif azione == "aggiungi":
                libro.quantita += 1
                print("Una copia aggiunta.")

def menu():
    libreria = Libreria()
    while True:
        print("\nMenu:")
        print("1. Aggiungere un nuovo libro")
        print("2. Visualizzare tutti i libri")
        print("3. Cercare un libro per titolo")
        print("4. Gestione libri")
        print("5. Uscire dal programma")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            titolo = input("Titolo: ")
            autore = input("Autore: ")
            anno = input("Anno: ")
            quantita = int(input("Quantità: "))
            libro = Libro(titolo, autore, anno, quantita)
            libreria.aggiungi_libro(libro)
            print("Libro aggiunto.")
        elif scelta == "2":
            libreria.visualizza_libri()
        elif scelta == "3":
            titolo = input("Inserisci il titolo del libro: ")
            libreria.cerca_libro(titolo)
        elif scelta == "4":
            titolo = input("Inserisci il titolo del libro: ")
            azione = input("Scegli un'azione (rimuovi, modifica, aggiungi): ")
            libreria.gestisci_libro(titolo, azione)
        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")
menu()
