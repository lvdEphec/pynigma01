# config.py

PADDING = """


# -------------------------------------------------------------------------
# ESPACE TAMPON POUR LIMITER LES RISQUES DE CONFLIT
# -------------------------------------------------------------------------


"""

# L'en-tête commun à tous les fichiers de tests
TEST_HEADER = """
import pytest
import string
from src import code_cesar, code_substitution, analyse_frequence, utilitaires

def check(valeur):
    \"\"\"Si la valeur est NotImplemented, on skip. Sinon on retourne la valeur.\"\"\"
    if valeur is NotImplemented:
        pytest.skip("Fonction à implémenter")
    return valeur
"""