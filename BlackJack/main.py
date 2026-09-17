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
        # TODO: sum the value of every card in self.cards
        # TODO: count how many of those cards are aces
        # TODO: while the total is over 21 and there's an ace counted as 11,
        #       subtract 10 from the total for each ace (11 -> 1) until total <= 21
        #       or no more aces can be reduced
        # TODO: return the final total
        pass

    def is_bust(self):
        # TODO: get the current total using self.get_total()
        # TODO: return True if that total is over 21, else False
        pass


class BlackjackGame:
    def __init__(self):
        self.deck = None       # Deck instance
        self.player_hand = None  # Hand instance
        self.dealer_hand = None  # Hand instance

    def player_turn(self):
        # TODO: loop until the player stands or busts
        # TODO: ask the player to hit or stand (input or button in pygame later)
        # TODO: if hit, deal a card from self.deck and add it to self.player_hand
        # TODO: check self.player_hand.is_bust() after each hit; stop looping if True
        # TODO: if stand, break out of the loop
        pass

    def dealer_turn(self):
        # TODO: loop while self.dealer_hand.get_total() is less than 17
        # TODO: on each loop, deal a card from self.deck and add it to self.dealer_hand
        # TODO: loop naturally stops once total is 17 or more (or dealer busts)
        pass

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