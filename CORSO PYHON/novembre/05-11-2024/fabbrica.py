class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
        print(f"Aggiunti {quantita} {prodotto.nome} all'inventario.")

    def stampa_inventario(self):
        if self.inventario:
            print("Inventario della fabbrica:")
            for nome, quantita in self.inventario.items():
                print(f"{nome}: {quantita}")
        else:
            print("L'inventario è vuoto.")
    # #@property trasforma il metodo titolare in un getter per l'attributo privato __titolare.
    # @property
    # def inventario(self):
    #     return self.__inventario

def main():
    nome = input("Inserisci il nome del prodotto: ")
    prezzo_vendita = float(input("Inserisci il prezzo di vendita: "))
    costo_produzione = float(input("Inserisci il costo di produzione: "))
    tipo = input("Inserisci il tipo di prodotto (Elettronica/Abbigliamento): ")

    if tipo.lower() == "elettronica":
        garanzia = int(input("Inserisci la durata in anni della garanzia: "))
        prodotto = Elettronica(nome, costo_produzione, prezzo_vendita, garanzia)
    elif tipo.lower() == "abbigliamento":
        materiale = input("Inserisci il materiale: ")
        prodotto = Abbigliamento(nome, costo_produzione, prezzo_vendita, materiale)
    else:
        print("Tipo di prodotto non valido.")
        return

    risultato = prodotto.calcola_profitto()
    print(f"Il profitto per il prodotto {nome} è: {risultato}")

    fabbrica = Fabbrica()
    quantita = int(input("Inserisci la quantità del prodotto da aggiungere all'inventario: "))
    fabbrica.aggiungi_prodotto(prodotto, quantita)
    fabbrica.stampa_inventario()

# Avvia il programma

main()

