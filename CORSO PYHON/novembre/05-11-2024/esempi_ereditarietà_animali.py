# Definizione delle Classi Base

# Questo è un esempio di ereditarietà singola
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
 def mostra_informazioni(self):
    print(f"Veicolo marca {self.marca}, modello {self.modello}")

class Quad(Veicolo):
    Pass
    
#-------------------------------------------------------------------
# Definizione delle Classi Base



# Iniziamo definendo due classi base, Veicolo e DotazioniSpeciali, che saranno
# poi ereditate da una sottoclasse.
class Veicolo:
 def __init__(self, marca, modello):
  self.marca = marca
  self.modello = modello

 def mostra_informazioni(self):
  print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
 def __init__(self, dotazioni):
  self.dotazioni = dotazioni

 def mostra_dotazioni(self):
  print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
  
#-------------------------------------------------------------------
# Ereditarietà Multipla

# Ora, creiamo una classe AutomobileSportiva che eredita sia da Veicolo che da
# DotazioniSpeciali, dimostrando l'ereditarietà multipla. 

# Useremo super() per chiamare i costruttori delle classi base e sovrascriveremo
# il metodo mostra_informazioni per aggiungere ulteriori dettagli specifici
# dell'AutomobileSportiva.

class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)  
        # Alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni()  
        # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()  
        # Possiamo chiamare metodi di entrambe le superclassi
    
#--------------------------------------------------------------------
# Utilizzo della Classe Derivata


# Creiamo un'istanza della classe AutomobileSportiva e utilizziamo i suoi metodi
# per mostrare le informazioni sull'auto, inclusi i dettagli ereditati e quelli
# specifici della sottoclasse.


auto_sportiva = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllo
trazione", "Airbag laterali"], 720)
auto_sportiva.mostra_informazioni()