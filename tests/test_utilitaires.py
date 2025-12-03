import pytest
import string
from src import code_cesar, code_substitution, analyse_frequence, utilitaires

def check(valeur):
    """Si la valeur est NotImplemented, on skip. Sinon on retourne la valeur."""
    if valeur is NotImplemented:
        pytest.skip("Fonction à implémenter")
    return valeur

# ==========================================
# Tests pour : generer_mot_de_passe
# ==========================================

def test_generer_mot_de_passe_longueur():
    # Vérifie que la longueur demandée est respectée
    val = check(utilitaires.generer_mot_de_passe(12))
    assert len(val) == 12

def test_generer_mot_de_passe_aleatoire():
    # Deux appels successifs ne doivent pas générer le même résultat
    mdp1 = check(utilitaires.generer_mot_de_passe(12))
    mdp2 = utilitaires.generer_mot_de_passe(12)
    assert mdp1 != mdp2

def test_generer_mot_de_passe_complexite():
    # Spec: Doit contenir Maj, Min, Chiffre et Spécial (!@#$%)
    # On génère un MDP très long (100 chars) pour garantir statistiquement 
    # la présence de tous les types de caractères sans "flaky test".
    val = check(utilitaires.generer_mot_de_passe(100))
    
    a_maj = any(c.isupper() for c in val)
    a_min = any(c.islower() for c in val)
    a_digit = any(c.isdigit() for c in val)
    a_special = any(c in "!@#$%" for c in val)
    
    assert a_maj is True, "Le mot de passe doit contenir une majuscule"
    assert a_min is True, "Le mot de passe doit contenir une minuscule"
    assert a_digit is True, "Le mot de passe doit contenir un chiffre"
    assert a_special is True, "Le mot de passe doit contenir un caractère spécial (!@#$%)"


# ==========================================
# Tests pour : formater_en_blocs
# ==========================================

def test_formater_en_blocs_standard():
    # Découpage propre
    resultat = check(utilitaires.formater_en_blocs("AABBCC", 2))
    assert resultat == "AA BB CC"

def test_formater_en_blocs_reste():
    # Gestion du reste (5 lettres par blocs de 2 -> 2 2 1)
    resultat = check(utilitaires.formater_en_blocs("12345", 2))
    assert resultat == "12 34 5"

def test_formater_en_blocs_vide():
    assert check(utilitaires.formater_en_blocs("", 5)) == ""


# ==========================================
# Tests pour : compter_mots
# ==========================================

def test_compter_mots_simple():
    resultat = check(utilitaires.compter_mots("Bonjour le monde"))
    assert resultat == 3

def test_compter_mots_avec_espaces_multiples():
    # Les espaces multiples ne doivent pas compter comme des mots vides
    # "Un   deux" -> 2 mots
    resultat = check(utilitaires.compter_mots("Un   deux"))
    assert resultat == 2

def test_compter_mots_vide():
    assert check(utilitaires.compter_mots("")) == 0
    assert check(utilitaires.compter_mots("   ")) == 0


# ==========================================
# Tests pour : est_mot_de_passe_fort
# ==========================================

def test_est_mdp_fort_faible_taille():
    # Trop court (< 8)
    assert check(utilitaires.est_mot_de_passe_fort("Admin1!")) is False

def test_est_mdp_fort_faible_sans_chiffre():
    # Manque chiffre
    assert check(utilitaires.est_mot_de_passe_fort("AdminAdmin")) is False

def test_est_mdp_fort_faible_sans_maj():
    # Manque majuscule
    assert check(utilitaires.est_mot_de_passe_fort("admin123")) is False

def test_est_mdp_fort_faible_sans_min():
    # Manque minuscule
    assert check(utilitaires.est_mot_de_passe_fort("ADMIN123")) is False

def test_est_mdp_fort_valide():
    # Tout y est
    assert check(utilitaires.est_mot_de_passe_fort("Admin123")) is True


# ==========================================
# Tests pour : masquer_texte
# ==========================================

def test_masquer_texte_long():
    # Masque tout sauf les 2 derniers
    assert check(utilitaires.masquer_texte("123456")) == "****56"

def test_masquer_texte_limite():
    # 3 chars -> *23
    assert check(utilitaires.masquer_texte("123")) == "*23"

def test_masquer_texte_court():
    # Si <= 2, on ne masque pas (sinon on perd tout)
    assert check(utilitaires.masquer_texte("AB")) == "AB"
    assert check(utilitaires.masquer_texte("A")) == "A"
    assert check(utilitaires.masquer_texte("")) == ""

# ==========================================
# Tests pour : un_pour_prof
# ==========================================

def test_un_pour_prof():
    # 1
    assert check(utilitaires.un_pour_prof()) == 1