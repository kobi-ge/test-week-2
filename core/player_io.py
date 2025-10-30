def ask_player_action() -> str:
    user_input = input("please enter S for stand or H for hit \n").upper().strip()
    if user_input in ["H", "S"]:
        return user_input
    else:
        print("invalid input, try again")
        return ask_player_action()



