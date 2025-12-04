from config import PADDING, TEST_HEADER

# =============================================================================
# 1. LES TESTS UNITAIRES (RIGOUREUX & COMPLETS)
# =============================================================================
TESTS = TEST_HEADER + """
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
"""

# =============================================================================
# 2. SQUELETTE ETUDIANT (DOCSTRINGS GOOGLE STYLE & EXEMPLES)
# =============================================================================
STUDENT = f"""
def code_lettre(lettre, decalage):
    \"\"\"
    Décale une SEULE lettre en utilisant le code César.
    
    Règles métier :
    1. Si `lettre` n'est pas une lettre de l'alphabet (ex: '!', '1', ' '), elle est retournée inchangée.
    2. La lettre est d'abord convertie en MAJUSCULE.
    3. Le décalage est circulaire (Z + 1 = A).
    4. Le décalage peut être négatif ou supérieur à 26.

    Args:
        lettre (str): Le caractère unique à traiter.
        decalage (int): Le nombre de positions de décalage.

    Returns:
        str: Le caractère résultant (toujours en majuscule si c'est une lettre).

    Examples:
        >>> code_lettre('A', 1)
        'B'
        >>> code_lettre('z', 1)
        'A'
        >>> code_lettre('!', 5)
        '!'
    \"\"\"
    return NotImplemented
{PADDING}
def chiffrer_cesar(message, decalage):
    \"\"\"
    Chiffre une chaîne de caractères complète.
    
    Cette fonction doit itérer sur chaque caractère du message et utiliser
    la fonction `code_lettre` pour le transformer.

    Args:
        message (str): Le texte à chiffrer.
        decalage (int): Le décalage à appliquer.

    Returns:
        str: Le message chiffré.

    Examples:
        >>> chiffrer_cesar("HAL", 1)
        'IBM'
        >>> chiffrer_cesar("Hello World!", 1)
        'IFMMP XPSME!'
    \"\"\"
    return NotImplemented
{PADDING}
def dechiffrer_cesar(message, decalage):
    \"\"\"
    Inverse l'opération de chiffrement.
    
    Astuce : Mathématiquement, déchiffrer avec un décalage N revient à 
    chiffrer avec un décalage -N. Ne réécrivez pas la logique, réutilisez `chiffrer_cesar`.

    Args:
        message (str): Le texte chiffré.
        decalage (int): Le décalage qui a été utilisé pour chiffrer.

    Returns:
        str: Le message en clair.
    \"\"\"
    return NotImplemented
{PADDING}
def est_lettre(char):
    \"\"\"
    Vérifie si un caractère est une lettre de l'alphabet standard (A-Z).
    Pour cet exercice, on considère que les lettres accentuées NE SONT PAS 
    des lettres standards (pour simplifier les maths).

    Args:
        char (str): Le caractère à tester.

    Returns:
        bool: True si c'est une lettre ASCII (A-Z ou a-z), False sinon.

    Examples:
        >>> est_lettre('A')
        True
        >>> est_lettre('!')
        False
        >>> est_lettre('é')
        False
    \"\"\"
    return NotImplemented
{PADDING}
def nettoyer_accents(texte):
    \"\"\"
    Prépare un texte brut pour le chiffrement.
    
    Actions à effectuer :
    1. Remplacer les caractères accentués par leur équivalent sans accent 
       (é -> e, ç -> c, etc.).
    2. Convertir tout le texte en MAJUSCULES.
    
    Utilisez ce dictionnaire de correspondance :
    accs = {{'É':'E', 'È':'E', 'Ê':'E', 'À':'A', 'Ù':'U', 'Ç':'C', 'Ô':'O', 'Ò':'O', 'Î':'I', 'Ï':'I'}}

    Args:
        texte (str): Le texte brut.

    Returns:
        str: Le texte nettoyé.

    Example:
        >>> nettoyer_accents("Héllò")
        'HELLO'
    \"\"\"
    return NotImplemented
"""

# =============================================================================
# 3. SOLUTION PROFESSEUR (ROBUSTE)
# =============================================================================
SOLUTION = f"""
def code_lettre(lettre, decalage):
    # Règle défensive : si ce n'est pas une lettre, on touche pas
    if not est_lettre(lettre): 
        return lettre.upper() # On renvoie quand même en majuscule par cohérence
    
    # Conversion ASCII -> 0-25
    code_base = ord(lettre.upper()) - ord('A')
    
    # Application du décalage avec Modulo pour la rotation
    nouveau_code = (code_base + decalage) % 26
    
    # Retour au caractère
    return chr(nouveau_code + ord('A'))
{PADDING}
def chiffrer_cesar(message, decalage):
    resultat = []
    for caractere in message:
        lettre_chiffree = code_lettre(caractere, decalage)
        resultat.append(lettre_chiffree)
    return "".join(resultat)
{PADDING}
def dechiffrer_cesar(message, decalage):
    return chiffrer_cesar(message, -decalage)
{PADDING}
def est_lettre(char):
    # On vérifie que la chaine n'est pas vide et est une lettre ascii
    return len(char) == 1 and char.isascii() and char.isalpha()
{PADDING}
def nettoyer_accents(texte):
    accs = {{'É':'E', 'È':'E', 'Ê':'E', 'À':'A', 'Ù':'U', 'Ç':'C', 'Ô':'O', 'Ò':'O', 'Î':'I', 'Ï':'I'}}
    texte_propre = ""
    for char in texte.upper():
        texte_propre += accs.get(char, char)
    return texte_propre
"""