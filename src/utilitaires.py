import random
import string

def generer_mot_de_passe(longueur):
    """
    Génère un mot de passe aléatoire robuste.
    
    Contraintes obligatoires :
    Le mot de passe doit piocher des caractères au hasard parmi ces 4 catégories :
    1. Lettres majuscules (A-Z)
    2. Lettres minuscules (a-z)
    3. Chiffres (0-9)
    4. Caractères spéciaux (!@#$%)

    Astuce : Utilisez le module `string` et `random.choice`.

    Args:
        longueur (int): La taille souhaitée du mot de passe.

    Returns:
        str: Le mot de passe généré.

    Example:
        >>> generer_mot_de_passe(10)
        'aB1!eR5*xP'
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def formater_en_blocs(texte, taille):
    """
    Découpe une chaîne en blocs de N caractères séparés par des espaces.
    Utile pour rendre lisible une clé ou un texte chiffré.

    Args:
        texte (str): La chaîne brute.
        taille (int): La taille de chaque bloc.

    Returns:
        str: La chaîne formatée (ex: "BON JOU R").

    Example:
        >>> formater_en_blocs("ABCDEF", 2)
        'AB CD EF'
        >>> formater_en_blocs("12345", 2)
        '12 34 5'
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def compter_mots(texte):
    """
    Compte le nombre de mots dans une phrase.
    
    Règles :
    - Les mots sont séparés par un ou plusieurs espaces.
    - Les espaces multiples ne doivent pas compter comme des mots vides.

    Args:
        texte (str): La phrase à analyser.

    Returns:
        int: Le nombre de mots.

    Example:
        >>> compter_mots("Bonjour le monde")
        3
        >>> compter_mots("Un   deux")
        2
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def est_mot_de_passe_fort(mdp):
    """
    Vérifie la sécurité d'un mot de passe selon des critères stricts.
    
    Critères à valider (ET logique) :
    1. Longueur >= 8 caractères
    2. Contient au moins 1 chiffre
    3. Contient au moins 1 lettre majuscule
    4. Contient au moins 1 lettre minuscule

    Args:
        mdp (str): Le mot de passe à tester.

    Returns:
        bool: True si le mot de passe respecte tous les critères, False sinon.

    Example:
        >>> est_mot_de_passe_fort("Admin123")
        True
        >>> est_mot_de_passe_fort("admin123")
        False
    """
    return NotImplemented



# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def masquer_texte(texte):
    """
    Masque un secret (ex: numéro de carte) pour l'affichage.
    
    Règle :
    - Remplacer tous les caractères par une étoile '*'
    - SAUF les 2 derniers caractères qui restent visibles.
    - Cas particulier : Si le texte a 2 caractères ou moins, on ne masque rien (on renvoie tel quel).

    Args:
        texte (str): Le secret.

    Returns:
        str: Le texte masqué.

    Example:
        >>> masquer_texte("123456")
        '****56'
        >>> masquer_texte("Ok")
        'Ok'
    """
    return NotImplemented




# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------



def un_pour_prof():
    """
    retourne 1  
    """
    return NotImplemented