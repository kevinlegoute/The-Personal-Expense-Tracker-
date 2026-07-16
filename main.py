from interface_adapters.repo_memoire import RepoEnMemoire
from interface_adapters.repo_csv import RepoFichierCSV
from framework.console_app import ConsoleApp


def main():
    # ── Choisir l'implémentation du repository ──
    # repo = RepoEnMemoire()          # données perdues à la fermeture
    repo = RepoFichierCSV("depenses.csv")  # données persistées

    app = ConsoleApp(repo)
    app.demarrer()


if __name__ == "__main__":
    main()