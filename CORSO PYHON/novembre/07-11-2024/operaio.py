# Classe operaio con due figli

# avere 2 classi astratte come secondo genitore, 
# una per uno, dei figli di operaio

from abc import ABC, abstractmethod

# Classe base Operaio
class Operaio:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def lavora(self):
        print(f"{self.nome} sta lavorando.")

# Classe astratta Manutenzione
class Manutenzione(ABC):
    @abstractmethod
    def esegui_manutenzione(self):
        pass

# Classe astratta Produzione
class Produzione(ABC):
    @abstractmethod
    def esegui_produzione(self):
        pass

# Classe figlia OperaioManutenzione
class OperaioManutenzione(Operaio, Manutenzione):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def esegui_manutenzione(self):
        print(f"{self.nome} sta eseguendo la manutenzione.")

# Classe figlia OperaioProduzione
class OperaioProduzione(Operaio, Produzione):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def esegui_produzione(self):
        print(f"{self.nome} sta eseguendo la produzione.")

# Esempio di utilizzo
def main():
    # i numeri si riferiscono alla manutenzione
    operaio_manutenzione = OperaioManutenzione("Mario Rossi", 45)
    operaio_produzione = OperaioProduzione("Luigi Bianchi", 38)

    operaio_manutenzione.lavora()
    operaio_manutenzione.esegui_manutenzione()

    operaio_produzione.lavora()
    operaio_produzione.esegui_produzione()

# Avvia il programma
if __name__ == "__main__":
    main()

