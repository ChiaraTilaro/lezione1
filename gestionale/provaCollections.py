import copy
from collections import Counter, deque

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop" , 1200.0)
p2 = ProdottoRecord("Mouse" , 20.0)
p3 = ProdottoRecord("Auricolari" , 250.0)

# LISTE
carrello = [p1 , p2 , p3 , ProdottoRecord("Tablet" , 700.0)]

# aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor" , 150.0))

carrello.sort(key=lambda x: x.prezzo_unitario , reverse=True)

print("Prodotti nel carrello")
for i, p in enumerate(carrello):
    print(f"{i} {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

# aggiungere
carrello.append(ProdottoRecord("Prodpo" , 100.0)) # aggiunge in coda alla lista
carrello.extend([ProdottoRecord("aaaa" , 100.0) , ProdottoRecord("bbbb" , 100.0)])
carrello.insert(2 , ProdottoRecord("ccc" , 100.0)) # aggiunge nella posizione indicata dall'indice

# rimuovere
carrello.pop() # rimuove l'ultimo elemento
carrello.pop(2) # rimuove l'elemento in posizione 2
carrello.remove(p1) # elimina dalla lista la prima corrispondenza che trova
# carrello.clear() # elimina tutto

# sorting
# carrello.sort() # oridna seguendo l'oridnamento naturale, non funziona se gli oggetti contenuti non definiscono un metodo __lt::
# carrello.sort(reverse=True) # ordina al contrario
#carrello.sort(key=function)
#carrello_Ordinato = sorted(carrello) # crea una nuova lista ordinata

# copie ed altro
carrello.reverse() # restituisce la lista dall'ultimo al primo elemento
carrello_copia = carrello.copy() # shallow copy
carrello_copia2 = copy.deepcopy(carrello) # deep copy: copio anche il contenuto

# TUPLE
sede_principale = (45 , 8) # latitudine e langitudine della sede di Torino
sede_Milano = (45 , 9)

print(f"Sede principale lat: {sede_principale[0]}, Long: {sede_principale[1]}")

AliquoteIVA = (
    ("Standard" , 0.22),
    ("Ridotta" , 0.10) ,
    ("Alimentari" , 0.04),
    ("Esente" , 0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}")

def calcola_statistiche_carrello(carrello):
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi) , sum(prezzi)/len(prezzi) , max(prezzi) , min(prezzi))

tot , media , massimo , minimo= calcola_statistiche_carrello(carrello)

tot , *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

