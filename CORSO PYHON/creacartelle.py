import os
import datetime

def crea_cartelle(percorso_base):
    # Ottieni la data di oggi
    oggi = datetime.date.today()
    
    # Trova il prossimo lunedì
    giorni_fino_a_lunedi = (7 - oggi.weekday()) % 7
    prossimo_lunedi = oggi + datetime.timedelta(days=giorni_fino_a_lunedi)
    
    # Data di fine (2 dicembre)
    data_fine = datetime.date(oggi.year, 12, 2)
    
    # Crea cartelle per ogni giorno esclusi sabati e domeniche
    data_corrente = prossimo_lunedi
    while data_corrente <= data_fine:
        if data_corrente.weekday() < 5:  # Esclude sabati (5) e domeniche (6)
            nome_cartella = data_corrente.strftime("%d-%m-%Y")
            percorso_completo = os.path.join(percorso_base, nome_cartella)
            os.makedirs(percorso_completo, exist_ok=True)
            print(f"Cartella creata: {percorso_completo}")
        data_corrente += datetime.timedelta(days=1)

# Specifica il percorso base dove vuoi salvare le cartelle
percorso_base = "C:/Users/ROBERTA/Desktop/CORSO PYHON"

# Esegui la funzione
crea_cartelle(percorso_base)
