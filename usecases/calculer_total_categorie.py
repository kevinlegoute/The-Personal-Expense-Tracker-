from domain.interfaces.i_depense_repository import IDepenseRepository


class CalculerTotalCategorie:
    def __init__(self, repo: IDepenseRepository):
        self._repo = repo

    def executer(self, categorie: str) -> float:
        depenses = self._repo.chercher_par_categorie(categorie)
        return sum(d.montant for d in depenses)