# SET
categorie = {"Gold" , "Silver" , "Bronze" , "Gold"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum" , "Elite" , "Gold"}
# categorie_all = categorie.union(categorie2)
categorie_all = categorie | categorie2 # unione
print(categorie_all)

categorie_comuni = categorie & categorie2 # solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 # solo gli elementi presenti in categorie ma non in categorie 2
print(categorie_esclusive)

categorie_esclusive_simmetrica = categorie ^ categorie2 # differenza simmetrica
print(categorie_esclusive_simmetrica)

prodotti_ordine_A = {ProdottoRecord("Laptop" , 1200.0) ,
                     ProdottoRecord("Mouse" , 20.0),
                     ProdottoRecord("Tablet" , 700.0)}

prodotti_ordine_B = {ProdottoRecord("Laptop2" , 1200.0) ,
                     ProdottoRecord("Mouse2" , 20.0),
                     ProdottoRecord("Tablet2" , 700.0)}

# metodi utili per i set
s = set()
s1 = set()

# aggiungere
s.add(ProdottoRecord("aaaa" , 20.0)) # aggiunge un elemento
s.update({ProdottoRecord("aaa" , 20.0) , ProdottoRecord("bbb" , 20.0)}) # aggiunge più elementi

# rimuovere
#s.remove() # rimuove un elemento. restituisce keyerrore se non esiste
#s.discard() # rimuove un elemento senza arrabbiarsi se questo non esiste
#s.pop() # rimuove e restituisce un elemento
# s.clear()

# operazioni insiemistiche
s.union(s1) # s| s1
s.intersection(s1) # s & s1
s.difference(s1) # s- s1
s.symmetric_difference(s1) # s^ s1

s1.issubset(s) # se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi

# DICTIONARY
catalogo = {
    "LAP001" : ProdottoRecord("Laptop" , 1200.0) ,
    "LAP002" : ProdottoRecord("Laptop Pro" , 2300.0) ,
    "MAUOO1" : ProdottoRecord("Mouse" , 20.0) ,
    "AUR001" : ProdottoRecord("Auricolari" , 250.0)
}

cod = "LAP002"
prod = catalogo[cod]
print(f"Il prodotto con codice {cod} è {prod}")

prod1 = catalogo.get("NonEsiste")
if prod1 is None:
    print(f"Prodotto non trovato")

prod2 = catalogo.get("NonEsiste2" , ProdottoRecord("Sconosciuto" , 0))
print(prod2)

# ciclare su un dizionario
keys = list(catalogo.keys())
values = list(catalogo.values())

for k in keys:
    print(k)

for v in values:
    print(v)

for key, val in catalogo.items():
    print(f"Cod {key} è associata a {val}")

# rimuovere dal dizionario
rimosso = catalogo.pop("LAP002")
print(rimosso)

# dict comprehension
prezzi = {
    codice: prod.prezzo_unitario for codice , prod in catalogo.items()
}

# da ricordare per dict
# d[key] = v scrivo sul dizionario
# v = d[key] leggere , se non eisste key error
# v = d.get(key , default)  legge senza rischiare keyerror, se non esiste prende default
# d.pop(key) restituisce un valore e lo cancella dal dizionario
# d.clear() elimina tutto
# d.keys() restituisce tutte le chiavi definite nel diz
# d.values() restituisce tutti i valori salvati nel diz
# d.items() restituisce le coppie
# key un d condizione chye verifica se key è presente nel diz

"""Esercizio live
per ciascuno dei seguenti casi decidere quale struttura usare:"""

"""1) Memorizzare un elencoa di ordini che dovranno essere processati in ordine di arrivo"""
# LISTA
ordini_da_processare = []
o1 = Ordine([] , ClienteRecord("Mario Rossi" , "mario@polito.it" , "Gold"))
o2 = Ordine([] , ClienteRecord("Mario Bianchi" , "bianchi@polito.it" , "Silver"))
o3 = Ordine([] , ClienteRecord("Fulvio Rossi" , "fulvio@polito.it" , "Bronze"))
o4 = Ordine([] , ClienteRecord("Carlo Masone" , "carlo@polito.it" , "Gold"))

ordini_da_processare.append((o1 , 0))
ordini_da_processare.append((o2 , 10))
ordini_da_processare.append((o3 , 3))
ordini_da_processare.append((o4 , 45))

"""2) Memorizzare i codici fiscali del cliente (univoco)"""
#SET
codici_fiscali = {
    "ajdndndjnd231" , "mfjfiifni456" , " nksoejen678"
}

"""3) Creare un db di prodotti che posso cercare con un codice univoco"""
# DIZIONARIO
listino_prodotti = {
     "LAP001" : ProdottoRecord("Laptop" , 1200.0) ,
     "KEY001" : ProdottoRecord("Keyboard" , 2300.0)
}

"""4) Memorizzare le cooridnate gps della nuova sede di Roma"""
# TUPLA
magazzino_Roma = (45 , 6)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un oridne in un certo range temporale"""
# SET
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("================================================================================")

# COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi" , "mario@polito.it" , "Gold"),
    ClienteRecord("Mario Bianchi" , "bianchi@polito.it" , "Silver"),
    ClienteRecord("Fulvio Rossi" , "fulvio@polito.it" , "Bronze"),
    ClienteRecord("Carlo Masone" , "carlo@polito.it" , "Gold"),
    ClienteRecord("Mario Rossi" , "mario@polito.it" , "Gold"),
    ClienteRecord("Giuseppe Averta" , "bianchi@polito.it" , "Silver"),
    ClienteRecord("Francesca Pistilli" , "fulvio@polito.it" , "Bronze"),
    ClienteRecord("Carlo Masone" , "carlo@polito.it" , "Gold"),
    ClienteRecord("Fulvio Corno" , "carlo@polito.it" , "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(f"{categorie_counter}")

print("Categoria più frequente")
print(f"{categorie_counter.most_common(1)}")

print(" 2 Categoria più frequenti")
print(f"{categorie_counter.most_common(2)}")

print("totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13 , "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3 , "Stampante": 1}
)

vendite_bimestre = vendite_febbraio+ vendite_gennaio

# aggregare informazione
print(f"Vendite gennaio: {vendite_gennaio}")
print(f"Vendite febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

# fare la differenza
print(f"Differenza di vendite: {vendite_gennaio-vendite_febbraio}")

# modificarne i valori in the fly
vendite_gennaio["Laptop"] += 4
print(vendite_gennaio)

# metodi da ricordare
# c.most_common(n) restituisce gli n elementi più frequenti
# c.total() somma dei conteggi

print("================================================================================")
print("Deque")
# Deque
coda_ordini = deque()

for i in range(1 , 10):
    cliente = ClienteRecord(f"Cliente{i}" , f"cliente{i}@polito.it" , f"Gold")
    prodotto = ProdottoRecord(f"Prodotto{i}" , 100.0*i)
    ordine = Ordine([RigaOrdine(prodotto , 1) ], cliente)
    coda_ordini.append(ordine)

print(f"Ordini in coda: {len(coda_ordini)}")

while coda_ordini:
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente : {ordine_corrente.cliente}")

print(f"Ho processato tutti gli ordini")
