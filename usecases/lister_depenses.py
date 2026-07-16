from domain.interfaces.i_depense_repository import IDepenseRepository
from domain.entities.depense import Depense


class ListerDepenses:
    def __init__(self, repo: IDepenseRepository):
        self._repo = repo

    def executer(self) -> list[Depense]:
        return self._repo.lister()