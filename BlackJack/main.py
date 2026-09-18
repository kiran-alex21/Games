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
        for suit in suits: # creating each card and append it to self.cards
            for r, v in Ranks_Values.items():
                self.cards.append(Card(r, suit, v))

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
        self.deck = Deck()       # Deck instance
        self.player_hand = Hand()  # Hand instance
        self.dealer_hand = Hand()  # Hand instance

    def player_turn(self):
        bust = False
        stand = False
        while not bust and not stand: # loop until the player stands or busts
            choice = input("Hit(H) or Stand(S)? ") # ask the player to hit or stand (input or button in pygame later)
            choice = choice[0]
            if choice == "S": # if stand
                stand = True # break out of the loop
            elif choice == "H": # if hit
                card = self.deck.deal_card() # deal a card from deck 
                self.player_hand.add_card(card) # add card to player hand
                bust = self.player_hand.is_bust() # check for bust after each hit; stop looping if True

    def dealer_turn(self):
        bust = False
        while (self.dealer_hand.get_total() < 17) and not bust: # loop while dealer total is less than 17
            card = self.deck.deal_card() # deal a card from self.deck 
            self.dealer_hand.add_card() # add it to self.dealer_hand
            bust = self.dealer_hand.is_bust() # loop stops once dealer busts

    def resolve_round(self):
        # TODO: check if self.player_hand.is_bust() -> dealer wins
        # TODO: check if self.dealer_hand.is_bust() -> player wins
        # TODO: otherwise, compare self.player_hand.get_total() vs self.dealer_hand.get_total()
        #       higher total wins; equal totals = push (tie)
        # TODO: return or print the result
        pass

    def play_round(self):
        # TODO: create a new Deck instance and assign it to self.deck
        # TODO: call self.deck.shuffle()
        # TODO: create new Hand instances for self.player_hand and self.dealer_hand
        # TODO: deal 2 cards each to start (player and dealer)
        # TODO: call self.player_turn()
        # TODO: if the player didn't bust, call self.dealer_turn()
        # TODO: call self.resolve_round()
        # TODO: display/print the outcome of the round
        pass