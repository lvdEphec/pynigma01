import pytest
import string
from src import code_cesar, code_substitution, analyse_frequence, utilitaires

def check(valeur):
    """Si la valeur est NotImplemented, on skip. Sinon on retourne la valeur."""
    if valeur is NotImplemented:
        pytest.skip("Fonction à implémenter")
    return valeur

# ==========================================
# Tests pour : compter_lettres
# ==========================================

def test_compter_lettres_nominal():
    # Vérifie le comptage simple
    resultat = check(analyse_frequence.compter_lettres("BABA"))
    assert resultat['B'] == 2
    assert resultat['A'] == 2

def test_compter_lettres_ignorer_non_lettres():
    # Doit ignorer les espaces, chiffres et ponctuation
    resultat = check(analyse_frequence.compter_lettres("A 1 ! A"))
    assert ' ' not in resultat
    assert '1' not in resultat
    assert '!' not in resultat
    assert resultat['A'] == 2

def test_compter_lettres_vide():
    resultat = check(analyse_frequence.compter_lettres(""))
    assert resultat == {}


# ==========================================
# Tests pour : obtenir_lettre_la_plus_frequente
# ==========================================

def test_obtenir_frequente_typique():
    resultat = check(analyse_frequence.obtenir_lettre_la_plus_frequente("AAABBBBC"))
    assert resultat == 'B'

def test_obtenir_frequente_egalite():
    # En cas d'égalité (A:2, B:2), l'une ou l'autre est acceptée
    res = check(analyse_frequence.obtenir_lettre_la_plus_frequente("AABB"))
    assert res in ['A', 'B']

def _():
    # Cas limite : texte vide -> None
    resultat = check(analyse_frequence.obtenir_lettre_la_plus_frequente(""))
    assert resultat is None


# ==========================================
# Tests pour : calculer_similitude
# ==========================================

def test_calculer_similitude_identique():
    resultat = check(analyse_frequence.calculer_similitude("ABC", "ABC"))
    assert resultat == 1.0

def test_calculer_similitude_totalement_different():
    resultat = check(analyse_frequence.calculer_similitude("ABC", "DEF"))
    assert resultat == 0.0

def test_calculer_similitude_partielle():
    # 2 lettres communes (A, B) sur une longueur max de 3
    resultat = check(analyse_frequence.calculer_similitude("ABC", "ABD"))
    assert resultat == (2/3)

def test_calculer_similitude_longueurs_differentes():
    # "CHAT" (4) vs "CH" (2) -> 2 correspondances / 4 longueur max = 0.5
    resultat = check(analyse_frequence.calculer_similitude("CHAT", "CH"))
    assert resultat == 0.5


# ==========================================
# Tests pour : detecter_langue
# ==========================================

def test_detecter_langue_anglais_phrase():
    # Phrase : "THE WAY"
    # EN : TH(1) + W(1) + Y(1) = 3
    # FR : E(1 dans THE) = 1
    # 3 > 1 -> EN
    resultat = check(analyse_frequence.detecter_langue("THE WAY"))
    assert resultat == "EN"

def test_detecter_langue_francais_phrase():
    # Phrase : "LA TETE"
    # EN : 0
    # FR : E(2) = 2
    # 0 <= 2 -> FR
    resultat = check(analyse_frequence.detecter_langue("LA TETE"))
    assert resultat == "FR"

def test_detecter_langue_piege_faux_ami():
    # Piège : Phrase française avec des mots anglais/exotiques
    # "LE WEEK-END EN KAYAK"
    # EN : W(1) + Y(1) = 2
    # FR : E(4) = 4
    # 2 <= 4 -> FR (Le français gagne grâce aux E)
    resultat = check(analyse_frequence.detecter_langue("LE WEEK-END EN KAYAK"))
    assert resultat == "FR"

def test_detecter_langue_egalite_par_defaut():
    # W (1pt EN) vs E (1pt FR) -> Egalité -> FR
    resultat = check(analyse_frequence.detecter_langue("WE"))
    assert resultat == "FR"


# ==========================================
# Tests pour : est_palindrome
# ==========================================

def test_est_palindrome_simple():
    assert check(analyse_frequence.est_palindrome("KAYAK")) is True

def test_est_palindrome_faux():
    assert check(analyse_frequence.est_palindrome("BONJOUR")) is False

def test_est_palindrome_phrase_complexe():
    # Doit ignorer les espaces, la ponctuation et la casse
    # "L'ami naturel ?" -> "LAMINATUREL" (Pas palindrome)
    # "Engage le jeu que je le gagne" -> "ENGAGELEJEUQUEJELEGAGNE" (Palindrome)
    resultat = check(analyse_frequence.est_palindrome("Engage le jeu que je le gagne"))
    assert resultat is True