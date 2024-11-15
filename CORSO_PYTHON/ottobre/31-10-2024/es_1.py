import random

def genera_stringa():
    return random.choice(["basso", "alto"])

anni = int(input("Inserisci la tua età: "))
patente = input("Hai la patente? (sì/no): ").strip().lower()
tasso_alcol = genera_stringa()

if anni < 18:
    print("Non puoi guidare")
elif patente != "sì" and tasso_alcol == "alto":
    print(f"Non puoi guidare, il tuo tasso alcolico è {tasso_alcol}")
elif anni >= 18 and patente == "sì" and tasso_alcol == "basso":
    print(f"Puoi guidare, il tuo tasso alcolico è {tasso_alcol}")
elif patente != "sì":
    print("Non puoi guidare")