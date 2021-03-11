import enum
from typing import List, cast
import random


class Suit(enum.Enum):
    HEARTS = enum.auto()
    DIAMONDS = enum.auto()
    SPADES = enum.auto()
    CLUBS = enum.auto()


class Card(object):
    CARD_VALUE_DICT = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit: Suit, value: int):
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        print_value = Card.CARD_VALUE_DICT.get(self.value, self.value)
        return f"Card {print_value} of {self.suit.name}"

    def __eq__(self, o: object) -> bool:
        # Only cards can be checked for equality
        if type(o) != type(self):
            return False

        o = cast(Card, o)
        return self.value == o.value and self.suit == o.suit

    def set_ace_to_one(self):
        if self.value == 14:
            self.value = 1


class Deck(object):
    def __init__(self) -> None:
        self.cards: List[Card] = []
        for suit in [Suit.HEARTS, Suit.DIAMONDS, Suit.SPADES, Suit.CLUBS]:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def take_card(self) -> Card:
        return self.cards.pop()


class Player(object):
    def __init__(self, name: str):
        self.name = name
        self.hand: List[Card] = []

    def show_cards(self) -> None:
        print("---------------------")
        print(f"{self.name} cards:")
        for card in self.hand:
            print(f"{card}")
        print("---------------------")

    def get_card(self, card: Card) -> None:
        self.hand.append(card)

    def get_hand_value(self):
        return sum(c.value for c in self.hand)

    def ask_for_another_card(self):
        print(f"** {self.name}s' turn **")
        while True:
            try:
                useranswer = str(
                    input(f"{self.name} Do you want another card? [answer yes or no]"))
                if useranswer.lower() == "yes" or useranswer.lower() == "no":
                    if useranswer.lower() == "yes":
                        return True
                    else:
                        return False
                else:
                    print(f"{self.name} What??? yes or no")
            except:
                print(f"{self.name} What??? yes or no")

    def checking21_singular(self):
        if self.get_hand_value() > 21:
            number_of_aces = 0
            for card in self.hand:
                if card.value == 14:
                    number_of_aces += 1
            if self.get_hand_value() - (14*number_of_aces) < 21:
                while self.get_hand_value() > 21:
                    for card2 in self.hand:
                        if card2.value == 14:
                            card2.set_ace_to_one()
                            print(
                                f"{self.name} change his Card Ace of {card2.value} to {card2}")
                            self.show_cards()
                            break
                return True
            else:
                print(f"{self.name} is out of the game")
                return False
        else:
            return True


class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.players: List[Player] = []
        self.badplayers: List[Player] = []

    def number_of_players(self):
        PlayersValue = 0
        while True:
            try:
                PlayersValue = int(input("How much players?"))
                if PlayersValue > 0:
                    return PlayersValue
                else:
                    print("valid players value. try again...")
            except:
                print("valid players value. try again...")

    def players_names(self, number):
        for place in range(1, number + 1):
            while True:
                try:
                    playername = str(
                        input(f"hey player {place}, what is your name?"))
                    if playername.isalpha():
                        player = Player(playername)
                        self.players.append(player)
                        break
                    else:
                        print("valid name son. change your name!!!")
                except:
                    print("valid name son. change your name@")

    def show_cards(self):
        for player in self.players:
            player.show_cards()

    def checking21(self):
        for player in self.players:
            if player.get_hand_value() > 21:
                number_of_aces = 0
                for card in player.hand:
                    if card.value == 14:
                        number_of_aces += 1
                if player.get_hand_value() - (14*number_of_aces) < 21:
                    for card2 in player.hand:
                        if card2.value == 14:
                            card2.set_ace_to_one()
                            print(
                                f"{player.name} change his Card Ace of {card2.value}, to {card2}")
                        if player.get_hand_value() < 21:
                            player.show_cards()
                            break
                else:
                    x = self.players.remove(player)
                    print(f"{player.name} is out of the game")


#     def ShowCard(self):
#         print(self.suit, self.value)

