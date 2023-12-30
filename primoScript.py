"""
Creare uno script di python che simuli il login di un casino
    - si chieda all'utente: nome, cognome, ed età
    - si verifichino il nome e il cognome siano più lunghi di un carattere e che l'età sia maggiore di 18 anni
    - se è tutto corretto stampare una stringa di conferma altrimenti comunicare l'errore all'utente
    - si consideri che l'utente fornirà sempre dati del tipo corretto

BONUS: stampare il resoconto dei dati assicurandosi che il nome e il cognome inizino con la maiuscola
"""

def casino():
    control = True # variabile di controllo
    nameControl = False # variabile di controllo per il nome
    surnameControl = False # variabile di controllo per il cognome
    ageControl = False # variabile di controllo per l'età
    # chiede l'input all'utente del nome
    while(not nameControl):
        nomeUtente = input("Inserire il proprio nome: ")
        if len(nomeUtente) <= 1:
            print("Nome non valido")
            nameControl = False
        else:
            nameControl = True
    # chiede l'input all'utente del cognome
    while (not surnameControl):
        cognomeUtente = input("Inserire il proprio cognome: ")
        if len(cognomeUtente) <= 1:
            print("Cognome non valido")
            surnameControl = False
        else:
            surnameControl = True
    # chiede l'input all'utente dell'età e lo trasforma in int
    while (not ageControl):
        etaUtente = int(input("Inserire la propria età: "))
        if etaUtente < 18:
            print("Eta minore di 18 anni non valida")
            ageControl = False
        else:
            ageControl = True
    # verifica che tutti i dati siano stati inseriti correttamente
    if control:
        print("\nTutti i dati inseriti sono corretti")
    else:
        print("\nDati inseriti non validi")

    # Stampa il resoconto dei dati nel modo corretto
    nomeUtente = nomeUtente.lower()
    nomeUtente = nomeUtente.capitalize()

    cognomeUtente = cognomeUtente.lower()
    cognomeUtente = cognomeUtente.capitalize()

    print("\nIl resoconto dei dati: ")
    print("Nome: " + nomeUtente)
    print("Cognome: " + cognomeUtente)
    print("Eta: " + str(etaUtente))

# chiama la funzione
casino()