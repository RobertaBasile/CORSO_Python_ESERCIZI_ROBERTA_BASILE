#scrivi un programma che chiede all'utente 
# di inserire un numero o una stringa scegliendo 
# prima quale.Il programma dovrebbe determinare 
# il numero è pari o dispari e stampare il risultato
#  e se deve ripetere o stampare e poi ripetere.
def pariodispari(number):
    if number % 2 == 0:
        return "pari"
    else:
        return "dispari"

def funz_principale():
    while True:
        scelta = input("Vuoi inserire un numero o una stringa? (numero/stringa): ").lower()
        
        if scelta == "numero":
            numero = int(input("Inserisci un numero: "))
            risultato = pariodispari(numero)
            print(f"Il numero {numero} è {risultato}.")
        elif scelta == "stringa":
            stringa = input("Inserisci una stringa: ")
            print(f"Hai inserito la stringa: {stringa}")
        else:
            print("Scelta non valida. Riprova.")
            continue
        
        ripetere = input("Vuoi ripetere? (sì/no): ").lower()
        if ripetere != "sì":
            break

# Avvia il programma
funz_principale()


