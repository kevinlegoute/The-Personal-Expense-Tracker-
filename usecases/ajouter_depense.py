from domain.entities.depense import Depense
from domain.interfaces.i_depense_repository import IDepenseRepository
from datetime import date


class AjouterDepense:
    def __init__(self, repo: IDepenseRepository):
        self._repo = repo

    def executer(self, montant: float, categorie: str,
                 date_depense: date, description: str = "") -> Depense:
        depense = Depense(
            montant=montant,
            categorie=categorie,
            date_depense=date_depense,
            description=description,
        )
        self._repo.sauvegarder(depense)
        return depense