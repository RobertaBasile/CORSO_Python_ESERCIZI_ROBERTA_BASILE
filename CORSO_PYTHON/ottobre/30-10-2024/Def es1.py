# Scrivi un programma che genera un numero casuale tra uno e 100 inclusi. 
# l'utente deve indovinare quale numero è stato generato. 
# Dopo ogni tentativo il programma dovrebbe dire all'utente se il numero 
# da indovinare è più alto o più basso rispetto al numero inserito . 
# il gioco termina quando 
# l'utente indovina il numero o decide di uscire.
import random

def gioco_indovina_numero():
    numero_casuale = random.randint(1, 100)
    print("Ho generato un numero tra 1 e 100. Prova a indovinarlo!")

    while True:
        tentativo = input("Inserisci il tuo tentativo (o digita 'esci' per terminare): ")
        
        if tentativo.lower() == 'esci':
            print("Hai deciso di terminare il gioco. Il numero era:", numero_casuale)
            break
        
        tentativo = int(tentativo)
        
        if tentativo < numero_casuale:
            print("Il numero da indovinare è più alto.")
        elif tentativo > numero_casuale:
            print("Il numero da indovinare è più basso.")
        else:
            print("Congratulazioni! Hai indovinato il numero:", numero_casuale)
            break

# Avvia il gioco
gioco_indovina_numero()
