def code_lettre(lettre, decalage):
    """
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
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def chiffrer_cesar(message, decalage):
    """
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
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def dechiffrer_cesar(message, decalage):
    """
    Inverse l'opération de chiffrement.
    
    Astuce : Mathématiquement, déchiffrer avec un décalage N revient à 
    chiffrer avec un décalage -N. Ne réécrivez pas la logique, réutilisez `chiffrer_cesar`.

    Args:
        message (str): Le texte chiffré.
        decalage (int): Le décalage qui a été utilisé pour chiffrer.

    Returns:
        str: Le message en clair.
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def est_lettre(char):
    """
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
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def nettoyer_accents(texte):
    """
    Prépare un texte brut pour le chiffrement.
    
    Actions à effectuer :
    1. Remplacer les caractères accentués par leur équivalent sans accent 
       (é -> e, ç -> c, etc.).
    2. Convertir tout le texte en MAJUSCULES.
    
    Utilisez ce dictionnaire de correspondance :
    accs = {'É':'E', 'È':'E', 'Ê':'E', 'À':'A', 'Ù':'U', 'Ç':'C', 'Ô':'O', 'Ò':'O', 'Î':'I', 'Ï':'I'}

    Args:
        texte (str): Le texte brut.

    Returns:
        str: Le texte nettoyé.

    Example:
        >>> nettoyer_accents("Héllò")
        'HELLO'
    """
    return NotImplemented