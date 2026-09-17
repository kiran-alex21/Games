# Implement Deck.shuffle and deal_card
- Fill Deck.cards with all 52 Card objects in __init__ (13 ranks x 4 suits)
- Write shuffle() using random.shuffle, 
- Write deal_card() to pop and return the last card from the list.

# Implement Hand.add_card
- add_card() should append a Card to self.cards.

# Implement Hand.get_total with ace logic and is_bust()
- get_total() is the trickiest function — comeplete and test it on its own with a few hands before moving on.
Sum the values of all cards, treating aces as 11 by default
then subtract 10 for each ace as needed while the total is over 21.
- is_bust() should call get_total() and return True if it's over 21


# Test Card, Deck, and Hand in isolation
- Write a few throwaway print statements or a tiny test script:
create a deck, shuffle it, deal a few cards into a hand, and print the total.
- Confirm ace handling works (e.g. Ace + King = 21, Ace + Ace + 9 = 21) before touching the game logic.

# Implement BlackjackGame.player_turn
This should follow the player-turn flowchart directly.
- Loop asking the player to hit or stand.
- On hit, deal a card into player_hand and check is_bust()
- On stand, exit the loop.

# Implement BlackjackGame.dealer_turn
- Loop dealing cards into dealer_hand while get_total() is under 17.
No decisions needed here — it's a fixed rule, so no user input.

# Implement BlackjackGame.resolve_round
follow the resolution flowchart (player wins, dealer wins, or push).
- Check for busts first,
- Compare player_hand.get_total() and dealer_hand.get_total() to decide the winner

# Implement BlackjackGame.play_round and test end-to-end
Tie everything together:
- set up deck and hands,
- deal initial cards,
- call player_turn(), dealer_turn(), and resolve_round() in sequence,
- print the result.

Play a few full rounds in the terminal before starting the pygame visuals.