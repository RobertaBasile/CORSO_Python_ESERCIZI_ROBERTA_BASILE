# #puoi creare una lista assegnando 
# # un insieme di valori separati da virgole
# #  a una variabile. Ad esempio:
# numeri = [1, 2, 3, 4, 5]
# nomi = ["Alice", "Bob", "Charlie"]
# misto = [1, "due", True, 4.5]
# # 

# numeri = [1, 2, 3, 4, 5]
# print(numeri[0])
# print(numeri[2])
#---------------------------------------------------------------------------
numeri = [3, 1, 4, 2, 5, 4]
print("metodo pop")
numeri.pop()
print(numeri)
print("metodo count")
numero_di_4 = numeri.count(4)
print(numero_di_4)
#---------------------------------------------------------------------------
print("metodo remove")
numeri.remove(3)
print(numeri)

