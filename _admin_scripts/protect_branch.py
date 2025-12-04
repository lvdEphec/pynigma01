import os
import json
import subprocess

# --- CONFIGURATION ---
BRANCH = "main"
JOB_NAME = "test"  # Le nom exact du job dans le fichier .yml

def get_current_repo():
    """Tente de récupérer le nom du repo via git config."""
    try:
        url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"]).decode().strip()
        # Nettoyage de l'URL pour garder user/repo
        if "github.com" in url:
            return url.split("github.com/")[-1].replace(".git", "")
    except:
        return None

def protect_branch():
    target_repo = get_current_repo()
    
    if not target_repo:
        print("❌ Impossible de détecter le dépôt. Vérifiez que vous êtes dans un dossier Git.")
        return

    print(f"🛡️  Application de la protection sur '{BRANCH}' pour {target_repo}...")

    # Configuration de la protection (Payload JSON)
    rules = {
        "required_status_checks": {
            "strict": True,
            "contexts": [JOB_NAME]
        },
        "enforce_admins": False,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 0
        },
        "restrictions": None,
        "allow_force_pushes": False,
        "allow_deletions": False
    }

    json_rules = json.dumps(rules)

    # Commande GitHub CLI
    cmd = [
        "gh", "api", 
        f"/repos/{target_repo}/branches/{BRANCH}/protection",
        "--method", "PUT",
        "--input", "-"
    ]

    try:
        # On envoie le JSON via l'entrée standard
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=json_rules.encode())

        if process.returncode == 0:
            print("✅ Succès ! La branche est protégée.")
            print(f"   - PR obligatoire : OUI")
            print(f"   - Tests obligatoires : OUI ({JOB_NAME})")
        else:
            print("❌ Erreur lors de la configuration :")
            print(stderr.decode())
            print("💡 Astuce : Êtes-vous admin du repo ? Avez-vous fait 'gh auth login' ?")

    except FileNotFoundError:
        print("❌ Erreur : GitHub CLI ('gh') n'est pas installé.")

if __name__ == "__main__":
    protect_branch()