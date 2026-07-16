from domain.entities.depense import Depense
from domain.interfaces.i_depense_repository import IDepenseRepository


class RepoEnMemoire(IDepenseRepository):
    def __init__(self):
        self._data: dict[str, Depense] = {}

    def sauvegarder(self, depense: Depense) -> None:
        self._data[depense.id] = depense

    def supprimer(self, id: str) -> None:
        if id not in self._data:
            raise KeyError(f"Aucune dépense trouvée avec l'id : {id}")
        del self._data[id]

    def lister(self) -> list[Depense]:
        return list(self._data.values())

    def chercher_par_categorie(self, categorie: str) -> list[Depense]:
        return [
            d for d in self._data.values()
            if d.categorie.lower() == categorie.lower()
        ]