#     # change ace card from 11 to 1#
#     def setAcetoOne(self):
#         if self.value.lower() == "ace":
#             self.value = "1"
#         return self.value

#     def valueofcard(self):
#         if "ace" in self.value.lower():
#             return 11
#         elif "prince" in self.value.lower():
#             return 12
#         elif "queen" in self.value.lower():
#             return 13
#         elif "king" in self.value.lower():
#             return 14
#         else:
#             return int(self.value)

# def __eq__(self, anotherCard):
#     return self.value == anotherCard.value

#     def __gt__(self, anotherCard):
#         return self.value > anotherCard.value


# class Player:
#         super().__init__()
#         self.SetName(name)
#         self.cards = cards.copy()

#     def GetName(self):
#         return self.name

#     def SetName(self, Newname):
#         if not Newname.isalpha():
#             raise ValueError("Valid name")
#         self.name = Newname[:]

#     def GetCardsList(self):
#         return self.cards

#     def AddCard(self, anothercard):
#         self.cards.append(anothercard)

#     def SumCards(self):
#         sum1 = 0
#         for card in self.cards:
#             sum1 = sum1 + card.valueofcard()
#         return sum1


# ######################################################################################################
# # ~~~~~ all defunctions ~~~~~~~
# # returns the value of players who wanna play
# def HowMuchPlayers():
#     while True:
#         try:
#             PlayersValue = int(input("How much players?"))
#             if PlayersValue > 0:
#                 break
#             else:
#                 print("valid players value. try again...")
#         except:
#             print("valid players value. try again...")
#     return PlayersValue


# def CardCheck():
#     card_value = [
#         "1",
#         "2",
#         "3",
#         "4",
#         "5",
#         "6",
#         "7",
#         "8",
#         "9",
#         "10",
#         "Ace",
#         "Prince",
#         "Queen",
#         "King",
#     ]
#     card_figure = ["HURT♥︎,", "CLUB♣︎,", "DIMOND♦︎,", "SPADE♠︎,"]
#     value_random = card_value[random.randrange(0, 14)]
#     figure_random = card_figure[random.randrange(0, 4)]
#     return Card(figure_random, value_random)


# # creating list of Object PLAYERS. inserting each a name and list with two CARDS Objects
# def StartGame(value):
#     playerslist1 = []
#     for userplace in range(1, value + 1):
#         while True:
#             try:
#                 playername = str(input(f"hey player {userplace}, what is your name?"))
#                 if playername.isalpha():
#                     l = []
#                     l.append(CardCheck())
#                     l.append(CardCheck())
#                     player1 = Player(playername, l)
#                     playerslist1.append(player1)
#                     break
#                 else:
#                     print("valid name son. change your name!!!")
#             except:
#                 print("valid name son. change your name!!!")
#     return playerslist1


# # shows everyone's cards


# def showcardsofeveryone(playerlist1, playerwhosayno12):
#     print("************************")
#     print("************************")
#     print("your's cards players 🤵🏻‍♂️")
#     if playerlist1:
#         for user in playerlist1:
#             print("------------------------")
#             print(user.GetName())
#             for card in user.cards:
#                 print(card.GetCard())
#     print("------------------------")
#     if playerwhosayno12:
#         for user1 in playerwhosayno12:
#             print("------------------------")
#             print(user1.GetName())
#             for card in user1.cards:
#                 print(card.GetCard())
#     print("------------------------")


# # asks the player if he watns another card. if the user wants to return True and if not return False.


# def wantsanothercard(user):
#     print(f"** {user.GetName()}s' turn **")
#     while True:
#         try:
#             useranswer = str(
#                 input(f"{user.GetName()} Do you want another card? [answer yes or no]")
#             )
#             if useranswer.lower() == "yes" or useranswer.lower() == "no":
#                 if useranswer.lower() == "yes":
#                     return True
#                 else:
#                     return False
#             else:
#                 print(f"{user.GetName()} What??? yes or no")
#         except:
#             print(f"{user.GetName()} What??? yes or no")


