# 🤖 Rule-Based AI Chatbot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Library](https://img.shields.io/badge/cli-rich-magenta.svg)](https://rich.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sleek, robust, and interactive **Rule-Based AI Chatbot** with a premium command-line interface built in Python. Designed for the DecodeLabs internship, this application features beautiful visual panel rendering, intelligent keyword-response routing, and a built-in safety guardrail system.

---

## 🚀 Features

*   **✨ Premium Command-Line UI**: Powered by the `rich` library to deliver stunning colored panels, styled prompts, and visually distinct outputs.
*   **🧠 Smart Pattern-Matching**: Resolves 10+ predefined keyword-response pairs seamlessly.
*   **🛡️ Built-in Content Guardrails**: Automatically detects and handles forbidden words or phrases, declining unsafe inputs gracefully with localized visual indicators.
*   **🔌 Graceful Exit Handling**: Fully supports typing `quit` or using `Ctrl+C` (KeyboardInterrupt) to exit safely.

---

## ⚙️ Installation & Setup

Ensure you have **Python 3.8+** installed on your system. Follow these steps to set up and run the chatbot:

### 1. Clone or Open the Repository
```bash
cd Project-1-decodelabs-internship
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Create the environment
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
This project utilizes the `rich` package to render its premium terminal interface. Install it using `pip`:
```bash
pip install rich
```

### 4. Run the Chatbot
```bash
python rule-based-ai-chabot.py
```

---

## 💬 How to Interact

Simply start typing queries in the terminal when prompted with `You : `. The chatbot will respond within stylized panels.

## 🛡️ Safety Guardrails (Forbidden Content)

To ensure a safe user experience, the chatbot implements a **Guard Filter**. If the user's input contains any of the following safety-violating words, the chatbot will block the request and display a safety warning:

```txt
bomb, kill, attack, murder, nuclear, weapon, terrorist, death, suicide, assassination, crime, fuck you
```

### Example Safety Response:
```txt
┌── Chatbot ──────────────────────────────────────────┐
│ Sorry, but I can't help you with that.              │
└─────────────────────────────────────────────────────┘
```

---

## 🛠️ Codebase Structure

```bash
Project-1-decodelabs-internship/
│
├── rule-based-ai-chabot.py   # Main entry point containing chatbot logic & UI
└── README.md                 # Project documentation and setup guide
```
---

## 📝 License

Distributed under the MIT License. See [LICENSE](https://opensource.org/licenses/MIT) for more information.
