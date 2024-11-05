# Creare una classe base Animale e diverse classi derivate 
# che rappresentano diversi tipi di animali in uno zoo

def fai_suono(self):
    pass
class Zoo:
    def __init__(self):
        self.animali = []

    def aggiungi_animale(self, animale):
        self.animali.append(animale)
        print(f"{animale.nome} è stato aggiunto allo zoo.")

    def descrivi_animali(self):
        for animale in self.animali:
            print(animale.descrivi())
            print(f"suono: {animale.fai_suono()}")

class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        return f"{self.nome} ha {self.eta} anni."

class Leone(Animale):
    fai_suono()
class Scimmia(Animale):
    fai_suono()
class Zoo:
    def __init__(self):
        self.animali = []

    def aggiungi_animale(self, animale):
        self.animali.append(animale)
        print(f"{animale.nome} è stato aggiunto allo zoo.")

    def descrivi_animali(self):
        for animale in self.animali:
            print(animale.descrivi())
            print(f"Verso: {animale.fai_suono()}")

def main():
    zoo = Zoo()

    leone = Leone("Simba", 5)
   
    scimmia = Scimmia("George", 3)

    zoo.aggiungi_animale(leone)
   
    zoo.aggiungi_animale(scimmia)

    zoo.descrivi_animali()

# Avvia il programma
main()

