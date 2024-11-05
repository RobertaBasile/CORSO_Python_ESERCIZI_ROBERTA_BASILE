parola = "ciao a tutti"
frequenza={}
for char in parola:
    frequenza[char]=frequenza.setdefault(char,0)+1
    #setdefault(char,0)+1 equivale ad if...else