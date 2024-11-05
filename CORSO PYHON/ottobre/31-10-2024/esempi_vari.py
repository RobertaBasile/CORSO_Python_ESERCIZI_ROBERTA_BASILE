# lista = [1,2,3,4]

# for num in lista:
#     print(num)
# print("\n")

# i=0
# while i<len(lista):
#     print(lista[i])
#     i+=1
# --------------------------------------------------
# lista= [1,2,3,4,5]
# listapari=[]
# for num in lista:
#     if num%2==0:
#         listapari.append(num)
# print(listapari)
# listapari2=[num for num in lista if num%2 ==0]
# print(listapari2)
# ---------------------------------------------------
# tommaso ={"nome":"tommaso", 
#           "cognome":"muraca", 
#           "corsi":["python", "ml", "js"],
#           "altre info":{"ore":8, "giorni":1}}
# print(tommaso.get("via","nessuna via"))
# print(tommaso.setdefault("via","nessuna via"))
# tommaso["via"] = "via roma"
# print(tommaso)
# ----------------------------------------------------

# lista= [1,2,3,4,5]
# listapari=[num for num in lista if num%2 ==0]
# print(listapari)
# dizionario = {key:value for key, value in dict.items()}
# ------------------------------------------------------

# lista= [1,2,3,4,5]
# listapari=[num for num in lista if num%2 ==0]
# print(listapari)
# dict1= {"a":1, "b":2, "c":3}
# dizionario = {k:v*2 for k,v in dict1.items()}
# print(dizionario)
# ------------------------------------------------------
# print(listapari)
# dict1= {"a":1, "b":2, "c":3}
# def quadrato(val):
#     return val**2
# dizionario = {k:v*2 for k,v in dict1.items()}
# print(dizionario)-
# ------------------------------------------------------
# def funzione(**argomenti):
#     print(type(argomenti))
# funzione(num1=11,num2=2,num3=4)
# ------------------------------------------------------
# def funzione(**argomenti):
#     print(argomenti)
# funzione(num1=11,num2=2,num3=4)
# -------------------------------------------------------
# alunni={1:{"nome":"tommaso","voti":[10,7,4]}, 2:{"nome":"giovanni","voti":[10,7,4]}}
# -------------------------------------------------------
# def funzione(a,b):
# print (a+b)
# variabile =funzione(10,11)
# print(variabile)
# ----------------------------------------------------------
# def funzione(a,b):
#     somma=a+b
#     return somma
# variabile=funzione(10,11)
# print(funzione(variabile,10))
# -----------------------------------------------------------
# variabile1 = 10
# def funzione(a,b):
#     variabile1 =variabile1+10
    
# funzione(10,20)
# print(somma)
# ------------------------------------------------------------
# variabile1=10

# def funzione():
#     variabile1=11
    
# print(variabile1)
# funzione()
# print(variabile1)
# -------------------------------------------------------------
# variabile1=10

# def funzione():
#     global variabile1
#     variabile1=11
    
# print(variabile1)
# funzione()
# print(variabile1)
# ---------------------------------------------------------------
# variabile1 = 10
# def funzione():
#     global variabile1
#     variabile1 =variabile1+1
    
# print(variabile1)
# funzione()
# print(variabile1)
# funzione()
# print(variabile1)
# ---------------------------------------------------------------
# lista= [1,2,3,4,5]

# listaT =[]

# for num in lista:
#     listaT.append(triplica, (num))
    
# listaT = list(map(triplica, lista))


# print(listaT)
# ---------------------------------------------------------------
# def numero_p(n):
#     return n%2 ==0

# print(numero_p(5))
# ---------------------------------------------------------------
# lista= [1,2,3,4,5]

# def numero_p(n):
#     return n%2 ==0
# listaP= list(filter(numero_p, lista))
# print(listaP)