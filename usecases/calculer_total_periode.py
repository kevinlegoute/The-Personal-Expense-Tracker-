from domain.interfaces.i_depense_repository import IDepenseRepository
from datetime import date


class CalculerTotalPeriode:
    def __init__(self, repo: IDepenseRepository):
        self._repo = repo

    def executer(self, date_debut: date, date_fin: date) -> float:
        if date_debut > date_fin:
            raise ValueError("La date de début doit être antérieure à la date de fin.")
        depenses = self._repo.lister()
        return sum(
            d.montant for d in depenses
            if date_debut <= d.date_depense <= date_fin
        )