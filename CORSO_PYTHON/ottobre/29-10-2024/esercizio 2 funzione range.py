from sympy import isprime

controllo = True
numeri_primi=[]

while controllo!= False:
    number1 = int(input("inserire un numero"))
    number2 = int(input("inserire un numero"))

    interval = [*range(number1 + number2 + 1)]
    for i in interval:
        if (isprime(i)):
            numeri_primi.append(i)
            print(i)
    question = input("vuoi ripetere? ")
    if question== "no":
        controllo = False

