# Crea una classe chiamata Punto. Questa classe dovrebbe avere:

# Due attributi: x e y, per rappresentare le coordinate del punto nel piano.

# Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
# coordinate del punto di questi valori.

# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
# piano.

""" import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)

# inserire le coordinate
x = float(input("Inserisci la coordinata x: "))
y = float(input("Inserisci la coordinata y: "))

# Crea un'istanza della classe Punto con le coordinate inserite
punto = Punto(x, y)
print(f"Coordinate iniziali: ({punto.x}, {punto.y})")

# Esempio di utilizzo del metodo muovi
dx = float(input("Inserisci il valore per dx: "))
dy = float(input("Inserisci il valore per dy: "))
punto.muovi(dx, dy)
print(f"Coordinate dopo lo spostamento: ({punto.x}, {punto.y})")

# Calcola e stampa la distanza dall'origine
distanza = punto.distanza_da_origine()
print(f"Distanza dall'origine: {distanza}")
 """
 
