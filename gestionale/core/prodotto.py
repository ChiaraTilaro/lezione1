from dataclasses import dataclass


@dataclass
class ProdottoRecord:
    nome: str
    prezzo_unitario : float

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        self.nome == other.nome

    def __str__(self):
        return f"{self.name} - {self.prezzo_unitario}"
