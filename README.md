# Tetris-game
# Tetris — Python × Pygame

A modern, object-oriented take on the classic Tetris puzzle game, built entirely with **Python 3** and **Pygame 2**.  
Created as a hands-on learning project after following [Clear Code’s tutorial](https://youtu.be/nF_crEtmpBo), then extended with cleaner OOP design, polished visuals, and extra features.

---

## Features
- **Fully playable**: seven tetrominoes, rotation, soft drop, lock delay, line clears, and score tracking.  
- **Object-Oriented Architecture**: separate classes for `Grid`, `Game`, and `UI` for maximum readability and easy future upgrades.  
- **Smooth animations** running at 60 FPS thanks to delta-time based updates.  
- **Clean codebase** (PEP 8 compliant, type-hinted) with docstrings and inline comments.  
- **Cross-platform**—works on Windows, macOS, and Linux with Python 3.8+.  

---

## Installation


# 1. Clone the repository
git clone https://github.com/your-username/tetris-pygame.git
cd tetris-pygame

# 2.  Create a virtual environment
python -m venv .venv && source .venv/bin/activate  # macOS/Linux
# For Windows: python -m venv .venv && .venv\Scripts\activate

# 3. Run the game
python main.py
