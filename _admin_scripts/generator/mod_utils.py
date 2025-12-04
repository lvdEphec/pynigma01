from config import PADDING, TEST_HEADER

# =============================================================================
# 1. TESTS UNITAIRES (RIGOUREUX)
# =============================================================================
TESTS = TEST_HEADER + """
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
"""

# =============================================================================
# 2. SQUELETTE ETUDIANT (Specs précises)
# =============================================================================
STUDENT = f"""
import random
import string

def generer_mot_de_passe(longueur):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def formater_en_blocs(texte, taille):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def compter_mots(texte):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def est_mot_de_passe_fort(mdp):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def masquer_texte(texte):
    \"\"\"
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
    \"\"\"
    return NotImplemented
"""

# =============================================================================
# 3. SOLUTION PROFESSEUR
# =============================================================================
SOLUTION = f"""
import random
import string

def generer_mot_de_passe(longueur):
    # Sécurité : on force une taille min de 8 même si demandé moins (optionnel mais bonne pratique)
    if longueur < 8: longueur = 8
    
    # Construction du pool de caractères
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    
    # Génération
    return "".join(random.choice(caracteres) for _ in range(longueur))
{PADDING}
def formater_en_blocs(texte, taille):
    morceaux = []
    # On itère avec un pas de 'taille'
    for i in range(0, len(texte), taille):
        morceaux.append(texte[i:i+taille])
    return " ".join(morceaux)
{PADDING}
def compter_mots(texte):
    # .split() par défaut gère parfaitement les espaces multiples
    return len(texte.split())
{PADDING}
def est_mot_de_passe_fort(mdp):
    if len(mdp) < 8:
        return False
    
    # On vérifie chaque critère
    a_majuscule = any(c.isupper() for c in mdp)
    a_minuscule = any(c.islower() for c in mdp)
    a_chiffre = any(c.isdigit() for c in mdp)
    
    return a_majuscule and a_minuscule and a_chiffre
{PADDING}
def masquer_texte(texte):
    if len(texte) <= 2:
        return texte
    
    nb_etoiles = len(texte) - 2
    return "*" * nb_etoiles + texte[-2:]
"""