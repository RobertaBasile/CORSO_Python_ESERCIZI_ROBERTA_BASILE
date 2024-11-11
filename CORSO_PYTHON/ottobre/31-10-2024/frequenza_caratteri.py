# Chiedi all'utente di inserire una stringa
stringa = input("Inserisci una stringa: ")

# Calcola la frequenza dei caratteri
risultato = frequenza_caratteri(stringa)

# Stampa il risultato
print("Frequenza di comparsa dei caratteri:", risultato)

def frequenza_caratteri(stringa):
    #creo dizionario frequenza vuoto
    frequenza = {}
    for carattere in stringa:
        if carattere in frequenza:
            frequenza[carattere] += 1
        else:
            frequenza[carattere] = 1
    return frequenza