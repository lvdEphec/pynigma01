import pytest
import string
from src import code_cesar, code_substitution, analyse_frequence, utilitaires

def check(valeur):
    """Si la valeur est NotImplemented, on skip. Sinon on retourne la valeur."""
    if valeur is NotImplemented:
        pytest.skip("Fonction à implémenter")
    return valeur

# ==========================================
# Tests pour : code_miroir
# ==========================================

def test_code_miroir_nominal(): 
    # A(1er) <-> Z(26e)
    # B(2e) <-> Y(25e)
    resultat = check(code_substitution.code_miroir("ABC"))
    assert resultat == "ZYX"

def test_code_miroir_phrase_avec_espaces():
    # Les espaces et la ponctuation doivent être conservés
    # A -> Z, Z -> A, U -> F, Y -> B
    resultat = check(code_substitution.code_miroir("AZ UY!"))
    assert resultat == "ZA FB!" # Correction ici (C'était BY avant, ce qui est faux)

def test_code_miroir_vide():
    assert check(code_substitution.code_miroir("")) == ""

def test_code_miroir_cycle():
    # Miroir(Miroir(X)) == X
    msg = "TEST"
    premier_passage = check(code_substitution.code_miroir(msg))
    second_passage = check(code_substitution.code_miroir(premier_passage))
    assert second_passage == msg


# ==========================================
# Tests pour : vers_leet_speak
# ==========================================

def test_vers_leet_speak_dictionnaire_complet(): 
    # Vérification de tout le dictionnaire demandé
    # E->3, A->4, T->7, I->1, O->0, S->5
    entree = "ESTIOA"
    attendu = "357104"
    resultat = check(code_substitution.vers_leet_speak(entree))
    assert resultat == attendu

def test_vers_leet_speak_mixte_et_invariants():
    # Doit gérer majuscules/minuscules et caractères hors dico
    # H -> H (pas de changement)
    # e -> 3 (changement)
    entree = "Hello World!"
    attendu = "H3LL0 W0RLD!"
    resultat = check(code_substitution.vers_leet_speak(entree))
    assert resultat == attendu

def test_vers_leet_speak_vide():
    assert check(code_substitution.vers_leet_speak("")) == ""


# ==========================================
# Tests pour : depuis_leet_speak
# ==========================================

def test_depuis_leet_speak_nominal(): 
    # Opération inverse
    entree = "35710"
    attendu = "ESTIO"
    resultat = check(code_substitution.depuis_leet_speak(entree))
    assert resultat == attendu

def test_depuis_leet_speak_phrase():
    entree = "H3LL0 W0RLD"
    attendu = "HELLO WORLD"
    resultat = check(code_substitution.depuis_leet_speak(entree))
    assert resultat == attendu


# ==========================================
# Tests pour : chiffrer_vigenere
# ==========================================

def test_chiffrer_vigenere_cle_identite(): 
    # Si la clé est 'A' (index 0), le texte ne change pas
    # Si la clé est 'AAAA', c'est pareil
    resultat = check(code_substitution.chiffrer_vigenere("HELLO", "A"))
    assert resultat == "HELLO"

def test_chiffrer_vigenere_nominal():
    # PARIS (15,0,17,8,18) + CLE (2,11,4) 
    # P(15)+C(2)=R(17)
    # A(0)+L(11)=L(11)
    # R(17)+E(4)=V(21)
    # I(8)+C(2)=K(10) ... on boucle sur la clé
    # Résultat attendu : RLVKD
    resultat = check(code_substitution.chiffrer_vigenere("PARIS", "CLE"))
    assert resultat == "RLVKD"

def test_chiffrer_vigenere_gestion_espaces_message():
    # Point CRITIQUE de l'algo : 
    # Les espaces du message ne doivent PAS faire avancer l'index de la clé.
    # Message : "A A" (A, Espace, A)
    # Clé     : "B C" (B, C)
    # 1. 'A' chiffré avec 'B' (+1) -> 'B'
    # 2. ' ' ignoré (index clé ne bouge pas) -> ' '
    # 3. 'A' chiffré avec 'C' (+2) -> 'C' (et non avec B !)
    # Résultat attendu : "B C"
    entree = "A A"
    cle = "BC"
    resultat = check(code_substitution.chiffrer_vigenere(entree, cle))
    assert resultat == "B C"

def test_chiffrer_vigenere_cle_avec_espaces():
    # La clé doit être nettoyée (les espaces virés) avant usage
    # "C L E" doit devenir "CLE"
    resultat = check(code_substitution.chiffrer_vigenere("PARIS", "C L E"))
    assert resultat == "RLVKD"

def test_chiffrer_vigenere_vide():
    assert check(code_substitution.chiffrer_vigenere("", "CLE")) == ""


# ==========================================
# Tests pour : dechiffrer_vigenere
# ==========================================

def test_dechiffrer_vigenere_nominal(): 
    # Inverse exact du chiffrement
    resultat = check(code_substitution.dechiffrer_vigenere("RLVKD", "CLE"))
    assert resultat == "PARIS"

def test_dechiffrer_vigenere_phrase():
    chiffre = "B C"
    cle = "BC"
    # B(-1) -> A, Espace, C(-2) -> A
    resultat = check(code_substitution.dechiffrer_vigenere(chiffre, cle))
    assert resultat == "A A"