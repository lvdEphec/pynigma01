import pytest
import string
from src import code_cesar, code_substitution, analyse_frequence, utilitaires

def check(valeur):
    """Si la valeur est NotImplemented, on skip. Sinon on retourne la valeur."""
    if valeur is NotImplemented:
        pytest.skip("Fonction à implémenter")
    return valeur

# -----------------------------------------------------------------------------
# Tests unitaires pour : code_lettre
# -----------------------------------------------------------------------------

def test_code_lettre_nominal():
    # Cas standard : A + 1 = B
    assert check(code_cesar.code_lettre('A', 1)) == 'B'

def test_code_lettre_saut_alphabet():
    # Cas de rotation : Z + 1 = A
    assert check(code_cesar.code_lettre('Z', 1)) == 'A'
    assert check(code_cesar.code_lettre('Y', 3)) == 'B'

def test_code_lettre_decalage_negatif():
    # Cas arrière : B - 1 = A
    assert check(code_cesar.code_lettre('B', -1)) == 'A'
    assert check(code_cesar.code_lettre('A', -1)) == 'Z'

def test_code_lettre_grand_decalage():
    # Cas modulo : A + 27 (26+1) = B
    assert check(code_cesar.code_lettre('A', 27)) == 'B'
    assert check(code_cesar.code_lettre('A', 52)) == 'A'

def test_code_lettre_minuscule():
    # Spec : Doit traiter la minuscule et renvoyer une MAJUSCULE
    assert check(code_cesar.code_lettre('a', 1)) == 'B'
    assert check(code_cesar.code_lettre('z', 1)) == 'A'

def test_code_lettre_invariant():
    # Spec : Les caractères non-lettres restent inchangés
    assert check(code_cesar.code_lettre('!', 5)) == '!'
    assert check(code_cesar.code_lettre('1', 5)) == '1'
    assert check(code_cesar.code_lettre(' ', 5)) == ' '


# -----------------------------------------------------------------------------
# Tests unitaires pour : chiffrer_cesar
# -----------------------------------------------------------------------------

def test_chiffrer_nominal():
    assert check(code_cesar.chiffrer_cesar("HAL", 1)) == "IBM"

def test_chiffrer_phrase_complexe():
    # Mélange de majuscules, minuscules, espaces et ponctuation
    entree = "Salut, ça va ?"
    # S->T, a->B, l->M, u->V, t->U, ...
    attendu = "TBMVU, ÇB WB ?" # Note : ç et à ne sont pas traités par défaut (voir nettoyer)
    # Pour simplifier le test sans nettoyer_accents avant :
    assert check(code_cesar.chiffrer_cesar("Hello World!", 1)) == "IFMMP XPSME!"

def test_chiffrer_vide():
    # Edge case : chaîne vide
    assert check(code_cesar.chiffrer_cesar("", 5)) == ""

def test_chiffrer_decalage_nul():
    # Identité
    assert check(code_cesar.chiffrer_cesar("TEST", 0)) == "TEST"


# -----------------------------------------------------------------------------
# Tests unitaires pour : dechiffrer_cesar
# -----------------------------------------------------------------------------

def test_dechiffrer_nominal():
    assert check(code_cesar.dechiffrer_cesar("IBM", 1)) == "HAL"

def test_dechiffrer_cycle_complet():
    # Chiffrer puis déchiffrer doit redonner l'original
    original = "MESSAGE SECRET 123"
    chiffre = check(code_cesar.chiffrer_cesar(original, 13))
    clair = check(code_cesar.dechiffrer_cesar(chiffre, 13))
    assert clair == original


# -----------------------------------------------------------------------------
# Tests unitaires pour : est_lettre
# -----------------------------------------------------------------------------

def test_est_lettre_vrai():
    assert check(code_cesar.est_lettre('A')) is True
    assert check(code_cesar.est_lettre('b')) is True

def test_est_lettre_faux():
    assert check(code_cesar.est_lettre('1')) is False
    assert check(code_cesar.est_lettre('!')) is False
    assert check(code_cesar.est_lettre(' ')) is False
    assert check(code_cesar.est_lettre('')) is False # Vide

def test_est_lettre_accents():
    # Selon la spec ASCII stricte
    assert check(code_cesar.est_lettre('é')) is False


# -----------------------------------------------------------------------------
# Tests unitaires pour : nettoyer_accents
# -----------------------------------------------------------------------------

def test_nettoyer_accents_base():
    assert check(code_cesar.nettoyer_accents("été")) == "ETE"

def test_nettoyer_accents_tout_type():
    # ç -> C, à -> A, ù -> U
    assert check(code_cesar.nettoyer_accents("Ça va où ?")) == "CA VA OU ?"

def test_nettoyer_accents_vide():
    assert check(code_cesar.nettoyer_accents("")) == ""