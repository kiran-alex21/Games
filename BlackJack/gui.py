import pygame
from main import BlackjackGame

# ---------- Setup ----------
pygame.init()
# TODO: set WIDTH and HEIGHT constants
# TODO: create the screen with pygame.display.set_mode((WIDTH, HEIGHT))
# TODO: set the window title with pygame.display.set_caption()
# TODO: create a clock with pygame.time.Clock() (used to cap the frame rate)
# TODO: create a font with pygame.font.SysFont() or pygame.font.Font(None, size)

# ---------- Colours ----------
# TODO: define a background colour as an RGB tuple, e.g. BG_COLOUR = (20, 90, 50)
# TODO: define a button colour and a text colour the same way

# ---------- Button rectangles ----------
# TODO: create a pygame.Rect for the Hit button (x, y, width, height)
# TODO: create a pygame.Rect for the Stand button
# TODO: create a pygame.Rect for the Play Again button (only shown at game over)

# ---------- Game state ----------
game = BlackjackGame()
state = "dealing"  # one of: "dealing", "player_turn", "dealer_turn", "game_over"
winner = None


def start_new_round():
    global state, winner
    # TODO: create a new Deck, assign it to game.deck, and shuffle it
    # TODO: create new Hand instances for game.player_hand and game.dealer_hand
    # TODO: deal 2 cards each to the player and dealer to start
    # TODO: reset winner to None
    # TODO: set state to "player_turn"
    pass


def draw_hand(hand, x, y):
    # TODO: loop through hand.cards
    # TODO: for each card, build a short label string from card.rank and card.suit
    # TODO: render that label with the font (font.render())
    # TODO: blit the rendered text onto the screen, offsetting x (or y) for each card
    #       so the cards don't overlap
    pass


def draw_buttons():
    # TODO: if state is "player_turn", draw the Hit and Stand button rectangles
    #       and render their labels ("Hit" / "Stand") on top of each
    # TODO: if state is "game_over", draw the Play Again button rectangle
    #       and render its label on top
    pass


def draw_text(text, x, y):
    # TODO: render the given text with the font
    # TODO: blit it onto the screen at the given position
    pass


start_new_round()  # TODO: uncomment once start_new_round() is implemented, to deal the first hand

# ---------- Main loop ----------
running = True
while running:
    # TODO: fill the screen with the background colour (screen.fill(BG_COLOUR))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "player_turn":
                # TODO: if hit_button_rect.collidepoint(event.pos):
                #           call game.player_hit()
                #           if game.player_turn_over(): set state to "dealer_turn"
                # TODO: elif stand_button_rect.collidepoint(event.pos):
                #           set state to "dealer_turn"
                pass
            elif state == "game_over":
                # TODO: if play_again_button_rect.collidepoint(event.pos):
                #           call start_new_round()
                pass

    if state == "dealer_turn":
        # TODO: call game.dealer_turn()
        # TODO: call game.resolve_round() and store the result in winner
        # TODO: set state to "game_over"
        pass

    # TODO: call draw_hand() for the player's hand (e.g. bottom of screen)
    # TODO: call draw_hand() for the dealer's hand (e.g. top of screen)
    # TODO: call draw_buttons()
    # TODO: if state is "game_over", call draw_text() to show the winner message

    # TODO: call pygame.display.flip() to update the display
    # TODO: call clock.tick(60) to cap the frame rate at 60 FPS

pygame.quit()