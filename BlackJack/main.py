##Imports
import random

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = []  # list of Card instances
        Ranks_Values = { # Card ranks and values
            "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "J": 10, "Q": 10, "K": 10,
            }
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits: # loops for each suit
            for r, v in Ranks_Values.items(): # loops for each Rank
                card = Card(r, suit, v) # creating each card
                self.cards.append(card) # append it to self.cards

    def shuffle(self): # return a shuffled deck
        shuffled = random.shuffle(self.cards)
        return shuffled

    def deal_card(self): # removes + returns last card
        try:
            deal_card = self.cards.pop() # remove the last card
        except:
            deal_card = None
        return deal_card


class Hand:
    def __init__(self):
        self.cards = []  # list of Card instances

    def add_card(self, card): # appends the card to self.cards
        self.cards.append(card)

    def get_total(self):
        total = 0
        aces = 0
        for card in self.cards: # Sum of the value of every card
            total += card.value
            if card.rank == "A": # counts how many  aces
                aces += 1
        while total > 21: # checks for bust due to high aces
            if aces > 0: # reduces aces value to 1 if needed
                total -= 10
                aces -= 1
            else:
                break
        # return the final total
        return total

    def is_bust(self):
        total = self.get_total() # get the current total using self.get_total()
        if total > 21: # return True if  total is over 21, else False
            return True
        else:
            return False


class BlackjackGame:
    def __init__(self):
        self.deck = None       # Deck instance
        self.player_hand = None  # Hand instance
        self.dealer_hand = None  # Hand instance

    def player_turn(self):
        bust = False
        stand = False
        while not bust and not stand: # loop until the player stands or busts
            current_total = self.player_hand.get_total()
            print(f"You're current total is {current_total}")
            choice = input("Hit(H) or Stand(S)? ") # ask the player to hit or stand (input or button in pygame later)
            choice = choice[0].upper()
            if choice == "S": # if stand
                stand = True # break out of the loop
            elif choice == "H": # if hit
                card = self.deck.deal_card() # deal a card from deck
                if card != None:
                    self.player_hand.add_card(card) # add card to player hand
                else:
                    print("No Cards left")
                bust = self.player_hand.is_bust() # check for bust after each hit; stop looping if True
        return stand

    def player_hit(self):
        card = self.deck.deal_card() # deal a card from deck
        if card != None:
            self.player_hand.add_card(card) # add card to player hand
        else:
            print("No Cards left")

    def player_turn_over(self):
        return self.player_hand.is_bust() # check for bust and returns outcome

    def dealer_turn(self):
        while (self.dealer_hand.get_total() < 17) and not self.player_hand.is_bust(): # loop while dealer total is less than 17
            card = self.deck.deal_card()
            if card != None: # deal a card from self.deck 
                self.dealer_hand.add_card(card) # add it to self.dealer_hand
            else:
                print("No Cards left")

    def resolve_round(self):
        winner = None
        player_total = self.player_hand.get_total()
        dealer_total = self.dealer_hand.get_total()
        if self.player_hand.is_bust(): # if self.player_hand.is_bust()
            winner = "dealer" # dealer wins
        elif self.dealer_hand.is_bust(): # if self.dealer_hand.is_bust()
            winner = "player" # player wins
        else:
            if player_total > dealer_total: # compare player_total vs dealer_total, higher total wins
                winner = "player" 
            elif dealer_total > player_total:
                winner = "dealer"
            else:
                winner = "push" # equal totals = push (tie)
        print(f"The dealer has: {dealer_total}\nThe player has: {player_total}")
        return winner # return result
        pass

    def start_round(self):
        self.deck = Deck() # create a new Deck instance and assign it to self.deck
        self.deck.shuffle() # call self.deck.shuffle()
        self.player_hand = Hand()  # Player Hand instance
        self.dealer_hand = Hand()  # Dealer Hand instance
        count = 0
        while count < 2: # deal 2 cards each to start (player and dealer)
            card = self.deck.deal_card()
            self.player_hand.add_card(card)
            card = self.deck.deal_card()
            self.dealer_hand.add_card(card)
            count += 1

    def play_round(self):
        stand = False
        bust = False
        while not stand and not bust:
            stand = self.player_turn() # call self.player_turn()
            bust = self.player_hand.is_bust()
            self.dealer_turn() # call self.dealer_turn()
        else:
            winner = self.resolve_round() # call self.resolve_round()
            print(f"The {winner} has won") # display/print the outcome of the round

if __name__ == "__main__":
    game = BlackjackGame()
    game.start_round()
    game.play_round()