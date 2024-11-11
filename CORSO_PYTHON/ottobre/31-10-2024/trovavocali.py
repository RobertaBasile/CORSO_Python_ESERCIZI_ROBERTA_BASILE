def trova_vocali(parola):
    vocali = "aeiouAEIOU"
    for indice, carattere in enumerate(parola):
        if carattere in vocali:
            print(f"Vocale: {carattere}, Indice: {indice}")

# Chiedi all'utente di inserire una parola
parola = input("Inserisci una parola: ")

# Trova e stampa le vocali e i loro indici
trova_vocali(parola)
