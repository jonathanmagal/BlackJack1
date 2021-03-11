
from blackjack2 import Player, Suit, Card, Deck, Game
from hashlib import new


def test_repr():
    assert str(Card(Suit.HEARTS, 5)) == "Card 5 of HEARTS"
    assert str(Card(Suit.DIAMONDS, 11)) == "Card Jack of DIAMONDS"
    assert str(Card(Suit.CLUBS, 12)) == "Card Queen of CLUBS"
    assert str(Card(Suit.CLUBS, 13)) == "Card King of CLUBS"
    assert str(Card(Suit.CLUBS, 14)) == "Card Ace of CLUBS"


# TDD (TEST DRIVEN DEVELOPMENT)
# RED > GREEN > REFACTOR
def test_equality():
    assert Card(Suit.HEARTS, 5) != "5"
    assert Card(Suit.HEARTS, 5) != Card(Suit.HEARTS, 6)
    assert Card(Suit.HEARTS, 5) != Card(Suit.CLUBS, 5)
    assert Card(Suit.HEARTS, 5) == Card(Suit.HEARTS, 5)


def test_set_ace_to_one():
    c1 = Card(Suit.HEARTS, 14)
    c1.set_ace_to_one()
    c2 = Card(Suit.HEARTS, 1)
    assert c1.value == c2.value
    c3 = Card(Suit.HEARTS, 13)
    c3.set_ace_to_one()
    assert c1.value != c3.value


def test_create_deck():
    deck = Deck()
    assert len(deck.cards) == 52
    assert deck.cards[0] == Card(Suit.HEARTS, 2)
    assert deck.cards[-1] == Card(Suit.CLUBS, 14)


def test_shuffle_deck():
    deck = Deck()
    original_order = " ".join(str(card) for card in deck.cards)

    for _ in range(1000):
        deck.shuffle()
        new_order = " ".join(str(card) for card in deck.cards)
        assert original_order != new_order


def test_take_card():
    deck = Deck()
    handed_card = deck.take_card()
    for card in deck.cards:
        assert handed_card != card


def test_player():
    player = Player("Dror")
    player.get_card(Card(Suit.HEARTS, 14))
    player.get_card(Card(Suit.CLUBS, 2))
    assert player.get_hand_value() == 16


def test_number_of_players():
    game = Game()
    x = game.number_of_players()
    assert x > 0


def test_players_names():
    game = Game()
    playerslist = game.players_names(5)
    assert len(playerslist) == 5


def test_checking21():
    game = Game()
    player1 = Player("yonatan")
    player2 = Player("dror")
    player3 = Player("omer")
    player1.get_card(Card(Suit.DIAMONDS, 11))
    player1.get_card(Card(Suit.CLUBS, 14))
    player1.get_card(Card(Suit.HEARTS, 13))
    player2.get_card(Card(Suit.DIAMONDS, 7))
    player2.get_card(Card(Suit.HEARTS, 9))
    player3.get_card(Card(Suit.DIAMONDS, 14))
    player3.get_card(Card(Suit.CLUBS, 11))
    game.players.append(player1)
    game.players.append(player2)
    game.players.append(player3)
    game.checking21()
    assert player1 not in game.players
    assert player2 in game.players
    assert player3 in game.players
    for p in game.players:
        if p.name == "dror":
            assert p.get_hand_value() == 16
        if p.name == "omer":
            assert p.get_hand_value() == 12


def test_checking21_singular():
    player1 = Player("adam")
    player2 = Player("roee")
    player3 = Player("tamar")
    player1.get_card(Card(Suit.DIAMONDS, 5))
    player1.get_card(Card(Suit.CLUBS, 13))
    player1.get_card(Card(Suit.HEARTS, 14))
    player2.get_card(Card(Suit.DIAMONDS, 7))
    player2.get_card(Card(Suit.HEARTS, 9))
    player3.get_card(Card(Suit.DIAMONDS, 14))
    player3.get_card(Card(Suit.CLUBS, 13))
    player3.get_card(Card(Suit.CLUBS, 12))
    assert player1.checking21_singular() == True
    assert player1.get_hand_value() == 19
    assert player2.checking21_singular(player2) == True
    assert player2.get_hand_value() == 16
    assert player3.checking21_singular(player3) == False
    assert player1.get_hand_value() == 26


def test_game():
    game = Game()
    game.deck.shuffle()
    values = [[11, 14], [7, 9], [13, 12], [5, 4]]
    for name in ["jonathan", "dror", "matan", "moshe"]:
        game.players.append(Player(name))
    for player in game.players:
        for _ in range(2):
            player.get_card(game.deck.take_card())
    for player, value in zip(game.players, values):
        player.hand[0].value = value[0]
        player.hand[1].value = value[1]
    game.checking21()
    for player1 in game.players:
        assert player1.name != "matan"
    for player2 in game.players:
        player2.get_card(Card(Suit.CLUBS, 14))
        player2.checking21_singular()
    for i in game.players:
        if i.name == "jonathan":
            assert i.get_hand_value() == 13
        if i.name == "dror":
            assert i.get_hand_value() == 17
        if i.name == "moshe":
            assert i.get_hand_value() == 10
    assert len(game.players) == 3
    x = game.deck.take_card()
    for card in game.deck.cards:
        assert card != x