# def checking21general(playerslist1):
#     for user in playerslist1:
#         sum = 0
#         acelist = []
#         for card in user.cards:
#             if card.CardValue().lower() == "ace":
#                 acelist.append(card.valueofcard())
#             sum = sum + card.valueofcard()
#         if sum > 21:
#             if acelist:
#                 if sum - (11 * len(acelist)) < 21:
#                     print(f"{user.GetName()} your Ace changed to 1. It was Inevitable.")
#                     for card2 in user.cards:
#                         if card2.CardValue().lower() == "ace":
#                             card2.setAcetoOne()
#                             break
#                     break
#             else:
#                 print(f"{user.GetName()} removed from the game")
#                 playerslist1.remove(user)
#     if not playerslist1:
#         print(f"{user.GetName()} won the game! that was boring. 🤷🏽‍♂️")
#     if len(playerslist1) == 1:
#         print(f"{playerslist1[0].GetName()} won the game! that was boring. 🤷🏽‍♂️")
#         playerslist1.pop()
#     return playerslist1


# def playerpass21(user):
#     sum = 0
#     acelist = []
#     for card in user.cards:
#         if card.valueofcard() == 11:
#             while True:
#                 try:
#                     useranswer = input(
#                         f"{user.GetName()} you got ACE at your card. Do you want to change his value to 1 ?"
#                     )
#                     if useranswer.lower() == "yes":
#                         card.setAcetoOne()
#                         print("Ace have changed to 1")
#                         break
#                     if useranswer.lower() == "no":
#                         print("ok Ace remain 11")
#                         acelist.append(card.valueofcard())
#                         break
#                     else:
#                         print(f"{user.GetName()} What??? yes or no")
#                 except:
#                     print(f"{user.GetName()} What??? yes or no")
#         sum = sum + card.valueofcard()
#     if sum > 21:
#         if acelist:
#             if sum - (11 * len(acelist)) < 21:
#                 print(f"{user.GetName()} your Ace changed to 1. It was Inevitable.")
#                 for card2 in user.cards:
#                     if card2.CardValue().lower() == "ace":
#                         card2.setAcetoOne()
#                 return user, True
#         return user, False
#     if sum <= 21:
#         return user, True


# #####################################################################################################
# # ~~~~~ main program ~~~~~

# drawlist = []
# playerslistwhosaidno = []
# playersvalue = HowMuchPlayers()
# playerslist = StartGame(playersvalue)
# showcardsofeveryone(playerslist, playerslistwhosaidno)
# playerslist = checking21general(playerslist)
# while len(playerslist) > 0:
#     for player in playerslist:
#         playeranswer = wantsanothercard(player)
#         if not playeranswer:
#             playerslist.remove(player)
#             playerslistwhosaidno.append(player)
#             print(
#                 f"{player.GetName()} stops actions and waiting to all players to finish."
#             )
#             showcardsofeveryone(playerslist, playerslistwhosaidno)
#             continue
#         if playeranswer:
#             player.cards.append(CardCheck())
#             showcardsofeveryone(playerslist, playerslistwhosaidno)
#             player1, playertag = playerpass21(player)
#             if not playertag:
#                 playerslist.remove(player)
#                 print(f"{player.GetName()} has removed from game")
#                 showcardsofeveryone(playerslist, playerslistwhosaidno)
#                 if len(playerslist) == 1 and not playerslistwhosaidno:
#                     print(f"congrats, {playerslist[0].GetName()} won the game! 💰")
#                     playerslist.pop()
#                 continue
#             else:
#                 player.cards = player1.cards[:]
#                 showcardsofeveryone(playerslist, playerslistwhosaidno)
#                 continue
# if playerslistwhosaidno:
#     max = 0
#     winnername = " "
#     for playerno in playerslistwhosaidno:
#         if playerno.SumCards() > max:
#             max = playerno.SumCards()
#             winnername = playerno.GetName()
#     for checkdrew in playerslistwhosaidno:
#         if checkdrew.SumCards() == max and checkdrew.GetName() != winnername:
#             drawlist.append(checkdrew)
#     if drawlist:
#         for serchy in playerslistwhosaidno:
#             if serchy.GetName() == winnername:
#                 drawlist.append(serchy)
#         print("we have draw between:")
#         showcardsofeveryone(drawlist, None)
#         print(
#             "ok ok ok listen. every one gets one card. \n the one closer to 21 WINS. Go"
#         )
#         for matchplayers in drawlist:
#             matchplayers.cards.append(CardCheck())
#         showcardsofeveryone(drawlist, None)
#         gapmin = 0
#         winnername2 = " "
#         for matchplayers2 in drawlist:
#             gapto21 = abs(21 - matchplayers2.SumCards())
#             if gapmin < gapto21:
#                 gapmin = gapto21
#                 winnername2 = matchplayers2.GetName()
#         print(f"{winnername2} is the winer after draw. his cards are the closet to 21")
#     else:
#         print(f"{winnername} is the winner!!!!")


