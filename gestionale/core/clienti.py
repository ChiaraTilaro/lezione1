# Scrivbere una classe cliente cjhe abbia i campi nome, email, categoria(Gold, Silver, Bronza)
# Vorremmo che questa classe avesse un metodo che chiamiamo descrizione che deve restituire una stringa
# formattata ad esempio: "Cliente Fulvio Bianchi (Gold) - fulvio@google.com
from dataclasses import dataclass

# si modifichi la classe cliente in maniera tale che la proprietà categoria sia "protetta"
# e accetti solo Gold, Silver e Bronze


categorie_valide = {"Gold" , "Silver" , "Bronze"}

class Cliente:
    def __init__(self, nome , email , categoria):
        self.nome = nome
        self.email = email
        self._categoria = None
        self.categoria = categoria




    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"


    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):

        if categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida")
            self._categoria = categoria

@dataclass
class ClienteRecord:
    nome: str
    email : str
    categoria : str

    def __str__(self):
        return f" Cliente {self.nome} -- {self.email} ({self.categoria})"


def _test_modulo():
    c1 = Cliente("Mario Bianchi" , "mario.bianchi@polito.it" , "Gold")
    #c1 = Cliente("Carlo Masone" , "carlo.masone@polito.it" , "Platinum")
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()
