from blackjack2 import Deck, Player, Card, Game

# date: 10/3/2021

game = Game()
game.deck.shuffle()
numberofplayers = game.number_of_players()
game.players_names(numberofplayers)
for player in game.players:
    for _ in range(2):
        player.get_card(game.deck.take_card())
game.show_cards()
game.checking21()
for mister in game.players:
    if len(game.badplayers) + 1 == len(game.players):
        print(f"{mister.name} is the winner")
        break
    answer = mister.ask_for_another_card()
    while answer == True:
        c = game.deck.take_card()
        print(f"{mister.name} got {c}")
        mister.get_card(c)
        game.show_cards()
        x = mister.checking21_singular()
        if not x:
            game.badplayers.append(mister)
            break
        answer = mister.ask_for_another_card()
if len(game.badplayers) + 1 != len(game.players):
    draw = []
    finallist = list(set(game.players) - set(game.badplayers))
    tophand = max(a.get_hand_value() for a in finallist)
    for player in finallist:
        if player.get_hand_value() == tophand:
            draw.append(player)
    if len(draw) > 1:
        print("the winners are:")
        for i in draw:
            print(i.name)
    else:
        print(f"the winner is {draw[0].name}")
