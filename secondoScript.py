y = (1,2,3,4,5,6,7,8,9)
x = [1,2,3,4,5,6,7,8,9]
z = {1,2,3,4,5,6,7,8,9}

print("Tupla: " + str(y))
print("Lista: " + str(x))
print("Lista: " + str(z))

print("Tipo della lista = " + str(type(x)))

for i in range(0, 10): # il 10 è escluso stampa da 0 a 9
    print(i)

# scrivere un programma che concateni due liste
listaUno = [3,6,7,3,2,5]
listaDue = [98,149,14,124,567]

print("Concatenazione di stringhe: " + str(listaUno) + str(listaDue))

# scrivere un programma che sommi due liste di eguali lunghezza
listaUno = [1,2,3,4,5]
listaDue = [6,7,8,9,10]

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