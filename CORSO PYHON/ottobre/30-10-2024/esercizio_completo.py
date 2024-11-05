# # # Esercizio su Python: Cicli e Condizioni
# # # Punto 1: Utilizzo di if
# # # Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari e "Dispari" se il numero è dispari.

# # # Punto 2: Utilizzo di while e range
# # # Scrivi un sistema che prende in input un numero intero positivo n 
# # e stampa tutti i numeri da n a 0 (compreso), decrementando di 
# # 1.Deve potersi ripete all’infinito

# # # Punto 3: Utilizzo di for
# # # Scrivi un sistema che prende in input una lista di numeri 
# # e stampa il quadrato di ciascun numero nella lista.

# # # Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in input una lista di numeri interi che precedente è stata valorizzata dall’utente.
# # # Il sistema deve:
# # # Utilizzare un ciclo for per trovare il numero massimo nella lista.
# # # Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
# # # Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, 
# # altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.
# # #parte 1
# def pariodispari(number):
#     if number % 2 == 0:
#         return "pari"
#     else:
#         return "dispari"

# def funz_principale():
#     while True:
         
#         numero = int(input("Inserisci un numero: "))
#         risultato = pariodispari(numero)
           
# # Avvia il programma
# funz_principale()

# # #parte 2
# def countdown():
    
#     while True:
#           number = int(input("Inserisci un numero: "))
        
#         #Conto alla rovescia
#           for i in range(number, -1, -1):
#               print(i)
#     countdown()
#  #parte 3
# # Funzione per calcolare il quadrato di ciascun numero nella lista
# def quadrati(lista):
#     for numero in lista:
#         print(numero ** 2)

# # Chiedi all'utente di inserire una lista di numeri separati da spazi
# input_utente = input("Inserisci una lista di numeri separati da spazi: ")

# # Converti l'input dell'utente in una lista di numeri
# lista_numeri = [int(x) for x in input_utente.split()]

# # Calcola e stampa il quadrato di ciascun numero nella lista
# quadrati(lista_numeri)
# #parte 4
# def main():
#     # Chiedi all'utente di inserire una lista di numeri separati da spazi
#     input_utente = input("Inserisci una lista di numeri interi separati da spazi: ")

#     # Converti l'input dell'utente in una lista di numeri
#     lista_numeri = [int(x) for x in input_utente.split()]

#     # Utilizza una condizione if per controllare se la lista è vuota
#     if not lista_numeri:
#         print("Lista Vuota")
#     else:
#         # Utilizza un ciclo for per trovare il numero massimo nella lista
#         numero_massimo = lista_numeri[0]
#         for numero in lista_numeri:
#             if numero > numero_massimo:
#                 numero_massimo = numero

#         # Utilizza un ciclo while per contare quanti numeri sono presenti nella lista
#         conteggio = 0
#         indice = 0
#         while indice < len(lista_numeri):
#             conteggio += 1
#             indice += 1

#         # Stampa il numero massimo trovato e il numero di elementi nella lista
#         print(f"Numero massimo: {numero_massimo}")
#         print(f"Numero di elementi nella lista: {conteggio}")

# # Avvia il programma
# main()
#parte 4 versione 2
def main():
    # Chiedi all'utente di inserire una lista di numeri interi e 
    # parole separati da spazi
    input_utente = input("Inserisci una lista di numeri interi e parole separati da spazi: ")

    # Converti l'input dell'utente in una lista di elementi
    lista_elementi = input_utente.split()

    # Utilizza una condizione if per controllare se la lista è vuota
    if not lista_elementi:
        print("Lista Vuota")
    else:
        # Inizializza variabili per il numero massimo e minimo e le parole con più e meno lettere
        numero_massimo = None
        numero_minimo = None
        parola_piu_lunga = ""
        parola_piu_corta = None

        # Utilizza un ciclo for per trovare il numero massimo e minimo e la parola con più e meno lettere
        for elemento in lista_elementi:
            if elemento.isdigit():
                numero = int(elemento)
                if numero_massimo is None or numero > numero_massimo:
                    numero_massimo = numero
                if numero_minimo is None or numero < numero_minimo:
                    numero_minimo = numero
            else:
                if len(elemento) > len(parola_piu_lunga):
                    parola_piu_lunga = elemento
                if parola_piu_corta is None or len(elemento) < len(parola_piu_corta):
                    parola_piu_corta = elemento

        # Utilizza un ciclo while per contare quanti numeri e parole sono presenti nella lista
        conteggio_numeri = 0
        conteggio_parole = 0
        indice = 0
        while indice < len(lista_elementi):
            if lista_elementi[indice].isdigit():
                conteggio_numeri += 1
            else:
                conteggio_parole += 1
            indice += 1

        # Stampa i risultati
        print(f"Numero massimo: {numero_massimo}")
        print(f"Numero minimo: {numero_minimo}")
        print(f"Parola con più lettere: {parola_piu_lunga}")
        print(f"Parola con meno lettere: {parola_piu_corta}")
        print(f"Numero di numeri nella lista: {conteggio_numeri}")
        print(f"Numero di parole nella lista: {conteggio_parole}")

# Avvia il programma
main()
