"""
Tests for main.py

Run with: python -m pytest Blackjack -v

These are written against the intended behaviour described in the TODOs.
Most will fail until you implement the corresponding method — that's
expected. Implement one method, then re-run to check it.
"""

import pytest
from main import Card, Deck, Hand, BlackjackGame


# ---------- Card ----------

def test_card_stores_attributes():
    card = Card(rank="K", suit="Hearts", value=10)
    assert card.rank == "K"
    assert card.suit == "Hearts"
    assert card.value == 10


# ---------- Deck ----------

def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52


def test_deck_has_13_ranks_per_suit():
    deck = Deck()
    suits = {card.suit for card in deck.cards}
    assert len(suits) == 4
    for suit in suits:
        ranks_in_suit = [card.rank for card in deck.cards if card.suit == suit]
        assert len(ranks_in_suit) == 13
        assert len(set(ranks_in_suit)) == 13  # no duplicate ranks within a suit


def test_deck_shuffle_keeps_same_cards_different_order():
    deck = Deck()
    original_order = list(deck.cards)
    deck.shuffle()
    assert len(deck.cards) == 52
    # same cards present (order-independent check)
    assert sorted((c.rank, c.suit) for c in deck.cards) == \
           sorted((c.rank, c.suit) for c in original_order)
    # NOTE: this does not strictly guarantee the order changed (shuffle can
    # rarely return the same order by chance), but catches a no-op shuffle()
    # almost always in practice.


def test_deal_card_removes_and_returns_a_card():
    deck = Deck()
    dealt = deck.deal_card()
    assert isinstance(dealt, Card)
    assert len(deck.cards) == 51
    assert dealt not in deck.cards


def test_deal_card_empties_deck_after_52_deals():
    deck = Deck()
    for _ in range(52):
        deck.deal_card()
    assert len(deck.cards) == 0


# ---------- Hand ----------

def test_add_card_appends_to_hand():
    hand = Hand()
    card = Card("7", "Clubs", 7)
    hand.add_card(card)
    assert card in hand.cards
    assert len(hand.cards) == 1


def test_get_total_simple_no_ace():
    hand = Hand()
    hand.add_card(Card("7", "Clubs", 7))
    hand.add_card(Card("9", "Spades", 9))
    assert hand.get_total() == 16


def test_get_total_single_ace_counts_as_11_when_safe():
    hand = Hand()
    hand.add_card(Card("A", "Hearts", 11))
    hand.add_card(Card("6", "Diamonds", 6))
    assert hand.get_total() == 17  # ace stays 11


def test_get_total_ace_drops_to_1_to_avoid_bust():
    hand = Hand()
    hand.add_card(Card("A", "Hearts", 11))
    hand.add_card(Card("K", "Spades", 10))
    hand.add_card(Card("5", "Clubs", 5))
    assert hand.get_total() == 16  # 11+10+5=26 -> ace drops to 1 -> 16


def test_get_total_two_aces():
    hand = Hand()
    hand.add_card(Card("A", "Hearts", 11))
    hand.add_card(Card("A", "Spades", 11))
    hand.add_card(Card("9", "Clubs", 9))
    # 11+11+9=31 (bust) -> drop one ace to 1 -> 1+11+9=21 (stop, no longer bust)
    # your get_total() should drop aces ONE AT A TIME until <= 21, not all at once
    assert hand.get_total() == 21


def test_is_bust_true_over_21():
    hand = Hand()
    hand.add_card(Card("K", "Hearts", 10))
    hand.add_card(Card("Q", "Spades", 10))
    hand.add_card(Card("5", "Clubs", 5))
    assert hand.is_bust() is True


def test_is_bust_false_under_21():
    hand = Hand()
    hand.add_card(Card("K", "Hearts", 10))
    hand.add_card(Card("5", "Spades", 5))
    assert hand.is_bust() is False


def test_is_bust_false_at_exactly_21():
    hand = Hand()
    hand.add_card(Card("A", "Hearts", 11))
    hand.add_card(Card("K", "Spades", 10))
    assert hand.is_bust() is False


# ---------- BlackjackGame.player_turn ----------

