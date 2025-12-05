# Pour lancer le générateur, le dossier complet _admin_scripts doit être présent
# et se trouver dans le dossier où on désire créer le projet.
# Exemple : /mon-projet/_admin_scripts/generator/GENERATEUR.py

import sys
import os
import shutil
import subprocess
import importlib.util
from pathlib import Path

# =============================================================================
# ⚙️ CONFIGURATION ET CHEMINS
# =============================================================================

SCRIPT_DIR = Path(__file__).resolve().parent           # _admin_scripts/generator
PROJECT_ROOT = SCRIPT_DIR.parent.parent                # Racine PYNIGMA
sys.path.append(str(SCRIPT_DIR))                       # Pour importer les modules mod_

# -----------------------------------------------------------------------------
# 📄 CONTENU DES FICHIERS STATIQUES
# -----------------------------------------------------------------------------
CONTENU_MAIN = r"""import sys
import os

# Ajout du dossier courant au path pour trouver le package 'src'
sys.path.append(os.getcwd())
MODULES_CHARGES = False

try:
    from src import code_cesar, code_substitution, analyse_frequence, utilitaires
    MODULES_CHARGES = True
except ImportError as e:
    print(f"\n⚠️  ATTENTION : Problème d'importation des modules 'src'.")
    print(f"   Détail : {e}")
except Exception as e:
    print(f"\n⚠️  ERREUR CRITIQUE : {e}")

def afficher_menu():
    print("\n" + "="*70)
    print("🕵️  PY-NIGMA - Outil de Cryptographie  🕵️")
    print("="*70)
    print("--- 🏛️  CODE CÉSAR ---")
    print("1. Chiffrer       : Décaler les lettres (A + 1 -> B)")
    print("2. Déchiffrer     : Retrouver le message original")
    print("\n--- 🔀  SUBSTITUTION ---")
    print("3. Leet Speak     : Remplacer les lettres par des chiffres (E->3, A->4)")
    print("4. Miroir         : Inverser l'alphabet (A->Z, B->Y)")
    print("\n--- 📊  ANALYSE ---")
    print("5. Fréquence      : Trouver la lettre qui apparait le plus souvent")
    print("6. Palindrome     : Vérifier si le mot se lit dans les deux sens")
    print("\n--- 🛠️  UTILITAIRES ---")
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

CONTENU_GITIGNORE = r"""
# Environnements Python
venv/
.venv/
# Fichiers compilés et cache
__pycache__/
*.py[cod]
.pytest_cache/
# Métadonnées et systèmes
.DS_Store
# Editeur (à ignorer si la config n'est pas partagée)
.vscode/
"""

# -----------------------------------------------------------------------------
# 🤖 CONTENU DES WORKFLOWS GITHUB
# -----------------------------------------------------------------------------
WORKFLOW_TESTS = r"""name: CI TDD
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
"""

# ICI : J'AI BIEN RENOMMÉ LA VARIABLE POUR QU'ELLE CORRESPONDE À SON UTILISATION
WORKFLOW_ADMIN_PROTECTION = r"""name: 🛡️ 2. Admin - Protéger (⚠️ SUPPRIMER LE RUN APRES)

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
        with:
          python-version: '3.10'

      - name: Masquer le token dans les logs
        run: echo "::add-mask::${{ inputs.admin_token }}"
      
      - name: Lancement Script
        env:
          # Ici on utilise VOTRE token admin fourni manuellement
          GH_TOKEN: ${{ inputs.admin_token }}
        run: python _admin_scripts/protect_branch.py
"""

WORKFLOW_ADMIN_ISSUES = r"""name: 🪄 1. Admin - Créer Tâches (Auto)

on:
  workflow_dispatch: # Bouton simple "Run"

# On donne au robot le droit d'écrire des issues
permissions:
  issues: write
  contents: read

jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Lancement Script
        env:
          # Le robot utilise son propre token interne
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python _admin_scripts/create_issues.py
"""

WORKFLOW_CHATOPS_ASSIGN = r"""name: ChatOps Assignation
on:
  issue_comment:
    types: [created]

jobs:
  manage_assignment:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      # Cas 1 : L'étudiant veut prendre la tâche
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
            
      # Cas 2 : L'étudiant veut libérer la tâche
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
"""

# -----------------------------------------------------------------------------
# ⚙️ FICHIER DE CONFIGURATION PYTEST
# -----------------------------------------------------------------------------
CONTENU_PYTEST_INI = r"""[pytest]
python_files = tests/test_*.py
"""

# -----------------------------------------------------------------------------
# 🗺️ MAPPING DES FICHIERS
# -----------------------------------------------------------------------------
MODULES_MAPPING = {
    "mod_cesar.py":        {"src": "src/code_cesar.py",        "test": "tests/test_code_cesar.py"},
    "mod_substitution.py": {"src": "src/code_substitution.py", "test": "tests/test_code_substitution.py"},
    "mod_frequence.py":    {"src": "src/analyse_frequence.py", "test": "tests/test_analyse_frequence.py"},
    "mod_utils.py":        {"src": "src/utilitaires.py",       "test": "tests/test_utilitaires.py"}
}

# =============================================================================
# 🛠️ FONCTIONS UTILITAIRES
# =============================================================================

def load_module_dynamically(mod_filename):
    """Charge un module mod_*.py pour lire ses variables"""
    mod_path = SCRIPT_DIR / mod_filename
    if not mod_path.exists():
        print(f"   ❌ ERREUR CRITIQUE : Fichier introuvable {mod_filename}")
        return None
    try:
        spec = importlib.util.spec_from_file_location(mod_filename[:-3], mod_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"   💥 Erreur lecture {mod_filename} : {e}")
        return None

def write_file(path, content):
    """Écrit le contenu dans un fichier (crée les dossiers si besoin)"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        # Nettoyage des lignes vides inutiles pour les fichiers de config YAML/INI
        if path.suffix in ['.yml', '.yaml', '.ini']:
             content = '\n'.join(line for line in content.splitlines() if line.strip() or line.startswith('#'))
        f.write(content.strip() + "\n")

