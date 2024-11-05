# Chiedi all'utente di inserire un numero. Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, 
# stampando ogni numero. e chiederti se vuoi ripetere o no Chiedi all'utente di inserire un numero.

# Il programma dovrebbe controllare se il numero inserito è primo o no.
# Se è primo, lo salva e stampa "Il numero è primo". 
# Altrimenti, stampa "Il numero non è primo". si ferma il tutto quando ha 5 numeri primi

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def countdown():
    prime_numbers = []
    while len(prime_numbers) < 5:
        number = int(input("Inserisci un numero: "))
        
        # Conto alla rovescia
        for i in range(number, -1, -1):
            print(i)
        
        # Controllo se il numero è primo, se sì, lo aggiunge alla lista
        if is_prime(number):
            prime_numbers.append(number)
            print("Il numero è primo.")
        else:
            print("Il numero non è primo.")
        
        # Chiedi se l'utente vuole ripetere
      
        repeat = input("Vuoi ripetere? (sì/no): ").lower()
        if repeat != 'sì':
            break
    
    print("siamo arrivati a 5 numeri primi", prime_numbers)

# Avvia il programma
countdown()
