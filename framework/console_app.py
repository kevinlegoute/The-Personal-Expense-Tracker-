from datetime import date
from domain.interfaces.i_depense_repository import IDepenseRepository
from usecases.ajouter_depense import AjouterDepense
from usecases.supprimer_depense import SupprimerDepense
from usecases.lister_depenses import ListerDepenses
from usecases.calculer_total_categorie import CalculerTotalCategorie
from usecases.calculer_total_periode import CalculerTotalPeriode


class ConsoleApp:
    def __init__(self, repo: IDepenseRepository):
        self._ajouter = AjouterDepense(repo)
        self._supprimer = SupprimerDepense(repo)
        self._lister = ListerDepenses(repo)
        self._total_cat = CalculerTotalCategorie(repo)
        self._total_periode = CalculerTotalPeriode(repo)

    def demarrer(self):
        print("\n╔══════════════════════════════════════╗")
        print("║     CARNET DE DÉPENSES PERSONNELLES  ║")
        print("╚══════════════════════════════════════╝")
        while True:
            self._afficher_menu()
            choix = input("Votre choix : ").strip()
            if choix == "1":
                self._handle_ajouter()
            elif choix == "2":
                self._handle_supprimer()
            elif choix == "3":
                self._handle_lister()
            elif choix == "4":
                self._handle_total_categorie()
            elif choix == "5":
                self._handle_total_periode()
            elif choix == "0":
                print("\n👋 Au revoir !\n")
                break
            else:
                print("⚠️  Choix invalide, veuillez réessayer.")

    def _afficher_menu(self):
        print("\n┌──────────────────────────────────────┐")
        print("│              MENU PRINCIPAL           │")
        print("├──────────────────────────────────────┤")
        print("│  1. Ajouter une dépense               │")
        print("│  2. Supprimer une dépense             │")
        print("│  3. Lister toutes les dépenses        │")
        print("│  4. Total par catégorie               │")
        print("│  5. Total par période                 │")
        print("│  0. Quitter                           │")
        print("└──────────────────────────────────────┘")

    # ─── Handlers ───────────────────────────────────

    def _handle_ajouter(self):
        print("\n── Ajouter une dépense ──")
        try:
            montant = float(input("Montant (ex: 15.50) : "))
            categorie = input("Catégorie (ex: Alimentation) : ").strip()
            date_str = input("Date (AAAA-MM-JJ) : ").strip()
            description = input("Description (optionnel) : ").strip()
            date_depense = date.fromisoformat(date_str)
            depense = self._ajouter.executer(
                montant=montant,
                categorie=categorie,
                date_depense=date_depense,
                description=description,
            )
            print(f"✅ Dépense ajoutée avec succès ! (id: {depense.id[:8]}...)")
        except ValueError as e:
            print(f"❌ Erreur : {e}")

    def _handle_supprimer(self):
        print("\n── Supprimer une dépense ──")
        self._handle_lister()
        id_complet = input("\nEntrez l'id complet de la dépense à supprimer : ").strip()
        try:
            self._supprimer.executer(id_complet)
            print("✅ Dépense supprimée avec succès !")
        except KeyError as e:
            print(f"❌ Erreur : {e}")

    def _handle_lister(self):
        print("\n── Liste des dépenses ──")
        depenses = self._lister.executer()
        if not depenses:
            print("  Aucune dépense enregistrée.")
            return
        print(f"\n  {'ID':<10} {'Montant':>10} {'Catégorie':<18} {'Date':<12} Description")
        print(f"  {'─'*10} {'─'*10} {'─'*18} {'─'*12} {'─'*20}")
        for d in depenses:
            print(
                f"  {d.id:<10} "
                f"{d.montant:>9.2f}HTG "
                f"{d.categorie:<18} "
                f"{d.date_depense.isoformat():<12} "
                f"{d.description}"
            )
        print(f"\n  Total général : {sum(d.montant for d in depenses):.2f}HTG")

    def _handle_total_categorie(self):
        print("\n── Total par catégorie ──")
        categorie = input("Catégorie : ").strip()
        try:
            total = self._total_cat.executer(categorie)
            print(f"💰 Total pour '{categorie}' : {total:.2f}HTG")
        except Exception as e:
            print(f"❌ Erreur : {e}")

    def _handle_total_periode(self):
        print("\n── Total par période ──")
        try:
            date_debut = date.fromisoformat(input("Date de début (AAAA-MM-JJ) : ").strip())
            date_fin = date.fromisoformat(input("Date de fin   (AAAA-MM-JJ) : ").strip())
            total = self._total_periode.executer(date_debut, date_fin)
            print(f"💰 Total du {date_debut} au {date_fin} : {total:.2f}HTG")
        except ValueError as e:
            print(f"❌ Erreur : {e}")