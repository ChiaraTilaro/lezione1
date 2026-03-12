class Prodotto:
    aliquota_iva = 0.22 #variabile di classe: è la stessa per tutte le istanze che verranno create

    def __init__(self, name :str , price : float, quantity : int, supplier = None):
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore(self):
        return self._price*self.quantity

    def valore_lordo(self):
        netto = self.valore()
        lordo = netto*(1+self.aliquota_iva)
        return lordo

    # per fare un metodo di classe
    @classmethod
    def costruttore_con_quantità_1(cls , name: str, price: float , supplier: str):
        cls(name , price , 1 , supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    @property
    def price(self): #getter
        return self._price
    @price.setter
    def price(self , valore):
        if valore <0:
            raise ValueError("Attenzione, il prezzo non può essere negativo")
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi - a {self.price} $"

    def __repr__(self):
        return f"Prodotto(nome = {self.name} price = {self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other: "Prodotto"):
        return self.price < other.price

    def prezzo_finale(self):
        return self.price*(1+self.aliquota_iva)

class ProdottoScontato(Prodotto):
    def __init__(self, name :str , price : float, quantity : int, supplier: str, sconto_percento: float):
       #Prodotto.__init__() modo alternativo
        super().__init__(name, price , quantity , supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self):
        return self.valore_lordo()*(1- self.sconto_percento/100)

class Servizio(Prodotto):
    def __init__(self, name :str , tariffa_oraria : float, ore : int):
        super().__init__(name = name, price=tariffa_oraria, quantity=1, supplier=None)
        self.ore = ore

    def prezzo_finale(self):
        return self.price*self.ore

# definire una classe abbonamento che abbia come attributi: "nome , prezzo_mensile, mesi"
# Abbonamento dovrà avere un metodo per calcolare il prezzo finale ottenuto come prezzo_menisle*mesi
class Abbonamento:
    def __init__(self, nome: str , prezzo_mensile:float , mesi:int):
        self.name = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self):
        return self.prezzo_mensile*self.mesi

from typing import Protocol

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self):
        ... # equivalente a pass ma al contrario di pass si una quando non si deve scrivere del codice

from dataclasses import dataclass
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario : float

    def __hash__(self):
        return hash((self.name , self.prezzo_unitario))

    def __str__(self):
        return f"{self.name} - {self.prezzo_unitario}"


MAX_QUANTITA = 1000

def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome , prezzo , 1 , None)

def _test_modulo():
    print("Sto testando il modulo prodotti.py")
    myproduct1 = Prodotto(name="Laptop", price=1200, quantity=12, supplier="ABC")
    print(f"Nome prodotto: {myproduct1.name}- Prezzo: {myproduct1.price}")
    print(f"Il totale lordo di myproduct1 è: {myproduct1.valore_lordo()}") # uso un metodo di istanza

    p3 = Prodotto.costruttore_con_quantità_1("Auricolari" , 200 , "ABC") # modo per chiamare un metodo di classe

    print(f"Prezzo scontato di myproduct1{Prodotto.applica_sconto(myproduct1.price , 15)}") #modo per chiamare un metodo statico

    myproduct2 = Prodotto("Mouse" , 10 , 25 , "CDE")
    print(f"Nome prodotto: {myproduct2.name}- Prezzo: {myproduct2.price}")

    print(f"Valore lordo di prodotto1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24
    print(f"Valore lordo di prodotto1: {myproduct1.valore_lordo()}")

    print(myproduct1)

    p_a = Prodotto("Laptop", price=1200.0, quantity=12, supplier="ABC")
    p_b = Prodotto("Mouse", 10, 14 , "CDE")

    print(f"Myproduct1 == p_a {myproduct1 == p_a}") # va a chiamare il metodo __eq__ appena implementato, mi aspetto True
    print(f"p_a == p_b {p_a == p_b}") # mi aspetto false

    mylist = [p_a, p_b , myproduct1]

    for p in mylist:
        print(f"-{p}")

    my_product_scontato = ProdottoScontato(name="Auricolari" , price=320, quantity=1, supplier="ABC", sconto_percento=10)
    my_service = Servizio(name="Consulenza" , tariffa_oraria=100, ore=3)

    mylist.append(my_product_scontato)
    mylist.append(my_service)

    mylist.sort(reverse=True)

    for elem in mylist:
        print(elem.name,"->", elem.prezzo_finale())

    print("------------------------------------------------------")


    abb = Abbonamento("Software gestionale", 30.0 , 24)
    mylist.append(abb)
    for elem in mylist:
        print(elem.name,"->", elem.prezzo_finale())

    def calcola_totale(elementi):
        tot = 0
        for e in elementi:
            tot += e.prezzo_finale()
        return tot
    print(f"Il totale è: {calcola_totale(mylist)}")



    def calcola_totale(elementi: list[HaPrezzoFinale] ):
        return sum(e.prezzo_finale() for e in elementi)
    print(f"Il totale è: {calcola_totale(mylist)}")




if __name__ == "__main__":
    _test_modulo()