# =============================================================================
# 🚀 ACTIONS DU MENU
# =============================================================================

def action_0a_squelette():
    """Crée l'arborescence, le main.py, les __init__.py, la config pytest et les workflows"""
    print("\n🏗️  Création du Squelette...")
    
    # 1. Dossiers
    for folder in ["src", "tests", ".github/workflows"]:
        (PROJECT_ROOT / folder).mkdir(parents=True, exist_ok=True)
    
    # 2. FIX CRITIQUE : __init__.py pour que 'src' soit un package
    write_file(PROJECT_ROOT / "src/__init__.py", "")
    write_file(PROJECT_ROOT / "tests/__init__.py", "")
    print("   ✅ Packages initialisés (__init__.py créés)")

    # 3. Workflows GitHub (Les 4 fichiers)
    write_file(PROJECT_ROOT / ".github/workflows/tests.yml", WORKFLOW_TESTS)
    write_file(PROJECT_ROOT / ".github/workflows/admin_1_issues.yml", WORKFLOW_ADMIN_ISSUES)
    # ICI LE NOM CORRESPOND MAINTENANT À LA VARIABLE DÉFINIE PLUS HAUT
    write_file(PROJECT_ROOT / ".github/workflows/admin_2_protection.yml", WORKFLOW_ADMIN_PROTECTION)
    write_file(PROJECT_ROOT / ".github/workflows/assign.yml", WORKFLOW_CHATOPS_ASSIGN)
    print("   ✅ Les 4 Workflows GitHub créés dans .github/workflows/")

    # 4. Configuration Pytest (FIX ModuleNotFoundError)
    write_file(PROJECT_ROOT / "pytest.ini", CONTENU_PYTEST_INI)
    print("   ✅ Configuration Pytest (pytest.ini) générée")
    
    # 5. Main.py
    write_file(PROJECT_ROOT / "main.py", CONTENU_MAIN)
    print("   ✅ main.py généré")

    # 6. Gitignore (VERSION COMPLÈTE)
    gitignore_path = PROJECT_ROOT / ".gitignore"
    if not gitignore_path.exists():
        write_file(gitignore_path, CONTENU_GITIGNORE)
        print("   ✅ .gitignore créé (version complète)")

def action_0b_environnement():
    """Setup .venv et requirements"""
    print("\n🐍 Configuration environnement...")
    venv_path = PROJECT_ROOT / ".venv"

    if not venv_path.exists():
        print(f"   🔨 Création venv...")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", str(venv_path)])
        except Exception as e:
            print(f"   ❌ Erreur venv : {e}")
            return
    else:
        print("   ✅ .venv ok.")

    # Requirements
    req_path = PROJECT_ROOT / "requirements.txt"
    if not req_path.exists():
        # *** MODIFICATION INCLUSION pytest-cov ***
        write_file(req_path, "pytest\npytest-cov\n")
        print("   ℹ️  requirements.txt créé.")

    # Install
    pip_exec = venv_path / ("Scripts" if os.name == 'nt' else "bin") / "pip"
    print("   ⬇️  Pip install...")
    try:
        subprocess.check_call([str(pip_exec), "install", "-r", str(req_path)])
        print("   ✅ Installation finie.")
    except Exception as e:
        print(f"   ❌ Erreur pip : {e}")

def generate_code(mode="STUDENT"):
    """Génère code + tests à partir des mod_*.py"""
    label = "ÉTUDIANT (Trous)" if mode == "STUDENT" else "PROF (Solution)"
    print(f"\n📝 Génération version : {label}")
    
    # On s'assure que la structure de base est là
    action_0a_squelette()
    print("-" * 20)

    for mod_name, targets in MODULES_MAPPING.items():
        module = load_module_dynamically(mod_name)
        if not module: continue

        try:
            content_src = module.STUDENT if mode == "STUDENT" else module.SOLUTION
            content_tests = module.TESTS
        except AttributeError as e:
            print(f"   ❌ {mod_name} invalide : Variable manquante ({e})")
            continue

        dest_src = PROJECT_ROOT / targets["src"]
        dest_test = PROJECT_ROOT / targets["test"]

        write_file(dest_src, content_src)
        print(f"   👤 src/{dest_src.name}")
        
        write_file(dest_test, content_tests)
        print(f"   🧪 tests/{dest_test.name}")

    print(f"\n✅ Projet prêt (Mode {mode}).")

# =============================================================================
# 🖥️ MENU
# =============================================================================

def main():
    while True:
        print("\n" + "="*40)
        print("      ADMINISTRATION PYNIGMA")
        print("="*40)
        print(" 0a) Créer le squelette (Workflows, init, main, pytest.ini)")
        print(" 0b) Paramétrer l'environnement (.venv)")
        print(" 1)  Générer version ÉTUDIANT (Code à trous)")
        print(" 2)  Générer version PROF (Solution complète)")
        print(" q)  Quitter")
        
        choix = input("\nVotre choix > ").strip().lower()

        if choix == "0a": action_0a_squelette()
        elif choix == "0b": action_0b_environnement()
        elif choix == "1": generate_code(mode="STUDENT")
        elif choix == "2": generate_code(mode="SOLUTION")
        elif choix == "q": break
        else: print("❌ Choix invalide.")

if __name__ == "__main__":
    main()