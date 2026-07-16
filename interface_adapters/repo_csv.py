import csv
import os
from datetime import date
from domain.entities.depense import Depense
from domain.interfaces.i_depense_repository import IDepenseRepository


class RepoFichierCSV(IDepenseRepository):
    COLONNES = ["id", "montant", "categorie", "date_depense", "description"]

    def __init__(self, chemin: str = "depenses.csv"):
        self._chemin = chemin
        self._initialiser_fichier()

    def _initialiser_fichier(self) -> None:
        if not os.path.exists(self._chemin):
            with open(self._chemin, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.COLONNES)
                writer.writeheader()

    def _lire_toutes(self) -> list[Depense]:
        depenses = []
        with open(self._chemin, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                depenses.append(Depense(
                    id=row["id"],
                    montant=float(row["montant"]),
                    categorie=row["categorie"],
                    date_depense=date.fromisoformat(row["date_depense"]),
                    description=row["description"],
                ))
        return depenses

    def _ecrire_toutes(self, depenses: list[Depense]) -> None:
        with open(self._chemin, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.COLONNES)
            writer.writeheader()
            for d in depenses:
                writer.writerow({
                    "id": d.id,
                    "montant": d.montant,
                    "categorie": d.categorie,
                    "date_depense": d.date_depense.isoformat(),
                    "description": d.description,
                })

    def sauvegarder(self, depense: Depense) -> None:
        depenses = self._lire_toutes()
        depenses = [d for d in depenses if d.id != depense.id]
        depenses.append(depense)
        self._ecrire_toutes(depenses)

    def supprimer(self, id: str) -> None:
        depenses = self._lire_toutes()
        nouvelles = [d for d in depenses if d.id != id]
        if len(nouvelles) == len(depenses):
            raise KeyError(f"Aucune dépense trouvée avec l'id : {id}")
        self._ecrire_toutes(nouvelles)

    def lister(self) -> list[Depense]:
        return self._lire_toutes()

    def chercher_par_categorie(self, categorie: str) -> list[Depense]:
        return [
            d for d in self._lire_toutes()
            if d.categorie.lower() == categorie.lower()
        ]