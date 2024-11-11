# Andiamo a creare 3 input che riempiamo con booleano un numero intero 
# e una stringa li inseriamo in una lista e inseriamo la lista 
# come valore di un dizionario per chiave ‘tipididato’:

def main():
    # input booleano
    booleano = input("Inserisci un valore booleano (True/False): ").capitalize()
    if booleano == "True":
        booleano = True
    elif booleano == "False":
        booleano = False
    else:
        print("Valore booleano non valido. Impostato su False di default.")
        booleano = False

    # Chiedi all'utente di inserire un numero intero
    numero_intero = int(input("Inserisci un numero intero: "))

    # Chiedi all'utente di inserire una stringa
    stringa = input("Inserisci una stringa: ")

    # Crea una lista con i valori inseriti
    lista_valori = [booleano, numero_intero, stringa]

    # Crea un dizionario con la chiave 'tipididato' e la lista come valore
    dizionario = {'tipididato': lista_valori}

    # Stampa il dizionario
    print("Dizionario creato:", dizionario)

# Avvia il programma
main()
