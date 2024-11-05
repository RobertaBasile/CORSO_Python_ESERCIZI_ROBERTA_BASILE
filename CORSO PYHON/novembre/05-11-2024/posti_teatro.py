# creare una classe base Posto che rappresenta un singolo posto nel teatro. Da questa, deriveranno
# diverse classi per tipi specifici di posti, come PostoVIP e PostoStandard. Sarà inoltre
# necessaria una classe Teatro per gestire tutti i posti e le prenotazioni.



# Classe Posto:
# Attributi privati:
# _numero (intero: numero del posto)
# _fila (stringa: fila in cui si trova il posto)
# _occupato (booleano: stato del posto, se è occupato o meno)
# Metodi:
# prenota(): prenota il posto se non è già occupato.
# libera(): libera il posto se è occupato.
# Getter per numero e fila, e uno stato che indica se il posto è occupato.
# Classi Derivate:
# PostoVIP:
# Aggiunge un attributo per servizi_extra (e.g., accesso al lounge, servizio in posto).
# Sovrascrive il metodo prenota() per includere la gestione dei servizi extra.
# PostoStandard:
# Potrebbe avere un costo aggiuntivo per la prenotazione online o altri servizi meno
# esclusivi.
# Classe Teatro:
# Attributi:
# _posti: lista di tutti i posti nel teatro.
# Metodi:
# prenota_posto(numero, fila): trova e prenota un posto specifico.
# stampa_posti_occupati(): mostra tutti i posti occupati.
class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già occupato.")
            
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} liberato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già libero.")
            
    #verranno create altre funzioni per Il momento ho iniziato a scrivere le principali, 
    # tutte verranno poi richiamate nel main()
    
    def main():
    teatro = Teatro()

    posto1 = PostoVIP(1, "A", "Accesso al lounge")
    posto2 = PostoStandard(2, "A", 5)
    posto3 = PostoStandard(3, "B", 3)

    teatro.aggiungi_posto(posto1)
    teatro.aggiungi_posto(posto2)
    teatro.aggiungi_posto(posto3)

    teatro.prenota_posto(1, "A")
    teatro.prenota_posto(2, "A")
    teatro.prenota_posto(3, "B")

    teatro.stampa_posti_occupati()

# Avvia il programma
main()