from config import PADDING, TEST_HEADER

# =============================================================================
# 1. TESTS UNITAIRES (Rigoureux)
# =============================================================================
TESTS = TEST_HEADER + """
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
"""

# =============================================================================
# 2. SQUELETTE ETUDIANT (Specs précises)
# =============================================================================
STUDENT = f"""
def code_miroir(message):
    \"\"\"
    Applique le chiffrement miroir (aussi appelé Atbash).
    L'alphabet est inversé : 
    A <-> Z
    B <-> Y
    C <-> X
    ...
    M <-> N

    Règles :
    - Les caractères non-alphabétiques (chiffres, ponctuation) restent inchangés.
    - La casse (majuscule/minuscule) est harmonisée en MAJUSCULE.

    Args:
        message (str): Le texte à chiffrer.

    Returns:
        str: Le texte chiffré.

    Example:
        >>> code_miroir("AZ")
        'ZA'
        >>> code_miroir("Hello")
        'SVOOL'
    \"\"\"
    return NotImplemented
{PADDING}
def vers_leet_speak(message):
    \"\"\"
    Transforme le texte en Leet Speak (remplacement par des chiffres).
    
    Dictionnaire de remplacement OBLIGATOIRE :
    E -> 3
    A -> 4
    T -> 7
    I -> 1
    O -> 0
    S -> 5
    
    Règles :
    - Tout doit être mis en majuscules avant la conversion.
    - Les caractères qui ne sont pas dans le dictionnaire restent inchangés.

    Args:
        message (str): Le texte original.

    Returns:
        str: Le texte transformé.

    Example:
        >>> vers_leet_speak("ESTIO")
        '35710'
        >>> vers_leet_speak("Table")
        '74BL3'
    \"\"\"
    return NotImplemented
{PADDING}
def depuis_leet_speak(message):
    \"\"\"
    Retrouve le texte original depuis du Leet Speak.
    Inverse les règles : 3->E, 4->A, 7->T, 1->I, 0->O, 5->S.

    Args:
        message (str): Le texte en Leet Speak.

    Returns:
        str: Le texte lisible (en majuscule).

    Example:
        >>> depuis_leet_speak("35710")
        'ESTIO'
    \"\"\"
    return NotImplemented
{PADDING}
def chiffrer_vigenere(message, cle):
    \"\"\"
    Chiffre avec la méthode de Vigenère (Code César à clé variable).
    
    Algorithme :
    Pour chaque lettre du message (index i) :
    1. Si ce n'est pas une lettre, on l'ajoute tel quel au résultat.
    2. Sinon :
       a. On trouve la lettre correspondante dans la clé.
          Attention : L'index dans la clé n'avance QUE si on chiffre une lettre.
          Lettre clé = cle[index_cle % len(cle)]
       b. Calculer le décalage : position de la lettre clé (A=0, B=1...).
       c. Appliquer ce décalage à la lettre du message (comme César).
       d. Incrémenter l'index de la clé.

    Pré-requis :
    - Le message et la clé doivent être mis en majuscules.
    - La clé doit être "nettoyée" (retirer les espaces) avant de commencer.

    Args:
        message (str): Le texte à chiffrer.
        cle (str): La clé de chiffrement (ex: "MUSIQUE").

    Returns:
        str: Le message chiffré.

    Example:
        >>> chiffrer_vigenere("PARIS", "CLE")
        'RLVKD'
    \"\"\"
    return NotImplemented
{PADDING}
def dechiffrer_vigenere(message, cle):
    \"\"\"
    Déchiffre un message Vigenère.
    Même logique que le chiffrement, mais on SOUSTRAIT le décalage au lieu de l'ajouter.

    Args:
        message (str): Le texte chiffré.
        cle (str): La clé utilisée.

    Returns:
        str: Le message en clair.

    Example:
        >>> dechiffrer_vigenere("RLVKD", "CLE")
        'PARIS'
    \"\"\"
    return NotImplemented
"""

# =============================================================================
# 3. SOLUTION PROFESSEUR (Optimisée)
# =============================================================================
SOLUTION = f"""
import string

def code_miroir(message):
    alphabet_normal = string.ascii_uppercase
    alphabet_miroir = alphabet_normal[::-1]
    
    # maketrans crée une table de correspondance performante
    table_traduction = str.maketrans(alphabet_normal, alphabet_miroir)
    return message.upper().translate(table_traduction)
{PADDING}
def vers_leet_speak(message):
    remplacements = {{'E': '3', 'A': '4', 'T': '7', 'I': '1', 'O': '0', 'S': '5'}}
    resultat = ""
    for char in message.upper():
        resultat += remplacements.get(char, char)
    return resultat
{PADDING}
def depuis_leet_speak(message):
    remplacements = {{'3': 'E', '4': 'A', '7': 'T', '1': 'I', '0': 'O', '5': 'S'}}
    resultat = ""
    for char in message.upper():
        resultat += remplacements.get(char, char)
    return resultat
{PADDING}
def chiffrer_vigenere(message, cle):
    # Préparation
    message = message.upper()
    cle = cle.upper().replace(" ", "") # Nettoyage de la clé
    
    if not cle: # Sécurité si clé vide
        return message
        
    resultat = ""
    index_cle = 0
    
    for char in message:
        if char.isalpha():
            # 1. Récupérer le décalage depuis la clé
            lettre_cle = cle[index_cle % len(cle)]
            decalage = ord(lettre_cle) - ord('A')
            
            # 2. Appliquer le décalage (César)
            code_base = ord(char) - ord('A')
            nouveau_code = (code_base + decalage) % 26
            resultat += chr(nouveau_code + ord('A'))
            
            # 3. Avancer dans la clé
            index_cle += 1
        else:
            # Caractère spécial : pas de chiffrement, pas d'avancée de clé
            resultat += char
            
    return resultat
{PADDING}
def dechiffrer_vigenere(message, cle):
    message = message.upper()
    cle = cle.upper().replace(" ", "")
    
    if not cle:
        return message
        
    resultat = ""
    index_cle = 0
    
    for char in message:
        if char.isalpha():
            lettre_cle = cle[index_cle % len(cle)]
            decalage = ord(lettre_cle) - ord('A')
            
            # Soustraction (+26 pour le modulo positif en Python, bien que % gère les négatifs)
            code_base = ord(char) - ord('A')
            nouveau_code = (code_base - decalage) % 26
            resultat += chr(nouveau_code + ord('A'))
            
            index_cle += 1
        else:
            resultat += char
            
    return resultat
"""