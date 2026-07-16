from domain.interfaces.i_depense_repository import IDepenseRepository


class SupprimerDepense:
    def __init__(self, repo: IDepenseRepository):
        self._repo = repo

    def executer(self, id: str) -> None:
        self._repo.supprimer(id)