# Connect Four AI — Lightweight Flutter & Flask Application

This repository contains the core logic for a **Connect Four (Puissance 4)** application powered by a **Python Flask backend** with an **AI opponent using Minimax with Alpha-Beta Pruning**.

> **Note on Repository Structure:**  
> Standard Flutter auto-generated build files and platform folders (`android/`, `ios/`, `build/`, `.dart_tool/`) were excluded to keep the repository lightweight and efficient. Only the essential source code files (`/lib` for Flutter UI and core `.py` backend scripts) are included[cite: 5].

---

## 🛠️ Features

- **Core Game Engine:** Minimax algorithm with Alpha-Beta Pruning for intelligent AI moves.
- **Flask REST API Backend:** Efficient client-server communication via HTTP endpoints.
- **Lightweight Flutter Frontend:** Essential Dart files handling UI navigation, game views, and API calls[cite: 5].

---

## 📂 Repository Structure

```text
.
├── play.py                 # Flask server handling API routes and game loop[cite: 5]
├── project.py              # ConnectFourBoard engine (Minimax & Alpha-Beta Pruning)[cite: 5]
└── lib/                    # Essential Flutter source code[cite: 5]
    ├── welcom.dart         # Welcome screen UI[cite: 5]
    ├── main.dart           # App entry point and primary game interface[cite: 5]
    └── main2.dart          # Secondary game mode interface[cite: 5]
```

---

## 📋 How to Run the Project

### 1. Start the Flask Backend (Python)

1. Install Python dependencies:
   ```bash
   pip install flask numpy
   ```
2. Launch the Flask API server:
   ```bash
   python play.py
   ```

### 2. Run the Flutter Frontend

1. Generate standard Flutter project files in your workspace:
   ```bash
   flutter create connect_four_app
   ```
2. Replace or copy the provided `lib/` directory contents (`main.dart`, `main2.dart`, `welcom.dart`) into your new project's `lib/` folder[cite: 5].
3. Run the application:
   ```bash
   flutter run
   ```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
