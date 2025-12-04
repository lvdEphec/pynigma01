from config import PADDING, TEST_HEADER

# =============================================================================
# 1. TESTS UNITAIRES (RIGOUREUX & PIÈGES)
# =============================================================================
TESTS = TEST_HEADER + """
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

def test_obtenir_frequente_texte_vide():
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
"""

# =============================================================================
# 2. SQUELETTE ETUDIANT (Specs précises)
# =============================================================================
STUDENT = f"""
def compter_lettres(texte):
    \"\"\"
    Compte le nombre d'apparitions de chaque lettre dans le texte.
    
    Règles :
    - Ignorer les espaces, chiffres et caractères spéciaux.
    - Convertir tout en majuscules avant de compter.

    Args:
        texte (str): Le texte à analyser.

    Returns:
        dict: Un dictionnaire {{'LETTRE': nombre_occurences}}.

    Example:
        >>> compter_lettres("Ba ba!")
        {{'B': 2, 'A': 2}}
    \"\"\"
    return NotImplemented
{PADDING}
def obtenir_lettre_la_plus_frequente(texte):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def calculer_similitude(texte1, texte2):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def detecter_langue(texte):
    \"\"\"
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
    \"\"\"
    return NotImplemented
{PADDING}
def est_palindrome(texte):
    \"\"\"
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
    \"\"\"
    return NotImplemented
"""

# =============================================================================
# 3. SOLUTION PROFESSEUR
# =============================================================================
SOLUTION = f"""
def compter_lettres(texte):
    compteur = {{}}
    for char in texte.upper():
        if char.isalpha() and char.isascii():
            # .get(cle, 0) renvoie la valeur actuelle ou 0 si pas encore présent
            compteur[char] = compteur.get(char, 0) + 1
    return compteur
{PADDING}
def obtenir_lettre_la_plus_frequente(texte):
    comptes = compter_lettres(texte)
    if not comptes:
        return None
    # max() avec l'argument 'key' permet de trier selon les valeurs du dico
    return max(comptes, key=comptes.get)
{PADDING}
def calculer_similitude(texte1, texte2):
    if not texte1 or not texte2:
        return 0.0
    
    longueur_max = max(len(texte1), len(texte2))
    longueur_min = min(len(texte1), len(texte2))
    
    correspondances = 0
    # On itère jusqu'à la fin du mot le plus court pour éviter "IndexError"
    for i in range(longueur_min):
        if texte1[i] == texte2[i]:
            correspondances += 1
            
    return correspondances / longueur_max
{PADDING}
def detecter_langue(texte):
    texte = texte.upper()
    score_en = texte.count('W') + texte.count('Y') + texte.count('TH')
    score_fr = texte.count('E') + texte.count('É')
    
    if score_en > score_fr:
        return "EN"
    return "FR"
{PADDING}
def est_palindrome(texte):
    # Liste en compréhension pour garder que les lettres
    lettres = [c for c in texte.upper() if c.isalpha() and c.isascii()]
    texte_propre = "".join(lettres)
    
    # Comparaison avec l'inverse ([::-1])
    return texte_propre == texte_propre[::-1]
"""