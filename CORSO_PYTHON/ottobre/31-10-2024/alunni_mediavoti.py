def calcola_media(voti):
    return sum(voti) / len(voti)

def main():
    i=0
    alunni = {}
    numero_alunni = int(input("Inserisci n alunni: ").strip().lower())
    while i<numero_alunni:
        opzione = input("Inserisci 'alunno' per aggiungere un alunno, 'media' per calcolare le medie, o 'esci' per terminare: ").strip().lower()
        
        if opzione == 'alunno':
            nome = input("Inserisci il nome dell'alunno: ").strip()
            voti = input("Inserisci i voti dell'alunno separati da spazi: ").strip().split()
            voti = [float(voto) for voto in voti]
            alunni[nome] = voti
            i+=1
        elif opzione == 'media':
            for nome, voti in alunni.items():
                media = calcola_media(voti)
                print(f"Nome: {nome}, Media: {media}")
        elif opzione == 'esci':
            break
        else:
            print("opzione non valido. Riprova.")

# Avvia il programma
main()
