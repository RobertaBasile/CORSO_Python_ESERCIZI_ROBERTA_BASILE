class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
        print(f"Aggiunti {quantita} {prodotto.nome}(i) all'inventario.")
        
    def stampa_inventario(self):
        if self.inventario:
            print("Inventario della fabbrica:")
            for nome, quantita in self.inventario.items():
                print(f"{nome}: {quantita}")
        else:
            print("L'inventario è vuoto.")

def main():
    nome = input("Inserisci il nome del prodotto: ")
    prezzo_vendita = float(input("Inserisci il prezzo di vendita: "))
    costo_produzione = float(input("Inserisci il costo di produzione: "))
    
    prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
    risultato = prodotto.calcola_profitto()
    print(f"Il profitto per il prodotto {nome} è: {risultato}")
    
    fabbrica = Fabbrica()
    quantita = int(input("Inserisci la quantità del prodotto da aggiungere all'inventario: "))
    fabbrica.aggiungi_prodotto(prodotto, quantita)
    fabbrica.stampa_inventario()

# Avvia il programma
main()
