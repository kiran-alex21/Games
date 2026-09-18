# Python Logic

## Implement Deck.shuffle and deal_card
- Fill Deck.cards with all 52 Card objects in __init__ (13 ranks x 4 suits)
- Write shuffle() using random.shuffle, 
- Write deal_card() to pop and return the last card from the list.

## Implement Hand.add_card
- add_card() should append a Card to self.cards.

## Implement Hand.get_total with ace logic and is_bust()
- get_total() is the trickiest function
Sum the values of all cards, treating aces as 11 by default
comeplete and test it on its own with a few hands before moving on.
then subtract 10 for each ace as needed while the total is over 21.
- is_bust() should call get_total() and return True if it's over 21


## Test Card, Deck, and Hand in isolation
- Write a few throwaway print statements or a tiny test script:
create a deck, shuffle it, deal a few cards into a hand, and print the total.
- Confirm ace handling works (e.g. Ace + King = 21, Ace + Ace + 9 = 21) before touching the game logic.

## Implement BlackjackGame.player_turn
This should follow the player-turn flowchart directly.
- Loop asking the player to hit or stand.
- On hit, deal a card into player_hand and check is_bust()
- On stand, exit the loop.

## Implement BlackjackGame.dealer_turn
- Loop dealing cards into dealer_hand while get_total() is under 17.
No decisions needed here — it's a fixed rule, so no user input.

## Implement BlackjackGame.resolve_round
follow the resolution flowchart (player wins, dealer wins, or push).
- Check for busts first,
- Compare player_hand.get_total() and dealer_hand.get_total() to decide the winner

## Implement BlackjackGame.play_round and test end-to-end
Tie everything together:
- set up deck and hands,
- deal initial cards,
- call player_turn(), dealer_turn(), and resolve_round() in sequence,
- print the result.

Play a few full rounds in the terminal before starting the pygame visuals.

# Pygame GUI
## Helpful sites
- https://www.pygame.org/docs/
- https://www.geeksforgeeks.org/python/pygame-tutorial/

## Set up the window and game loop
- Set WIDTH, HEIGHT and create the screen with pygame.display.set_mode()
- Create a clock with pygame.time.Clock()
- Create a font with pygame.font.SysFont() or pygame.font.Font()
Get a blank window showing with the loop running before adding anything else.

## Define colours and button rectangles
- Define BG_COLOUR, button colour, and text colour as RGB tuples
- Create a pygame.Rect for the Hit button
- Create a pygame.Rect for the Stand button
- Create a pygame.Rect for the Play Again button (only shown at game over)

## Implement start_new_round()
- Create a new Deck, assign it to game.deck, and shuffle it
- Create new Hand instances for game.player_hand and game.dealer_hand
- Deal 2 cards each to the player and dealer
- Reset winner to None and set state to "player_turn"
Call this once before the main loop starts, so the first hand is already dealt.

## Implement draw_hand()
- Loop through hand.cards
- Build a short label from each card's rank and suit
- Render the label with the font, then blit it to the screen
Offset the position for each card so they don't overlap.

## Implement draw_buttons() and draw_text()
- draw_buttons(): draw Hit/Stand when state is "player_turn", Play Again when state is "game_over"
- Render each button's label on top of its rectangle
- draw_text(): render and blit a given string at a given position — used for the winner message

## Wire up player_turn() clicks (Hit / Stand)
This replaces the console version's while loop — the pygame loop now drives the turn one click at a time.
- On Hit: call game.player_hit(), then check game.player_turn_over()
- If the player busts, set state to "dealer_turn"
- On Stand: set state to "dealer_turn" directly

## Wire up the dealer's turn and resolution
- When state is "dealer_turn", call game.dealer_turn()
- Call game.resolve_round() and store the result in winner
- Set state to "game_over"
dealer_turn() and resolve_round() don't need any changes — they aren't blocking on input.

## Add the Play Again / game over screen
- In "game_over" state, draw_text() the winner message
- On Play Again click, call start_new_round() to reset state back to "player_turn"

## Test end-to-end
- Play a full round through the pygame window: deal, hit/stand, dealer turn, result, replay
- Confirm the console version (main.py run directly) still works unaffected

## Polish: card images and styling
- Swap the plain-text cards for card image files with pygame.image.load()
- Add hover effects on buttons
- Tidy up fonts, colours, and spacing