# Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

# Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. 
# Se l'utente inserisce un numero negativo o zero, 
# il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
# Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
# Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
# Utilizzare una struttura if per determinare se n è un numero primo. 
# Un numero primo è divisibile solo per 1 e per se stesso. 
# Il programma deve stampare se n è primo o n
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Chiedi all'utente di inserire un numero intero positivo
    n = int(input("Inserisci un numero intero positivo: "))
    
    # Utilizza un ciclo while per garantire che l'utente inserisca un numero positivo
    while n <= 0:
        print("Il numero deve essere positivo.")
        n = int(input("Inserisci un numero intero positivo: "))
    
    # Utilizza un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n
    somma_pari = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            somma_pari += i
    print(f"La somma dei numeri pari da 1 a {n} è: {somma_pari}")
    
    # Utilizza un ciclo for per stampare tutti i numeri dispari da 1 a n
    print(f"I numeri dispari da 1 a {n} sono:")
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()
    
    # Utilizza una struttura if per determinare se n è un numero primo
    if is_prime(n):
        print(f"{n} è un numero primo.")
    else:
        print(f"{n} non è un numero primo.")

# Avvia il programma
main()
