def code_miroir(message):
    """
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
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def vers_leet_speak(message):
    """
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
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def depuis_leet_speak(message):
    """
    Retrouve le texte original depuis du Leet Speak.
    Inverse les règles : 3->E, 4->A, 7->T, 1->I, 0->O, 5->S.

    Args:
        message (str): Le texte en Leet Speak.

    Returns:
        str: Le texte lisible (en majuscule).

    Example:
        >>> depuis_leet_speak("35710")
        'ESTIO'
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def chiffrer_vigenere(message, cle):
    """
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
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def dechiffrer_vigenere(message, cle):
    """
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
    """
    return NotImplemented