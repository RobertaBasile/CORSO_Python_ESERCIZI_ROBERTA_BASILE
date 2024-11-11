# In questo esempio ho inserrito anche in input altre informazioni:
# - Nome titolare
# - Numero CartaDiCredito
# - iban
# - email PayPal
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        raise NotImplementedError("Questo metodo deve essere implementato dalle sottoclassi")

class CartaDiCredito(MetodoPagamento):
    def __init__(self, numero_carta, titolare):
        self.__numero_carta = numero_carta
        self.__titolare = titolare

    @property
    def numero_carta(self):
        return self.__numero_carta

    @numero_carta.setter
    def numero_carta(self, numero_carta):
        self.__numero_carta = numero_carta

    @property
    def titolare(self):
        return self.__titolare

    @titolare.setter
    def titolare(self, titolare):
        self.__titolare = titolare

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito.")

class PayPal(MetodoPagamento):
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con PayPal.")

class BonificoBancario(MetodoPagamento):
    def __init__(self, iban, titolare):
        self.__iban = iban
        self.__titolare = titolare

    @property
    def iban(self):
        return self.__iban

    @iban.setter
    def iban(self, iban):
        self.__iban = iban

    @property
    def titolare(self):
        return self.__titolare

    @titolare.setter
    def titolare(self, titolare):
        self.__titolare = titolare

    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Bonifico Bancario.")

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento

    def paga(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

def main():
    importo = float(input("Inserisci l'importo da pagare: "))

    metodo = input("Scegli il metodo di pagamento (carta, paypal, bonifico): ").lower()
    
    if metodo == "carta":
        numero_carta = input("Inserisci il numero della carta: ")
        titolare = input("Inserisci il nome del titolare: ")
        metodo_pagamento = CartaDiCredito(numero_carta, titolare)
    elif metodo == "paypal":
        email = input("Inserisci l'email di PayPal: ")
        metodo_pagamento = PayPal(email)
    elif metodo == "bonifico":
        iban = input("Inserisci l'IBAN: ")
        titolare = input("Inserisci il nome del titolare: ")
        metodo_pagamento = BonificoBancario(iban, titolare)
    else:
        print("Metodo di pagamento non valido.")
        return

    gestore = GestorePagamenti(metodo_pagamento)
    gestore.paga(importo)

# Avvia il programma
main()
