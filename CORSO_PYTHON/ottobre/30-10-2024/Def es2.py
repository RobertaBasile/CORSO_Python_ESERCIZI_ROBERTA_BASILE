# Chiedi all'utente di inserire un numero N. il programma 
# dovrebbe stampare la sequenza di fibonacci fino a N. ad esempio , 
# se l'utente 
# inserisce 100 , il programma dovrebbe stampare tutti i numeri 
# della sequenza di fibonacci minori o uguali a 100

def fibonacci_fino_a_n(n):
    sequenza = [0, 1]
    while True:
        #sequenza[-1]: restituisce l'ultimo elemento della lista.
        #sequenza[-2]: Questo restituisce il penultimo elemento 
        # della lista.
        prossimo_numero = sequenza[-1] + sequenza[-2]
        if prossimo_numero > n:
            break
        sequenza.append(prossimo_numero)
    return sequenza

def main():
    n = int(input("Inserisci un numero intero positivo: "))
    while n <= 0:
        n = int(input("Il numero deve essere POSITIVO ed INTERO: "))
    sequenza_fibonacci = fibonacci_fino_a_n(n)
    print(f"La sequenza di Fibonacci fino a {n} è: {sequenza_fibonacci}")

# Avvia il programma
main()
