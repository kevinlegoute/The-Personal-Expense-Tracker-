from abc import ABC, abstractmethod
from domain.entities.depense import Depense


class IDepenseRepository(ABC):

    @abstractmethod
    def sauvegarder(self, depense: Depense) -> None:
        pass

    @abstractmethod
    def supprimer(self, id: str) -> None:
        pass

    @abstractmethod
    def lister(self) -> list[Depense]:
        pass

    @abstractmethod
    def chercher_par_categorie(self, categorie: str) -> list[Depense]:
        pass