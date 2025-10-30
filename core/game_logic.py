
#from player_io import ask_player_action
def ask_player_action() -> str:
    user_input = input("please enter S for stand or H for hit \n").upper().strip()
    if user_input in ["H", "S"]:
        return user_input
    else:
        print("invalid input, try again")
        return ask_player_action()

def calculate_hand_value(hand: list[dict]) -> int:
    value = 0
    for card in hand:
        if card["rank"] == "A":
            value += 1
        elif card["rank"] == "J" or card["rank"] == "Q" or card["rank"] == "K":
            value += 10
        else:
            value += int(card["rank"])
    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    player["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    player_hand_val  = calculate_hand_value(player["hand"])
    dealer_hand_val = calculate_hand_value(dealer["hand"])
    print(f"beginning points: player hand value is: {player_hand_val}, dealer hand value is: {dealer_hand_val}")
    return None

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    print("dealer turn!")
    while calculate_hand_value(dealer["hand"]) < 17:
       dealer["hand"].append(deck.pop())
       current_dealer_val = calculate_hand_value(dealer["hand"])
       print(dealer["hand"][-1])
       print(f"dealer current value: {current_dealer_val}")
    if current_dealer_val > 21:
       print(f"dealer failed cause he got over 21")
       return False
    else:
       return True

def winner_decider(dealer_hand: list[dict], player_hand: list[dict]):
   dealer_total = calculate_hand_value(dealer_hand)
   player_total = calculate_hand_value(player_hand)
   if player_total > dealer_total:
       print("the winner is PLAYER!! congrats!!")
   elif dealer_total > player_total:
       print("the winner is DEALER!! congrats!!")
   else:
       print("it's a DRAW!")

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    print("welcome to THE BLACKJACK game")
    deal_two_each(deck, player, dealer)
    while True:
        user_action = ask_player_action()
        if user_action == "H":
            player["hand"].append(deck.pop())
            print(player["hand"][-1])
            player_hand_val = calculate_hand_value(player["hand"])
            if player_hand_val > 21:
                print(f"player got: {player_hand_val} and failed cause it's over 21")
                return None
            else:
                continue
        else:
            dealer_play_result = dealer_play(deck, dealer)
            if dealer_play_result:
                winner_decider(dealer["hand"] ,player["hand"])
                return None
            else:
                print("the winner is PLAYER!! congratulations!!")
                return None


