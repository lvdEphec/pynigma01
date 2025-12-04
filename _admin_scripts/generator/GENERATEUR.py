import os
import sys
import subprocess

# Importation des modules locaux (Tes fichiers de config)
# C'est ici que la magie opère : on récupère le contenu des autres fichiers
import config
import mod_infra
import mod_cesar
import mod_substitution
import mod_frequence
import mod_utils

# Le projet sera généré un cran au-dessus du dossier _admin_scripts
PROJECT_NAME = "../.." #PROJECT_ROOT

def write_files(file_dict, force=False):
    """Ecrit les fichiers sur le disque."""
    for path, content in file_dict.items():
        # Construction du chemin complet
        full_path = os.path.join(PROJECT_NAME, path)
        
        # Création des dossiers parents si nécessaire
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Protection contre l'écrasement (sauf si force=True)
        if not force and os.path.exists(full_path):
            print(f"  ⏭️  Ignoré (existe déjà) : {path}")
            continue
            
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        
        icon = "♻️ " if os.path.exists(full_path) and force else "📄"
        print(f"  {icon} {path}")

def setup_environment():
    """Installe le venv et les librairies."""
    project_path = os.path.abspath(PROJECT_NAME)
    venv_path = os.path.join(project_path, ".venv")
    requirements_path = os.path.join(project_path, "requirements.txt")
    
    print(f"\n⚙️  Configuration dans : {project_path}")
    
    # 1. Création Venv
    if not os.path.exists(venv_path):
        print("  🔨 Création du virtualenv (.venv)...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_path])
    
    # 2. Détection de pip
    if os.name == 'nt':
        pip_exe = os.path.join(venv_path, "Scripts", "pip.exe")
    else:
        pip_exe = os.path.join(venv_path, "bin", "pip")
    
    # 3. Installation
    if os.path.exists(requirements_path):
        print(f"  📦 Installation via {pip_exe}...")
        try:
            subprocess.check_call([pip_exe, "install", "-r", requirements_path])
            print("  ✅ Installation OK !")
        except Exception:
            print("  ❌ Erreur d'installation")
    else:
        print("  ⚠️ Le fichier requirements.txt n'existe pas encore (Lancez l'option 0a).")

def main():
    # Création du dossier racine s'il n'existe pas
    if not os.path.exists(PROJECT_NAME):
        os.makedirs(PROJECT_NAME)
        print(f"📁 Dossier racine '{PROJECT_NAME}' créé.")

    print(f"\n🔧 GÉNÉRATEUR DE PROJET : {PROJECT_NAME}")
    print("===================================")
    print(" 0a. SQUELETTE      : Répare l'infra (Github, Main, Config).")
    print(" 0b. ENVIRONNEMENT  : Installe .venv et pytest.")
    print(" 1.  SOLUTION       : ⚠️  Écrase tout avec le code PROF (Vert).")
    print(" 2.  ÉTUDIANT       : ⚠️  Écrase tout avec le code VIDE (Jaune).")
    print("===================================")
    
    choice = input("Votre choix > ").strip().lower()
    
    # --- ASSEMBLAGE DU PUZZLE ---
    # On va chercher les morceaux dans chaque module
    
    ALL_TESTS = {
        "tests/test_code_cesar.py": mod_cesar.TESTS,
        "tests/test_code_substitution.py": mod_substitution.TESTS,
        "tests/test_analyse_frequence.py": mod_frequence.TESTS,
        "tests/test_utilitaires.py": mod_utils.TESTS,
    }
    
    ALL_SOLUTIONS = {
        "src/code_cesar.py": mod_cesar.SOLUTION,
        "src/code_substitution.py": mod_substitution.SOLUTION,
        "src/analyse_frequence.py": mod_frequence.SOLUTION,
        "src/utilitaires.py": mod_utils.SOLUTION,
    }
    
    ALL_STUDENTS = {
        "src/code_cesar.py": mod_cesar.STUDENT,
        "src/code_substitution.py": mod_substitution.STUDENT,
        "src/analyse_frequence.py": mod_frequence.STUDENT,
        "src/utilitaires.py": mod_utils.STUDENT,
    }

    print("\n⏳ Traitement en cours...")

    if choice == "0a":
        # Infra + Tests (Sans écraser l'existant si possible)
        write_files(mod_infra.FILES, force=False)
        write_files(ALL_TESTS, force=False) 
        # On écrit les fichiers source vides UNIQUEMENT s'ils manquent (pour éviter les erreurs d'import)
        write_files(ALL_STUDENTS, force=False)
        print("\n✅ Terminé (Mode Squelette).")

    elif choice == "0b":
        setup_environment()

    elif choice == "1":
        # Mode PROF : On force tout
        write_files(mod_infra.FILES, force=True)
        write_files(ALL_TESTS, force=True)
        write_files(ALL_SOLUTIONS, force=True)
        print("\n✅ Terminé (Mode SOLUTION).")

    elif choice == "2":
        # Mode ÉTUDIANT : On force tout avec le code vide
        write_files(mod_infra.FILES, force=True)
        write_files(ALL_TESTS, force=True)
        write_files(ALL_STUDENTS, force=True)
        print("\n✅ Terminé (Mode ÉTUDIANT).")

    else:
        print("❌ Choix invalide.")

if __name__ == "__main__":
    main()