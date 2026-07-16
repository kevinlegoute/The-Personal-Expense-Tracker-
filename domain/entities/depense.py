from dataclasses import dataclass, field
from datetime import date
import uuid


@dataclass
class Depense:
    montant: float
    categorie: str
    date_depense: date
    description: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()) [:8])

    def __post_init__(self):
        if self.montant <= 0:
            raise ValueError("Le montant doit être strictement positif.")
        if not self.categorie.strip():
            raise ValueError("La catégorie ne peut pas être vide.")
        if not isinstance(self.date_depense, date):
            raise TypeError("La date doit être un objet datetime.date.")