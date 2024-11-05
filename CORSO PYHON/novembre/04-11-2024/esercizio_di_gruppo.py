 #ESERCIZIO
 

# Andare a svolger e in gruppo minimo 3: Andiamo a creare un 
# sistema a X fasi dove x è il numero dei partecipanti il cui 
# scopo e: loggare, controllare i dati, far eseguire un "Gioco 
# matematico a punteggio(numerico consiglio)" da cui creare un 
# classifica e un logout con possibilità di ripetizione
# """

# # Lista users (dizionario)

# # Classe Utente
# # User ->id (int), nome (string), password (string), punteggio (float)
# # id -> crescente, (Attributo di classe)
# """Esempio:
#     users = {
#         0:{
#             "nome": "",
#             "punteggio": 0.0
#         },
#         1:{
#             "nome": "",
#             "punteggio": 0.0
#         }
#     }
#     """

# #Metodi
# """
#     Menu inziale:
#         1: Registrazione -> nome, password
#         2: Login -> nome, password
#         3: Exit
    
#     Menu log.:
#         1: Classifica
#         2: Giocare
#         3: Exit
#     -----
#     -> Registrazione: 
#         - Aggiungere al dizionario e controlla se esiste -> se esiste ti da errore e va a login
#         Output: nome, password, id <-(tupla)
        
#     -> Login:
#         - Controlla se esiste ed entra -> in caso di caso di errore password o nome sbagliato
#         Output: result (boolean)
    
#     -> Classifica
#         - Stampa la classifica
        
    
#     -> Giocare:
#         - Va al gioco e rittorna un punteggi alla fine del gioco che va inserito nel dizionario all'utente che ha giocato
#         Input: None,
#         Output: Punteggio
        
        
        
#     Task:
#         Cosimo -> Login
#         Stefano -> Gioco
#         Roberta -> Registrazione
#         Daniele -> Classifica

#   #registrazione
# def registra_user(users):
#     nome = input("Inserisci il tuo nome: ")
#     password = input("Inserisci la tua password: ")

#     # Controlla se l'user è già registrato
# #     users.items() restituisce tutte le coppie (chiave, valore) del dizionario users.

# # Il ciclo for itera su ciascuna coppia, assegnando la chiave a id_utente e il valore a dati.

# # Può accedere agli ID user e ai dati associati (nome e password) all'interno del ciclo.
#     for id_user, dati in users.items():
#         if dati['nome'] == nome:
#             print("user già registrato.")
#             return

#     # Genera un nuovo ID user
#     id_user = len(users) + 1
#     users[id_user] = {'nome': nome, 'password': password}
#     print(f"Registrazione completata per {nome} con ID user {id_user}")

# def main():
#     users = {}

#     while True:
#         scegli = input("Inserisci 'registra' per registrarti o 'esci' per terminare: ").lower()
#         if scegli == 'registra':
#             registra_user(users)
#         elif scegli == 'esci':
#             break
#         else:
#             print("scelta non valido. Riprova.")

# # Avvia il programma
# main()
