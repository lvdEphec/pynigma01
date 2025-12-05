# 🕵️‍♂️ Projet Py-Nigma

> ⚠️ **ÉTUDIANTS :** Toutes les consignes, les règles et le déroulement se trouvent dans le document PDF **"Énoncé du TP"**. Merci de le lire attentivement avant de commencer.

---
<br>
<br>
<br>

## 🛑 ZONE RÉSERVÉE PROFESSEUR (Checklist Démarrage)

*À suivre pas à pas pour initialiser un nouveau groupe.*

### 1. Création du Dépôt
- [ ] Sur ce dépôt Master, cliquer sur **Use this template** > **Create a new repository**.
- [ ] Nommer : `pynigma-groupe-X` (Public).

### 2. Configuration du Projet (Kanban)
- [ ] Onglet **Projects** > **New Project** > **Kanban**.
- [ ] **ACTIVER L'AUTO-ADD** :
    1. Cliquer sur **Workflows** (icône en haut à droite).
    2. Dans la liste à gauche
    3. Vérifier **Auto-add** et le lien vec le bon **repo**

### 3. Lancement des Scripts (Onglet Actions)
*Allez dans l'onglet **Actions** du nouveau repo.*

- [ ] **Lancer "🪄 1. Admin - Créer Tâches (Auto)"** :
(ou bien à la place créer les issues manuellement) :
    - Cliquer sur *Run workflow*.
    - *Vérifier que les 20 cartes apparaissent dans la colonne "Todo" du Projet.*

- [ ] **Lancer "🛡️ 2. Admin - Protéger (puis SUPPRIMER...)"** 
(ou bien à la place protéger la branche main dans les options) :
    - Cliquer sur *Run workflow*.
    - Coller le Token Admin (PAT).
    - *Une fois fini (Vert), supprimer le "Run" de l'historique.

### 4. Démo Live
- [ ] Rappeler fork, origin, upstream.
- [ ] Démo de l'appli (objectif) + montrer fonctionnalités manquantes.
- [ ] Lancer les tests unitaires pour les montrer
---
- [ ] Montrer Kanban, demander dans issues que chacun s'assigne une tâche avec /assign dans les commentaires.
- [ ] Mettre les tâches assignées dans In Progress.
---
- [ ] Parcourir les étapes de l'énoncé. Rappeler de ne pas oublier d'étape. Rappeler de ne coder qu'une fonction à la fois. (Ils peuvent changer si besoin d'une autre.)
- [ ] Leur dire de prévenir lorsque la PR est faite.
- [ ] Valider l'entrée dans le workflow pour lancer les tests, et merger dans le main si tout est bon.
- [ ] Montrer les logs du pipe.
---
- [ ] Ceux qui sont à l'aise peuvent foncer dans l'exercice. Les autres peuvent regarder l'exemple et faire l'exercice en parallèle. (Possibilité aussi d'un premier exemple rapide, puis un exemple en parallèle.)
- [ ] Pour l'exemple avec un_pour_prof, partir du clone. (Pour le fork il faudrait alors un autre compte.)
- [ ] Vérifier à chaque étape qu'ils comprennent la situation et ce qu'il faut faire.
- [ ] Bon moment pour montrer Ctrl-t et alt-flèches (vs code win)
- [ ] Lancer le code coverage pour le montrer
- [ ] Récupérer le code soumis pour voir ce qui tourne dans l'application