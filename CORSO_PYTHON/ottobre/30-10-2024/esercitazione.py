# # Esercitazione 
# # Esercizio 1 (Facile): Scrivi una funzione chiamata area_triangolo che prenda in 
# # input 1a base e I' altezza di un triangolo e restituisca 1a sua area. fare 1a 
# # stessa cosa con quadrato e rettagolo e rendere ripetibile salvando in una lista 
# # tutti i risultati 
# #----------------------------------------------------------------------------------------------------------
# # Esercizio 2 (Facile): Crea uno script che chiede nome e nun numero poi una chiama 1a 
# # funzione primo_o_no che determini se un numero dato è primo o no. La funzione dovrebbe 
# # restituire True se il numero è primo, e False altrimenti a quel punto se è primo lo salva 
# # e continua il ciclo altrimenti ti dice quante volte sta non divisore più piccolo 
# #----------------------------------------------------------------------------------------------------------
# # Esercizio 3 (Difficile): Sviluppa una funzione chiamata comprimi_stringa che prenda in 
# # input una stringa e restituisca una versione "compressa" di essa. La compressione dovrebbe 
# # funzionare in questo modo: per ogni gruppo consecutivo di caratteri identici nella 
# # stringa, La funzione dovrebbe aggiungere il carattere seguito dal numero di volte che 
# # appare consecutivamente . 
# # Per esempio, 1a stringa "aaabbc" dovrebbe diventare "aSb2c1". Se la "compressione" non 
# # riduce 'La lunghezza della stringa, funzione dovrebbe restituire 1a 
# # stringa originale. 
# #----------------------------------------------------------------------------
# #esercizio 1
# #----------------------------------------------------------------------------
# # Lista per salvare i risultati
# risultati = []

# # Decoratore per salvare i risultati
# def salva_risultato(func):
#     def wrapper(*args, **kwargs):
#         risultato = func(*args, **kwargs)
#         risultati.append(risultato)
#         return risultato
#     return wrapper

# @salva_risultato
# def area_triangolo(base, altezza):
#     return (base * altezza) / 2

# @salva_risultato
# def area_quadrato(lato):
#     return lato * lato

# @salva_risultato
# def area_rettangolo(base, altezza):
#     return base * altezza

# def main():
#     while True:
#         print("Scegli una figura geometrica:")
#         print("1. Triangolo")
#         print("2. Quadrato")
#         print("3. Rettangolo")
#         scelta = input("Inserisci il numero della tua scelta: ")

#         if scelta == "1":
#             base = float(input("Inserisci la base del triangolo: "))
#             altezza = float(input("Inserisci l'altezza del triangolo: "))
#             area = area_triangolo(base, altezza)
#             print(f"L'area del triangolo è: {area}")
#         elif scelta == "2":
#             lato = float(input("Inserisci il lato del quadrato: "))
#             area = area_quadrato(lato)
#             print(f"L'area del quadrato è: {area}")
#         elif scelta == "3":
#             base = float(input("Inserisci la base del rettangolo: "))
#             altezza = float(input("Inserisci l'altezza del rettangolo: "))
#             area = area_rettangolo(base, altezza)
#             print(f"L'area del rettangolo è: {area}")
#         else:
#             print("Scelta non valida. Riprova.")

#         ripetere = input("Vuoi calcolare un'altra area? (sì/no): ").strip().lower()
#         if ripetere != "sì":
#             break

#     print("Risultati delle aree calcolate:", risultati)


# # Avvia il programma
# main()
# #----------------------------------------------------------------------------
# #esercizio 2
# #----------------------------------------------------------------------------
# # Lista per salvare i numeri primi
# numeri_primi = []

# # Decoratore per salvare i numeri primi
# def salva_primo(func):
#     def wrapper(n):
#         risultato = func(n)
#         if risultato is True:
#             numeri_primi.append(n)
#         return risultato
#     return wrapper

# @salva_primo
# def primo_o_no(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return i  # Restituisce il più piccolo divisore non banale
#     return True

# def main():
#     nome = input("Inserisci il tuo nome: ")

#     while True:
#         numero = int(input(f"{nome}, inserisci un numero: "))

#         risultato = primo_o_no(numero)
#         if risultato is True:
#             print(f"{numero} è un numero primo.")
#         else:
#             print(f"{numero} non è un numero primo. Il più piccolo divisore non banale è {risultato}.")

#         ripetere = input("Vuoi inserire un altro numero? (sì/no): ").strip().lower()
#         if ripetere != "sì":
#             break

#     print(f"Numeri primi trovati: {numeri_primi}")

# # Avvia il programma
# main()
#esercizio3 
# Definizione del decoratore e della funzione
def compress_decorator(func):
    def wrapper(string):
        compressed = func(string)
        return compressed if len(compressed) < len(string) else string
    return wrapper

@compress_decorator
def comprimi_stringa(string):
    if not string:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed.append(f"{string[i - 1]}{count}")
            count = 1
    
    compressed.append(f"{string[-1]}{count}")
    
    return ''.join(compressed)

# Esempio di utilizzo con una stringa di input
input_string = input("inserisci stringa ")
output_string = comprimi_stringa(input_string)
print(output_string)  # Output: "a3b2c1"


