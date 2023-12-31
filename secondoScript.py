y = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("Tupla: " + str(y))
print("Lista: " + str(x))
print("Lista: " + str(z))

print("Tipo della lista = " + str(type(x)))

for i in range(0, 10):  # il 10 è escluso stampa da 0 a 9
    print(i)

# scrivere un programma che concateni due liste
listaUno = [3, 6, 7, 3, 2, 5]
listaDue = [98, 149, 14, 124, 567]

print("Concatenazione di stringhe: " + str(listaUno) + str(listaDue))

# scrivere un programma che sommi due liste di eguali lunghezza
listaUno = [1, 2, 3, 4, 5]
listaDue = [6, 7, 8, 9, 10]

# controlla se le due liste hanno effettivamente la stessa lunghezza
if len(listaUno) == len(listaDue):
    # inizializza una nuova lista
    listaSomma = []
    # per ogni elemento delle liste fa l'append sulla lista somma
    for i in range(len(listaUno)):
        listaSomma.append(listaUno[i] + listaDue[i])
    print("La lista somma è: " + str(listaSomma))
else:
    print("Non se po fa")

######### DIZIONARI #########

dizionarioUno = {
    "name": "Mattia",
    "age": 24,
    "city": "Macerata"
}

print(dizionarioUno["name"])
dizionarioUno["name"] = "Gianluca"
print(dizionarioUno["name"])

dizionarioUno["prova_aggiunta"] = "ciao"
print(dizionarioUno)
print(type(dizionarioUno))
print(len(dizionarioUno))
print(dizionarioUno.keys())
print(dizionarioUno.values())
print("Mattia" in dizionarioUno.keys())

for key, value in dizionarioUno.items():
    print(key, value)
    print(type(key))
    print(type(value))

"""
Compito 1. 
    Dichiarare due liste di numeri con cinque elementi ciascuna e 
    creare una lista concatenata che le includa entrambe
BONUS: Prendere gli elementi delle liste dall'utente chiedendole una per una 
"""

lista_uno = []
lista_due = []
lista_tot = []

# for i in range(5):
#     lista_uno.append(input("Inserisci il " + str((i + 1)) + " elemento della prima lista "))
#     lista_due.append(input("Inserisci il " + str((i + 1)) + " elemento della seconda lista "))
#
# lista_tot = lista_uno + lista_due
# print(lista_tot)

"""
Compito 2. 
    Dichiarare una lista e stamparne il reverse (senza usare altre variabili)
"""
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
aList.reverse()
print("Reverse list " + str(aList))

"""
Compito 3. 
    Modifichiamo l'esercizio del casinò in un registro degli utenti del suddetto. 
    Creare una interfaccia da terminale per aggiungere 10 utenti e salvare ciascuno 
    in un dizionario (e dunque in una lista che li contenga tutti). 
    Il programma deve rifiutare una inserzione se il nickname di uno degli utenti è già presente nel sistema.
    Finita l'inserzione, creare un modulo statistico che analizzi i dati inseriti nel sistema.
    In particolare si vuole sapere la percentuale di maschi e di femmine e la età massima, minima e media dei registrati.
    
    Struttura utente:
        - Nickname
        - Eta
        - Gender
        
    Si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione del problema, come ad esempio liste temporanee.
"""

# dizionario di esempio
dictionary = {
    "Nickname": [],
    "Eta": [],
    "Gender": []
}


# Ricerca lineare nel dizionario per Nome
def searchName(dic, nickname):
    for value in dic["Nickname"]:
        if value == nickname:
            return True
    return False


def inputDictionary():
    flag = True
    # input dell'utente
    for i in range(10):

        # poteva essere
        #   while nickname in dictionary["Nome"]
        #       input("Inserisci il nome ")

        # cicla finché l'utente non ha inserito un nome valido non già presente nel dizionario
        while flag:
            inputNickname = input("Inserisci il nickname ")
            # se il nome già esiste
            if searchName(dictionary, inputNickname):
                print("Nickname inserito già presente")
            else:
                flag = False
                dictionary["Nickname"].append(inputNickname)
        flag = True
        dictionary["Eta"].append(input("Inserisci l'età "))
        dictionary["Gender"].append(input("Inserisci il genere "))


# riscrivo il dictionary per non dovere inserire i valori ogni volta
diz = {
    "Nickname": ["Mattia", "Gianluca", "Marco", "Giovanni", "Gioele", "Francesca", "Maria", "Nastra", "Riccardo",
                 "Marcella"],
    "Eta": [12, 23, 45, 67, 25, 89, 56, 78, 90, 78],
    "Genere": ["M", "M", "M", "M", "M", "F", "F", "F", "M", "F"]
}
# percentuale di maschi e di femmine
numberOfPeople = len(diz["Nickname"])  # quante persone contiene il dizionario
maleCount = 0
femaleCount = 0
for gender in diz["Genere"]:
    if gender == "F":
        femaleCount += 1
    elif gender == "M":
        maleCount += 1

print("Percentuale di Femmine: " + str((femaleCount / numberOfPeople) * 100))
print("Percentuale di Maschi: " + str((maleCount / numberOfPeople) * 100))

# la età massima, minima e media dei registrati.
ageList = list(diz["Eta"])
ageList.sort()
print("Eta minima: " + str(ageList[0]))
print("Eta massima: " + str(ageList[-1]))
print("Eta media: " + str(sum(ageList) / numberOfPeople))
