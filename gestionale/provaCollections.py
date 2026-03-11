import copy

from gestionale.core.prodotti import ProdottoRecord

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
