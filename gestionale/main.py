# Scriviamo un codice python che modelli un semplice gestionale aziendale. Dovremo prevedere la possibilità
# di definire entità che modellano i prodotti, i clienti, offrire interfacce per calcolare i prezzi eventualmente
# scontati...
from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import ClienteRecord
import networkx as nx


p1 = Prodotto("Ebook Reader" , 120.0 , 1 , "AAA")
p2 = crea_prodotto_standard("Tablet" , 750.0)

print(p1)
print(p2)

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com" , "Gold")
p1 = ProdottoRecord("Laptop" , 1200.0)
p2 = ProdottoRecord("Mouse" , 20)
ordine = Ordine([RigaOrdine(p1 , 2) , RigaOrdine(p2 , 10)] , cliente1)
ordineScontato = OrdineConSconto([RigaOrdine(p1 , 2) , RigaOrdine(p2 , 10)] , cliente1 , 0.1)

print("------------------------------------------------------")
print(ordine)
print("Numero di righe nell'ordine:" , ordine.numero_righe())
print("Total netto:" , ordine.totale_netto())
print("Totale ordine (IVA 22%):" , ordine.totale_lordo(0.22))

print(ordineScontato)
print("Totale netto sconto:" , ordineScontato.totale_netto())
print("Totale lordo scontato" , ordineScontato.totale_lordo(0.22))


print("------------------------------------------------------")
# nel package gestionale, scriviamo un modulo fatture.py che contenga:
# una classe fattura che contiene un Ordine , un numero_fattura e una data
# un metodo genera_fattura() che restituisce una stringa formattata con tutte le info della fattura





