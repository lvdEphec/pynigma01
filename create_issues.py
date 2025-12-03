import os
import time

# Liste des tâches : (Titre de l'issue, Description complète/Docstring)
TASKS = {
    "Implémenter code_lettre (César)": """Décale une SEULE lettre majuscule en utilisant le code César.
Si le caractère n'est pas une lettre, il est retourné inchangé.

Args:
    lettre (str): Le caractère à chiffrer (ex: 'A').
    decalage (int): Le nombre de positions à décaler (ex: 3).

Returns:
    str: La lettre chiffrée en majuscule.

Example:
    >>> code_lettre('A', 3)
    'D'""",

    "Implémenter chiffrer_cesar": """Chiffre un message complet avec le code César.
Utilise la fonction code_lettre pour chaque caractère.

Args:
    message (str): Le texte à chiffrer.
    decalage (int): Le décalage à appliquer.

Returns:
    str: Le message chiffré.

Example:
    >>> chiffrer_cesar("HAL", 1)
    'IBM'""",

    "Implémenter dechiffrer_cesar": """Déchiffre un message codé avec César.
Astuce : C'est comme chiffrer avec un décalage négatif.

Args:
    message (str): Le texte chiffré.
    decalage (int): Le décalage utilisé pour le chiffrement.

Returns:
    str: Le message original en clair.

Example:
    >>> dechiffrer_cesar("IBM", 1)
    'HAL'""",

    "Implémenter est_lettre": """Vérifie si un caractère est une lettre de l'alphabet (A-Z ou a-z).
ATTENTION : On ne considère que les lettres sans accents (ASCII) pour cet exercice.

Args:
    char (str): Le caractère à tester.

Returns:
    bool: True si c'est une lettre, False sinon.

Example:
    >>> est_lettre('A')
    True""",

    "Implémenter nettoyer_accents": """Prépare le texte pour le chiffrement.

Règles :
1. Remplacer les lettres accentuées par leur version sans accent (é->e, à->a).
2. Tout mettre en MAJUSCULES.

Utilisez ce dictionnaire :
accs = {'É':'E', 'È':'E', 'Ê':'E', 'À':'A', 'Ù':'U', 'Ç':'C', 'Ô':'O', 'Ò':'O', 'Î':'I', 'Ï':'I'}

Args:
    texte (str): Texte brut.

Returns:
    str: Texte nettoyé.""",

    "Implémenter code_miroir (Subst)": """Applique le chiffrement miroir (Atbash).
L'alphabet est inversé : A<->Z, B<->Y, C<->X...

Args:
    message (str): Le texte à inverser.

Returns:
    str: Le texte chiffré.

Example:
    >>> code_miroir("AZ")
    'ZA'""",

    "Implémenter vers_leet_speak": """Transforme le texte en Leet Speak (remplacement par des chiffres).
Règles : E->3, A->4, T->7, I->1, O->0, S->5.

Args:
    message (str): Le texte original.

Returns:
    str: Le texte transformé.""",

    "Implémenter depuis_leet_speak": """Retrouve le texte original depuis du Leet Speak.
Inverse les règles : 3->E, 4->A...

Args:
    message (str): Le texte en Leet Speak.

Returns:
    str: Le texte lisible.""",

    "Implémenter chiffrer_vigenere": """Chiffre avec la méthode de Vigenère (Code César à clé variable).
La clé est répétée pour correspondre à la longueur du message.
Attention : La clé doit être nettoyée des espaces avant usage.

Args:
    message (str): Le texte à chiffrer.
    cle (str): La clé de chiffrement (ex: "MUSIQUE").

Returns:
    str: Le message chiffré.""",

    "Implémenter dechiffrer_vigenere": """Déchiffre un message Vigenère.
Même logique que le chiffrement, mais on soustrait le décalage.

Args:
    message (str): Le texte chiffré.
    cle (str): La clé utilisée.

Returns:
    str: Le message en clair.""",

    "Implémenter compter_lettres (Freq)": """Compte le nombre d'apparitions de chaque lettre.

Règles :
- Ignorer les espaces, chiffres et caractères spéciaux.
- Convertir tout en majuscules avant de compter.

Args:
    texte (str): Le texte à analyser.

Returns:
    dict: Un dictionnaire {'LETTRE': nombre}.""",

    "Implémenter obtenir_lettre_frequente": """Trouve la lettre qui revient le plus souvent dans le texte.

Astuce : Vous pouvez utiliser votre fonction `compter_lettres`.
Si le texte ne contient aucune lettre, retourner None.

Args:
    texte (str): Le texte à analyser.

Returns:
    str: La lettre la plus fréquente (ou None).""",

    "Implémenter calculer_similitude": """Calcule le pourcentage de ressemblance entre deux textes.

Algorithme :
1. Comparer les caractères à la même position.
2. Compter les correspondances exactes.
3. Diviser par la longueur du texte le plus long.

Args:
    texte1 (str): Premier texte.
    texte2 (str): Second texte.

Returns:
    float: Un score entre 0.0 et 1.0.""",

    "Implémenter detecter_langue": """Devine la langue du texte (Français ou Anglais).

Algorithme de scoring :
1. Convertir le texte en majuscules.
2. Score Anglais = somme des 'W', 'Y', 'TH'.
3. Score Français = somme des 'E', 'É'.
4. Si Score EN > Score FR : Retourner 'EN', Sinon 'FR'.

Returns:
    str: 'EN' ou 'FR'.""",

    "Implémenter est_palindrome": """Vérifie si le texte est un palindrome (se lit pareil dans les 2 sens).

Règles :
- Ne garder que les lettres (pas d'espace, pas de ponctuation).
- Ignorer la casse.

Example:
    >>> est_palindrome("Esope reste ici et se repose")
    True""",

    "Implémenter generer_mot_de_passe (Utils)": """Génère un mot de passe aléatoire robuste.
Doit contenir : Majuscules, minuscules, chiffres et caractères spéciaux (!@#$%).

Args:
    longueur (int): Taille du mot de passe.

Returns:
    str: Le mot de passe généré.""",

    "Implémenter formater_en_blocs": """Découpe une chaîne en blocs de N caractères séparés par des espaces.

Args:
    texte (str): La chaîne brute.
    taille (int): La taille de chaque bloc.

Returns:
    str: La chaîne formatée (ex: "BON JOU R").""",

    "Implémenter compter_mots": """Compte le nombre de mots dans une phrase.
Gère les espaces multiples (ne pas compter les vides).

Args:
    texte (str): La phrase à analyser.

Returns:
    int: Le nombre de mots.""",

    "Implémenter est_mot_de_passe_fort": """Vérifie la sécurité d'un mot de passe.
Critères : Min 8 caractères, 1 chiffre, 1 majuscule, 1 minuscule.

Args:
    mdp (str): Le mot de passe à tester.

Returns:
    bool: True si le mot de passe est fort.""",

    "Implémenter masquer_texte": """Masque un texte par des étoiles, sauf les 2 derniers caractères.
Si le texte est trop court (<= 2), on ne masque rien.

Args:
    texte (str): Le secret.

Returns:
    str: Le texte masqué."""
}

print(f"🚀 Lancement de la création de {len(TASKS)} issues sur GitHub...")
print("ℹ️  Assurez-vous d'avoir fait 'gh auth login' avant.")

counter = 1
for title, body in TASKS.items():
    # Échappement basique des guillemets pour la ligne de commande
    safe_body = body.replace('"', '\\"')
    
    # Commande GH
    cmd = f'gh issue create --title "{title}" --body "{safe_body}"'
    
    print(f"[{counter}/{len(TASKS)}] Création : {title}...")
    result = os.system(cmd)
    
    if result != 0:
        print("❌ Erreur lors de la création. Vérifiez votre connexion 'gh'.")
        break
        
    counter += 1
    # Petite pause pour ne pas se faire bloquer par l'API GitHub (Rate Limit)
    time.sleep(1)

print("\n✨ Terminé ! Toutes les tâches sont créées avec leurs spécifications.")