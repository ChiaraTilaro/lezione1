# Scrivere un software gestionale che abbia le seguenti funzionalità:
# 1) supportare l'arrivo e la gestione di ordini
# 1bis) quando arriva un nuovo ordine lo aggiungo ad una coda, assicurandomi che sia eseguito solo dopo gli altri
# 2) avere delle funzionalità per avere statistiche sugli ordini
# 3) fornire statistiche sulla distribuzione di ordini per categoria di cliente
import random
from collections import deque, Counter, defaultdict

from dao import dao
from dao.dao import DAO
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:
    def __init__(self):
        self.ordini_da_processare = deque()
        self.ordini_processati = []
        self.statistiche_prodotti = Counter()
        self.ordini_per_categoria = defaultdict(list)
        self._dao = DAO()
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self):
        # leggo prodotti e clienti dal db e creo degli ordini randomici per testare la mia app
        self._allP.extend(self._dao.getAllProdotti())
        self._allC.extend(self._dao.getAllClienti())

        for i in range(10):
            indexP = random.randint(0 , len(self._allP)-1)
            indexC = random.randint(0 , len(self._allC)-1)
            ordine = Ordine(
                [RigaOrdine(self._allP[indexP] , random.randint(1 , 5))] , self._allC[indexC]
            )
            self.add_ordine(ordine)

    def add_ordine(self , ordine : Ordine):
        """Aggiunge un nuovo ordine agli elementi da gestire"""
        self.ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self.ordini_da_processare)}")


    def crea_ordine(self , nomeP, prezzoP , quantitaP , nomeC , mailC , categoriaC):

        prod = ProdottoRecord(nomeP , prezzoP)
        cliente = ClienteRecord(nomeC , mailC , categoriaC)

        self._update_DB(prod , cliente)
        return Ordine([RigaOrdine(prod , quantitaP)] ,
                      cliente)

    def _update_DB(self , prod , cliente):
        if not self._dao.hasProdotto(prod):
            self._dao.addProdotto(prod)

        if not self._dao.hasCliente(cliente):
            self._dao.addCliente(cliente)

    def processa_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""

        # Assicuriamoci che un ordine da processare esista
        if not self.ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False , Ordine([] , ClienteRecord("" , "" , ""))

        # se esiste, processiamo il primo in coda
        ordine = self.ordini_da_processare.popleft()
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        #Aggiornare statistiche sui prodotti venduti
        #Laptop- 10+1
        #Mouse- 5+2
        for riga in ordine.righe:
            self.statistiche_prodotti[riga.prodotto.nome] += riga.quantita

        # raggruppare gli ordini per categoria
        self.ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #Archiviamo l'ordine
        self.ordini_processati.append(ordine)

        print(f"Ordine correttamente processato")
        return True , ordine

    def processa_tutti_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda"""
        print(f"Processando tutti {len(self.ordini_da_processare)} ordini")
        ordini = []
        while self.ordini_da_processare:
            _ , ordine = self.processa_prossimo_ordine()
            ordini.append(ordine)
        print("Tutti gli ordini sono stati processati")
        return ordini


    def get_statistiche_prodotti(self , top_n: int = 5):
        """Questo metodo restituisce info su quante unità sono state vendute di un certo prodotto"""
        valori = []
        for prodotto, quantita in self.statistiche_prodotti.most_common(top_n):
            valori.append((prodotto , quantita))
        return valori

    def get_distribuzione_categorie(self):
        """Questo metodo restituisce info su totale fatturato per ogni categoria presente"""
        valori = []
        for cat in self.ordini_per_categoria.keys():
            ordini = self.ordini_per_categoria[cat]
            totale_fatturato = sum(o.totale_lordo(0.22) for o in ordini)
            valori.append((cat , totale_fatturato))
        return valori

    def get_riepilogo(self):
        """Restituisce una stringa con le info di massima"""
        sommario = ""
        sommario += "\n" + "="*60
        sommario += f" \nOrdini correttamente gestiti: {len(self.ordini_processati)}"
        sommario += f"\n Oridni in coda: {len(self.ordini_da_processare)}"

        sommario += "Prodotti più venduti:"
        for prod , quantita in self.get_statistiche_prodotti():
            sommario += f"\n {prod}: {quantita}"

        print("Fatturato per categoria:")
        for cat , fatturato in self.get_distribuzione_categorie():
            sommario += f"\n {cat}: {fatturato}"
        sommario += "\n" + "="*60
        return sommario



def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop" , 1200.0) , 1),
            RigaOrdine(ProdottoRecord("Mouse" , 10.0) , 3)
        ] , ClienteRecord("Mario Rossi" , "mario@mail.it" , "Gold")) ,
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop" , 1200.0) , 1),
            RigaOrdine(ProdottoRecord("Mouse" , 10.0) , 2),
            RigaOrdine(ProdottoRecord("Tablet" , 500.0) , 1),
            RigaOrdine(ProdottoRecord("Cuffie" , 250.0) , 3)
        ] , ClienteRecord("Fulvio Bianchi" , "binachi@gmail.com" , "Gold")) ,
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop" , 1200.0) , 2),
            RigaOrdine(ProdottoRecord("Mouse" , 10.0) , 2)
        ] , ClienteRecord("Giuseppe Averta" , "giuseppe.averta@polito.it" , "Silver")) ,
        Ordine([
            RigaOrdine(ProdottoRecord("Tbalet" , 900.0) , 1),
            RigaOrdine(ProdottoRecord("Cuffie" , 250.0) , 3)
        ] , ClienteRecord("Carlo Masone" , "carlo@mail.it" , "Gold")) ,
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop" , 1200.0) , 1),
            RigaOrdine(ProdottoRecord("Mouse" , 10.0) , 3)
        ] , ClienteRecord("Francesca Pistilli" , "francesca@gmail.com" , "Bronze"))
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()

    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()





