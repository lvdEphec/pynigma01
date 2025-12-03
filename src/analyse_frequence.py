def compter_lettres(texte):
    """
    Compte le nombre d'apparitions de chaque lettre dans le texte.
    
    Règles :
    - Ignorer les espaces, chiffres et caractères spéciaux.
    - Convertir tout en majuscules avant de compter.

    Args:
        texte (str): Le texte à analyser.

    Returns:
        dict: Un dictionnaire {'LETTRE': nombre_occurences}.

    Example:
        >>> compter_lettres("Ba ba!")
        {'B': 2, 'A': 2}
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def obtenir_lettre_la_plus_frequente(texte):
    """
    Trouve la lettre qui revient le plus souvent dans le texte.
    
    Astuce : Vous pouvez utiliser votre fonction `compter_lettres`.
    Si le texte ne contient aucune lettre, retourner None.

    Args:
        texte (str): Le texte à analyser.

    Returns:
        str: La lettre la plus fréquente (ou None).

    Example:
        >>> obtenir_lettre_la_plus_frequente("Ba ba!")
        'B'  # (ou 'A', en cas d'égalité le premier trouvé suffit)
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def calculer_similitude(texte1, texte2):
    """
    Calcule le pourcentage de ressemblance entre deux textes.
    
    Algorithme :
    1. Comparer les caractères à la même position (index 0 avec 0, 1 avec 1...).
    2. Compter le nombre de correspondances exactes.
    3. Diviser ce nombre par la longueur du texte le plus long.
    
    Note : Si l'un des textes est vide, le score est 0.0.

    Args:
        texte1 (str): Premier texte.
        texte2 (str): Second texte.

    Returns:
        float: Un score entre 0.0 (différents) et 1.0 (identiques).

    Example:
        >>> calculer_similitude("CHAT", "CH")
        0.5  # 2 lettres communes ("CH") divisé par max length (4)
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def detecter_langue(texte):
    """
    Devine la langue du texte (Français ou Anglais) par analyse statistique simple.

    Algorithme de scoring :
    1. Convertir le texte en majuscules.
    2. Calculer le score Anglais (score_en) en additionnant le nombre d'occurrences de :
       - La lettre 'W'
       - La lettre 'Y'
       - La séquence 'TH'
    3. Calculer le score Français (score_fr) en additionnant le nombre d'occurrences de :
       - La lettre 'E'
       - La lettre 'É'
    4. Comparer les scores :
       - Si score_en > score_fr : Retourner 'EN'
       - Sinon (ou en cas d'égalité) : Retourner 'FR'

    Args:
        texte (str): Le texte à analyser.

    Returns:
        str: 'EN' pour Anglais, 'FR' pour Français.

    Example:
        >>> detecter_langue("Why do we wait")
        'EN'
        >>> detecter_langue("Le week-end en kayak")
        'FR' # Car beaucoup de 'E', même si 'W, Y, K' présents.
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def est_palindrome(texte):
    """
    Vérifie si le texte est un palindrome (se lit pareil dans les deux sens).
    
    Règles de nettoyage avant vérification :
    - Ne garder que les lettres (pas d'espace, pas de ponctuation).
    - Ignorer la casse (tout en majuscule).
    
    Exemple : "Laval" -> "LAVAL" (Vrai)

    Args:
        texte (str): Le mot ou la phrase.

    Returns:
        bool: True si c'est un palindrome, False sinon.

    Example:
        >>> est_palindrome("Esope reste ici et se repose")
        True
    """
    return NotImplemented