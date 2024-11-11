# creare una classe base Veicolo con attributi comuni a tutti i 
# veicoli e metodi per operazioni comuni come l'accensione e lo spegnimento.
# Derivando questa classe, creeranno specifiche classi per Auto, Furgone e Motocicletta, 
# aggiungendo caratteristiche uniche per ciascun tipo di veicolo. 
# Infine, dovranno implementare una classe GestoreParcoVeicoli per amministrare l'insieme dei veicoli.

# Classe Veicolo:
# Attributi privati:
# _marca (stringa)
# _modello (stringa)
# _anno (intero)
# _accensione (booleano)
# Metodi:
# accendi(): cambia lo stato di _accensione a vero.
# spegni(): cambia lo stato di _accensione a falso.
# Classi Derivate:
# Auto:
# Attributi aggiuntivi come _numero_porte
# Metodo specifico come suona_clacson()
# Furgone:
# Attributi per _capacità_carico
# Metodo per carica() e scarica()
# Motocicletta:
# Attributo per _tipo (e.g., sportiva, touring)
# Metodo per esegui_wheelie() se il tipo è sportivo
# Classe GestoreParcoVeicoli:
# Attributi:
# _veicoli: lista di tutti i veicoli.
# Metodi:
# aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
# rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
# lista_veicoli(): stampa un elenco di tutti i veicoli nel parco.


class Motocicletta(Veicolo):
    def __init__(self, tipo):
        
        self._tipo = tipo

    def esegui_wheelie(self):
        if self._tipo.lower() == "sportiva":
            print(f"{self._modello} sta eseguendo un wheelie!")
        else:
            print(f"{self._modello} non è adatta per un wheelie.")
    def metodo_specifico():
        pass 

class Barca(Veicolo):
    def __init__(self, tipo):
       
        self._tipo = tipo

    def accendi_motore(self):
        if self._tipo.lower() == "motore":
            print("Il motore è acceso.")
        else:
            print("è una barca a vela e non ha un motore da accendere.")
     def metodo_specifico():
        pass

