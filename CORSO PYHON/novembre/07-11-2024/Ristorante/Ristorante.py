# Crea una classe ristorante con una lista di liste chiamata menu e una 
# lista chiamata ordinazione, 
# Nel menu ci devono essere X piatti composti ogniuno da una lista propria di ingredienti, 
# e la lista ordinazione invece e composta dalle singole ordinazioni del cleinte, 
# Servirà quindi una classe cliente 
# e ogni membro della cucina potrà servire solo un tipo di piatto

# EXTRA: aggiungi personale, budget e costi, Feedback piatti e chef

from PersonaleCucina import Chef, SousChef, CuocoLinea

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Ristorante:
    def __init__(self):
        self.menu = []
        self.ordinazione = []
        self.personale = []

    def aggiungi_piatto(self, nome_piatto, ingredienti):
        self.menu.append([nome_piatto, ingredienti])

    def mostra_menu(self):
        print("Menu del Ristorante:")
        for piatto in self.menu:
            print(f"{piatto[0]}: {', '.join(piatto[1])}")

    def prendi_ordinazione(self, cliente, nome_piatto):
        for piatto in self.menu:
            if piatto[0] == nome_piatto:
                for membro in self.personale:
                    if membro.tipo_piatto == nome_piatto:
                        self.ordinazione.append((cliente, nome_piatto))
                        print(f"Ordinazione aggiunta: {cliente.nome} ha ordinato {nome_piatto}")
                        return
                print(f"Nessun membro della cucina può servire il piatto: {nome_piatto}")
                return
        print(f"Piatto {nome_piatto} non trovato nel menu.")

    def mostra_ordinazioni(self):
        print("Ordinazioni attuali:")
        for ordine in self.ordinazione:
            print(f"{ordine[0].nome} ha ordinato {ordine[1]}")

    def aggiungi_personale(self, membro):
        self.personale.append(membro)

def main():
    chef = Chef("Chef Mario", 54, "cucina italiana", "Spaghetti alla Carbonara")
    sous_chef = SousChef
    

