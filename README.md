# Connect Four AI — Flutter Application & Flask API

Une application complète multiplateforme du jeu **Puissance 4 (Connect Four)** développée avec **Flutter**, alimentée par un backend **Flask** en Python[cite: 4]. L'IA adverse prend ses décisions de jeu grâce à l'algorithme **Minimax optimisé par l'élagage Alpha-Bêta (Alpha-Beta Pruning)**.

---

## 🛠️ Fonctionnalités

- **Interface Multiplateforme (Flutter) :** Disponible sur Android, iOS, Web, Windows, macOS et Linux[cite: 4].
- **IA Intelligente (Minimax + Élagage Alpha-Bêta) :** Évaluation heuristique du plateau pour anticiper les coups du joueur et bloquer ses combinaisons gagnantes.
- **Mode IA vs IA / Humain vs IA :** Support pour les affrontements entre un joueur humain et l'IA ou simulations de parties IA contre IA.
- **API RESTful (Flask) :** Communication fluide via HTTP JSON entre l'application client et le serveur backend.
- **Effets Sonores & Audio :** Intégration d'éléments audio pour enrichir l'expérience de jeu.

---

## 📂 Structure du Dépôt

```text
.
├── lib/                  # Code source principal de l'application Flutter[cite: 4]
├── Audio/                # Fichiers audio et effets sonores du jeu[cite: 4]
├── android/              # Fichiers de configuration pour Android[cite: 4]
├── ios/                  # Fichiers de configuration pour iOS[cite: 4]
├── web/                  # Fichiers de configuration pour le Web[cite: 4]
├── windows/              # Fichiers de configuration pour Windows[cite: 4]
├── main.py               # Serveur Flask / API RESTful
├── project.py            # Moteur de jeu ConnectFourBoard (Minimax & Alpha-Beta)
├── pubspec.yaml          # Dépendances du projet Flutter[cite: 4]
└── README.md             # Documentation du projet[cite: 4]
```

---

## 📡 Endpoints de l'API Flask

Le serveur tourne par défaut sur `http://localhost:5000` :

| Méthode | Route | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Vérifie l'état de l'API. |
| `POST` | `/make_move` | Envoie le coup du joueur humain et déclenche la réponse de l'IA. |
| `POST` | `/make_move2` | Déclenche un tour entre deux algorithmes d'IA. |
| `GET` | `/get_board` | Récupère l'état actuel de la grille 6x7 sous forme de matrice JSON. |
| `GET` | `/restart` | Réinitialise la grille de jeu. |
| `GET` | `/game_over` | Vérifie si la partie est terminée (victoire, défaite ou égalité). |

---

## 📋 Prérequis & Installation

### 1. Démarrer le Backend Flask (Python)

1. Installez les dépendances Python nécessaires :
   ```bash
   pip install flask numpy
   ```
2. Lancez le serveur Flask :
   ```bash
   python main.py
   ```

### 2. Lancer l'Application Client (Flutter)

1. Assurez-vous d'avoir installé [Flutter SDK](https://flutter.dev/docs/get-started/install).
2. Récupérez les packages et dépendances :
   ```bash
   flutter pub get
   ```
3. Exécutez l'application sur la plateforme de votre choix :
   ```bash
   flutter run
   ```

---

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE) - libre d'utilisation et de modification.
