from dataclasses import dataclass


@dataclass
class ClienteRecord:
    nome: str
    email : str
    categoria : str

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        self.email == other.email

    def __str__(self):
        return f" Cliente {self.nome} -- {self.email} ({self.categoria})"
