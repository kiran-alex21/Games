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
BG_COLOUR     = (58, 12, 20)     # #3A0C14
BUTTON_COLOUR = (212, 175, 55)   # #D4AF37
CARD_COLOUR   = (245, 242, 235)  # #F5F2EB
TEXT_COLOUR   = (30, 10, 10)     # #1E0A0A
RESULT_COLOUR = (245, 242, 235)  # #F5F2EB

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
    # TODO: if dealer only draw first card - hide second card until game over
    # TODO: add delay between drawing each card
    for i, card in enumerate(hand):  # enumerate gives us the index too
        CARD_W, CARD_H = 80, 100
        card_rect = pygame.Rect((x + i * 90), y, CARD_W, CARD_H) # set card background
        pygame.draw.rect(screen, CARD_COLOUR, card_rect) # draw the card background

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
    if state != "game_over": # if state is "player_turn"
        # draw the Hit and Stand button rectangles
        pygame.draw.rect(screen, BUTTON_COLOUR, hit_button)
        pygame.draw.rect(screen, BUTTON_COLOUR, stand_button)
        # render their labels ("Hit" / "Stand") on top of each
        hit_text = font.render("Hit", True, TEXT_COLOUR)
        stand_text = font.render("Stand", True, TEXT_COLOUR)
        hit_text_rect = hit_text.get_rect(center=hit_button.center)
        stand_text_rect = stand_text.get_rect(center=stand_button.center)
        screen.blit(hit_text, hit_text_rect)
        screen.blit(stand_text, stand_text_rect)
    if state == "game_over": # if state is "game_over"
        pygame.draw.rect(screen, BUTTON_COLOUR, play_again_button) # draw the Play Again button rectangle
        # render its label on top
        play_again_text = font.render("Play Again", True, TEXT_COLOUR)
        play_again_rect = play_again_text.get_rect(center = play_again_button.center)
        screen.blit(play_again_text, play_again_rect)


def draw_text(text_render, rect):
    screen.blit(text_render, rect) # blit it onto the screen at the given position


start_new_round()  # deal the first hand
if game.dealer_hand.is_bust():
    state = "game_over"
    
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
                if hit_button.collidepoint(event.pos): # if hit button being clicked:
                    game.player_hit() # call game.player_hit()
                    if game.player_turn_over(): # when player turn ends
                        state = "dealer_turn" # set state to "dealer_turn"
                elif stand_button.collidepoint(event.pos): # elif stand button being clicked:
                    state = "dealer_turn" # set state to "dealer_turn"
            elif state == "game_over":
                if play_again_button.collidepoint(event.pos): # if play again button clicked:
                    start_new_round() # call start_new_round()

    if state == "dealer_turn":
        game.dealer_turn() # call game.dealer_turn()
        winner = game.resolve_round() # get winner and store
        state = "game_over"# set state to "game_over"

    # card row starting positions
    dealer_hand = game.dealer_hand.cards
    player_hand = game.player_hand.cards
    dealer_hand_x, dealer_hand_y = 30, 50
    player_hand_x, player_hand_y = 440, 50

    if state != "game_over":
        draw_hand(player_hand, player_hand_x, player_hand_y) # call draw_hand() for the player's hand
        draw_hand(dealer_hand, dealer_hand_x, dealer_hand_y) # call draw_hand() for the dealer's hand
    draw_buttons() # call draw_buttons()
    if game.player_hand.is_bust():
        state = "game_over"
    if game.dealer_hand.is_bust():
        state = "game_over"
    if state == "game_over": # if state is "game_over"
        # TODO: add dealers hand and delay for player to see cards.
        if winner != "push":
            winner_text = font.render(f"The {winner} Wins!", True, RESULT_COLOUR)
        else:
            winner_text = font.render("Push! (Draw)", True, RESULT_COLOUR)
        winner_rect = winner_text.get_rect(midbottom=(play_again_button.centerx, play_again_button.top - 15))
        draw_text(winner_text, winner_rect) # show the winner message
        # show dealers total
        dealer_total = font.render(f"The dealer has: {str(game.dealer_hand.get_total())}", True, RESULT_COLOUR)
        dealer_total_rect = dealer_total.get_rect(midbottom = (play_again_button.centerx, winner_rect.top - 15))
        draw_text(dealer_total, dealer_total_rect)
        # show players total
        player_total = font.render(f"The player has: {str(game.player_hand.get_total())}", True, RESULT_COLOUR)
        player_total_rect = player_total.get_rect(midbottom = (play_again_button.centerx, dealer_total_rect.top - 15))
        draw_text(player_total, player_total_rect)
    pygame.display.flip() # update the display
    clock.tick(60) # cap the frame rate at 60 FPS

pygame.quit()