# ##############################################################
# # @@@@@@@@@@@@@@@@@@@@@@@ asserting @ @@@@@@@@@@@@@@@@@@@@@@@@@@@
# ##############################################################

# cardaaa = Card("hurt", "9")
# cardbbb = Card("hurt", "10")
# cardccc = Card("Dimond", "king")
# cardddd = Card("Dimond", "3")
# cardeee = Card("club", "king")
# cardfff = Card("hurt", "3")
# cardhigh = Card("hurt", "prince")
# cardhigh2 = Card("hurt", "king")
# cardhigh3 = Card("hurt", "king")
# cardhigh4 = Card("dimond", "queen")
# card13 = Card("hurt", "ace")
# cardslist1 = [cardaaa, cardbbb]
# cardslist2 = [cardccc, cardddd]
# cardslist3 = [cardeee, cardfff]
# cardslisthigh = [cardhigh, cardhigh2]
# cardslisthigh2 = [cardhigh3, cardhigh4]
# assert cardaaa != cardbbb
# assert Card("hurt", "5") > Card("hurt", "3")
# playeraaa = Player("yonatan", cardslist1)
# playerbbb = Player("dror", cardslist2)
# playerccc = Player("YONI", cardslist3)
# playerhigh = Player("high", cardslisthigh)
# playerhigh2 = Player("hor", cardslisthigh2)
# playerhighlist44 = [playerhigh, playerhigh2]
# playerlist11 = [playeraaa, playerbbb]
# playerslistwhosaidno.append(playerbbb)
# playerslistwhosaidno.append(playerccc)
# cardofcardcheck = CardCheck()
# assert 0 < cardofcardcheck.valueofcard() < 15
# x, y = playerpass21(playerhigh)
# assert y == False
# z, a = playerpass21(playeraaa)
# assert a == True
# assert playeraaa.GetName().lower() == "yonatan"
# assert cardddd.valueofcard() == 3
# assert card13.valueofcard() == 11
# card13.setAcetoOne()
# assert card13.valueofcard() == 1
# card1 = Card("hurt", "ace")
# card2 = Card("hurt", "prince")
# card3 = Card("hurt", "3")
# card4 = Card("hurt", "4")
# card3 = Card("dimond", "1")
# card4 = Card("dimond", "1")
# liststam1 = [card3, card4]
# playerstam = Player("stam", liststam1)
# liststam2 = [playerstam]
# list1 = [card1, card2]
# list2 = [card3, card4]
# playera = Player("yoni", list1)
# playerb = Player("yuav", list2)
# playlist = [playera, playerb]
# x = checking21general(playlist)
# for y in x:
#     for card in y.cards:
#         assert card.CardValue().lower() != "ace"
# p = checking21general(playerhighlist44)
# assert len(p) < 2
# pp = checking21general(playerlist11)
# assert len(pp) == 2
