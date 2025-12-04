import sys
import os

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