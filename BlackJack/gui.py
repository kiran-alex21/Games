import pygame
from main import BlackjackGame

# ---------- Setup ----------
pygame.init()
# set WIDTH and HEIGHT constants
WIDTH, HEIGHT = 820, 240
# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set the window title
pygame.display.set_caption("BlackJack 1.0")
# create a clock with (used to cap the frame rate)
clock = pygame.time.Clock()
# create a font
font = pygame.font.SysFont("Atkinson Hyperlegible Next", 18)

# ---------- Colours ----------
# define a background colour (as an RGB tuple)
BG_COLOUR = (27, 24, 94)
# define a button colour
BUTTON_COLOUR = (77, 175, 184)
# define a text colour
TEXT_COLOUR = (5, 5, 5)
# define a card colour


# ---------- Button rectangles ----------
# create the Hit button
hit_button = pygame.Rect(475, 160, 130, 40)
# create the Stand button
stand_button = pygame.Rect(625, 160, 130, 40)
# create the Play Again button (only shown at game over)
play_again_button = pygame.Rect(320, 160, 180, 55)


# ---------- Game state ----------
game = BlackjackGame()
state = "dealing"  # one of: "dealing", "player_turn", "dealer_turn", "game_over"
winner = None


def start_new_round():
    global game, state, winner
    winner = None # reset winner to None
    game.start_round() # initiate round starting logic
    state = "player_turn" # set state to "player_turn"


def draw_hand(hand, x, y):
    for i, card in enumerate(hand):  # enumerate gives us the index too
        CARD_W, CARD_H = 80, 100
        card_rect = pygame.Rect((x + i * 90), y, CARD_W, CARD_H) # set card background
        pygame.draw.rect(screen, BUTTON_COLOUR, card_rect) # draw the card background

        # create labels for each card
        rank_text = font.render(card.rank, True, TEXT_COLOUR)
        of_text = font.render("of", True, TEXT_COLOUR)
        suit_text = font.render(card.suit, True, TEXT_COLOUR)
        # get co-ords for each label
        rank_rect = rank_text.get_rect(center=(card_rect.centerx, card_rect.top + 20))
        of_rect = of_text.get_rect(center=(card_rect.centerx, card_rect.top + 45))
        suit_rect = suit_text.get_rect(center=(card_rect.centerx, card_rect.top + 70))
        # add labels to screen
        screen.blit(rank_text, rank_rect)
        screen.blit(of_text, of_rect)
        screen.blit(suit_text, suit_rect)

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
    # fill the screen with the background colour
    screen.fill(BG_COLOUR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "player_turn":
                # TODO: if hit_button.collidepoint(event.pos):
                #           call game.player_hit()
                #           if game.player_turn_over(): set state to "dealer_turn"
                # TODO: elif stand_button.collidepoint(event.pos):
                #           set state to "dealer_turn"
                pass
            elif state == "game_over":
                # TODO: if play_again_button.collidepoint(event.pos):
                #           call start_new_round()
                pass

    if state == "dealer_turn":
        # TODO: call game.dealer_turn()
        # TODO: call game.resolve_round() and store the result in winner
        # TODO: set state to "game_over"
        pass

    # card row starting positions
    dealer_hand = game.dealer_hand.cards
    player_hand = game.player_hand.cards
    dealer_hand_x, dealer_hand_y = 30, 50
    player_hand_x, player_hand_y = 440, 50
    draw_hand(player_hand, player_hand_x, player_hand_y) # call draw_hand() for the player's hand
    draw_hand(dealer_hand, dealer_hand_x, dealer_hand_y) # call draw_hand() for the dealer's hand
    # TODO: call draw_buttons()
    # TODO: if state is "game_over", call draw_text() to show the winner message

    pygame.display.flip() # update the display
    clock.tick(60) # cap the frame rate at 60 FPS

pygame.quit()