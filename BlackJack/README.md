# Blackjack

A simple, no-betting Blackjack game built in Python, with a Pygame GUI and a console fallback that share the same game logic.

## Features
- Standard blackjack rules: dealer hits until 17, aces count as 1 or 11
- Full deck, deal, hit/stand, and win/lose/push resolution
- Pygame GUI with clickable Hit / Stand / Play Again buttons
- Console version (`main.py` run directly) for quick testing of the game logic without launching the GUI

## Requirements
- Python 3
- [pygame-ce](https://pyga.me/) — see `requirements.txt`

Install with:
```
pip install -r requirements.txt
```

## Running the game

**GUI version:**
```
python gui.py
```

**Console version:**
```
python main.py
```

## Project structure
- `main.py` — game logic: `Card`, `Deck`, `Hand`, and `BlackjackGame` classes
- `gui.py` — Pygame front end, imports and drives `BlackjackGame`
