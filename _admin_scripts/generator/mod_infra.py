# mod_infra.py

FILES = {
    # --- CONFIGURATION BASE ---
    "requirements.txt": "pytest\npytest-cov",
    
    # MODIFICATION ICI : On n'ignore PAS _admin_scripts car il doit partir sur Git.
    # On ignore juste le dossier generator (s'il est dedans) pour ne pas donner le corrigé/générateur aux étudiants ?
    # À vous de voir. Ici, j'ignore juste les caches et venv standard.
    ".gitignore": "venv/\n.venv/\n__pycache__/\n*.py[cod]\n.DS_Store\n.vscode/\n_admin_scripts/generator/\n",
    
    "src/__init__.py": "",
    "tests/__init__.py": "",
    
    # =========================================================================
    # WORKFLOWS GITHUB
    # =========================================================================

    # 1. CI TDD
    ".github/workflows/tests.yml": """name: CI TDD
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 2
    steps:
      - name: Récupération du code
        uses: actions/checkout@v3
      - name: Installation Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Installation des outils
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Lancement des tests
        run: |
          export PYTHONPATH=$PYTHONPATH:$(pwd)
          python -m pytest -rs -v --cov=src
""",

    # 2. ASSIGNATION
    ".github/workflows/assign.yml": """name: ChatOps Assignation
on:
  issue_comment:
    types: [created]

jobs:
  manage_assignment:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Assign
        if: contains(github.event.comment.body, '/assign')
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addAssignees({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              assignees: [context.payload.comment.user.login]
            })
      - name: Unassign
        if: contains(github.event.comment.body, '/unassign')
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.removeAssignees({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              assignees: [context.payload.comment.user.login]
            })
""",

    # 3. ADMIN - CREATION DES ISSUES
    ".github/workflows/admin_1_issues.yml": """name: 🪄 1. Admin - Créer Tâches (Auto)

on: workflow_dispatch

permissions:
  issues: write
  contents: read

jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: {python-version: '3.10'}
      - name: Lancement Script
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python _admin_scripts/create_issues.py
""",

    # 4. ADMIN - PROTECTION BRANCHE
    ".github/workflows/admin_2_protection.yml": """name: 🛡️ 2. Admin - Protéger (⚠️ SUPPRIMER LE RUN APRES)

on:
  workflow_dispatch:
    inputs:
      admin_token:
        description: 'Token Admin (PAT) - Obligatoire pour la sécurité'
        required: true
        type: string

jobs:
  protect-branch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: {python-version: '3.10'}
      - run: echo "::add-mask::${{ inputs.admin_token }}"
      - name: Lancement Script
        env:
          GH_TOKEN: ${{ inputs.admin_token }}
        run: python _admin_scripts/protect_branch.py
""",

    # --- MAIN.PY (VOTRE VERSION INITIALE) ---
    "main.py": """import sys
import os

sys.path.append(os.getcwd())
MODULES_CHARGES = False

try:
    from src import code_cesar, code_substitution, analyse_frequence, utilitaires
    MODULES_CHARGES = True
except ImportError as e:
    print(f"\\n⚠️  ATTENTION : Problème d'importation des modules 'src'.")
    print(f"   Détail : {e}")
except Exception as e:
    print(f"\\n⚠️  ERREUR CRITIQUE : {e}")

def afficher_menu():
    print("\\n" + "="*70)
    print("🕵️  PY-NIGMA - Outil de Cryptographie  🕵️")
    print("="*70)
    print("--- 🏛️  CODE CÉSAR ---")
    print("1. Chiffrer       : Décaler les lettres (A + 1 -> B)")
    print("2. Déchiffrer     : Retrouver le message original")
    print("\\n--- 🔀  SUBSTITUTION ---")
    print("3. Leet Speak     : Remplacer les lettres par des chiffres (E->3, A->4)")
    print("4. Miroir         : Inverser l'alphabet (A->Z, B->Y)")
    print("\\n--- 📊  ANALYSE ---")
    print("5. Fréquence      : Trouver la lettre qui apparait le plus souvent")
    print("6. Palindrome     : Vérifier si le mot se lit dans les deux sens")
    print("\\n--- 🛠️  UTILITAIRES ---")
    print("7. Générer MDP    : Créer un mot de passe fort et aléatoire")
    print("8. Masquer        : Cacher un secret avec des étoiles (****ok)")
    print("-" * 70)
    print("Q. Quitter")
    print("-" * 70)

def executer_fonction(func, *args):
    try:
        res = func(*args)
        if res is NotImplemented:
            print("❌ Fonction non implémentée (Retourne NotImplemented).")
        elif res is None:
            print("⚠️ La fonction a retourné None (Est-ce normal ?).")
        else:
            print(f"✅ RÉSULTAT : {res}")
    except AttributeError: print("⚠️ Fonction introuvable.")
    except Exception as e: print(f"⚠️ ERREUR D'EXÉCUTION : {e}")

def main():
    while True:
        afficher_menu()
        c = input("Votre choix > ").upper().strip()
        if c == "Q": break
        
        if not MODULES_CHARGES:
            print("❌ Erreur bloquante : Modules non chargés.")
            continue
        
        try:
            if c=="1": executer_fonction(code_cesar.chiffrer_cesar, input("Message : "), int(input("Décalage : ")))
            elif c=="2": executer_fonction(code_cesar.dechiffrer_cesar, input("Message chiffré : "), int(input("Décalage : ")))
            elif c=="3": executer_fonction(code_substitution.vers_leet_speak, input("Texte : "))
            elif c=="4": executer_fonction(code_substitution.code_miroir, input("Texte : "))
            elif c=="5": executer_fonction(analyse_frequence.obtenir_lettre_la_plus_frequente, input("Texte : "))
            elif c=="6": executer_fonction(analyse_frequence.est_palindrome, input("Mot : "))
            elif c=="7": executer_fonction(utilitaires.generer_mot_de_passe, int(input("Longueur : ")))
            elif c=="8": executer_fonction(utilitaires.masquer_texte, input("Secret : "))
            else: print("Choix inconnu.")
        except ValueError:
            print("⚠️ Erreur : Entrez un nombre valide.")

if __name__ == "__main__": main()
"""
}