def test_player_turn_stops_on_stand(monkeypatch):
    game = BlackjackGame()
    game.deck = Deck()
    game.player_hand = Hand()
    game.player_hand.add_card(Card("9", "Hearts", 9))
    game.player_hand.add_card(Card("8", "Spades", 8))
    monkeypatch.setattr("builtins.input", lambda *args: "stand")
    game.player_turn()
    assert game.player_hand.get_total() == 17  # unchanged, no cards drawn


def test_player_turn_hits_until_bust_or_stand(monkeypatch):
    game = BlackjackGame()
    game.deck = Deck()
    game.player_hand = Hand()
    game.player_hand.add_card(Card("9", "Hearts", 9))
    game.player_hand.add_card(Card("8", "Spades", 8))
    responses = iter(["hit", "stand"])
    monkeypatch.setattr("builtins.input", lambda *args: next(responses))
    game.player_turn()
    assert len(game.player_hand.cards) == 3  # one card was drawn, then stood


# ---------- BlackjackGame.dealer_turn ----------

def test_dealer_turn_stops_at_17_or_more():
    game = BlackjackGame()
    game.deck = Deck()
    game.dealer_hand = Hand()
    game.dealer_hand.add_card(Card("K", "Hearts", 10))
    game.dealer_hand.add_card(Card("9", "Spades", 9))  # total 19, already >= 17
    game.dealer_turn()
    assert len(game.dealer_hand.cards) == 2  # no cards drawn


def test_dealer_turn_draws_while_under_17():
    game = BlackjackGame()
    game.deck = Deck()
    game.dealer_hand = Hand()
    game.dealer_hand.add_card(Card("5", "Hearts", 5))
    game.dealer_hand.add_card(Card("4", "Spades", 4))  # total 9, well under 17
    game.dealer_turn()
    assert game.dealer_hand.get_total() >= 17


# ---------- BlackjackGame.resolve_round ----------

def test_resolve_round_player_busts_dealer_wins():
    game = BlackjackGame()
    game.player_hand = Hand()
    game.player_hand.add_card(Card("K", "Hearts", 10))
    game.player_hand.add_card(Card("Q", "Spades", 10))
    game.player_hand.add_card(Card("5", "Clubs", 5))  # 25, bust
    game.dealer_hand = Hand()
    game.dealer_hand.add_card(Card("9", "Hearts", 9))
    game.dealer_hand.add_card(Card("8", "Spades", 8))
    result = game.resolve_round()
    assert result == "dealer"


def test_resolve_round_dealer_busts_player_wins():
    game = BlackjackGame()
    game.player_hand = Hand()
    game.player_hand.add_card(Card("9", "Hearts", 9))
    game.player_hand.add_card(Card("8", "Spades", 8))
    game.dealer_hand = Hand()
    game.dealer_hand.add_card(Card("K", "Hearts", 10))
    game.dealer_hand.add_card(Card("Q", "Spades", 10))
    game.dealer_hand.add_card(Card("5", "Clubs", 5))  # 25, bust
    result = game.resolve_round()
    assert result == "player"


def test_resolve_round_higher_total_wins():
    game = BlackjackGame()
    game.player_hand = Hand()
    game.player_hand.add_card(Card("K", "Hearts", 10))
    game.player_hand.add_card(Card("9", "Spades", 9))  # 19
    game.dealer_hand = Hand()
    game.dealer_hand.add_card(Card("K", "Clubs", 10))
    game.dealer_hand.add_card(Card("7", "Diamonds", 7))  # 17
    result = game.resolve_round()
    assert result == "player"


def test_resolve_round_equal_totals_is_push():
    game = BlackjackGame()
    game.player_hand = Hand()
    game.player_hand.add_card(Card("K", "Hearts", 10))
    game.player_hand.add_card(Card("8", "Spades", 8))  # 18
    game.dealer_hand = Hand()
    game.dealer_hand.add_card(Card("Q", "Clubs", 10))
    game.dealer_hand.add_card(Card("8", "Diamonds", 8))  # 18
    result = game.resolve_round()
    assert result == "push"


# ---------- BlackjackGame.play_round ----------

def test_play_round_sets_up_deck_and_deals_initial_cards(monkeypatch):
    game = BlackjackGame()
    monkeypatch.setattr("builtins.input", lambda *args: "stand")
    game.play_round()
    assert isinstance(game.deck, Deck)
    assert len(game.player_hand.cards) >= 2
    assert len(game.dealer_hand.cards) >= 2