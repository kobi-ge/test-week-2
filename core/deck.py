import random
def build_standard_deck() -> list[dict]:
    cards_list = []
    card_dict = {}
    for rank in range(1, 14):
        for suite in ["H", "C", "D", "S"]:
            if rank == 1:
                rank = "A"
            elif rank == 11:
                rank = "J"
            elif rank == 12:
                rank = "Q"
            elif rank == 13:
                rank = "K"
            card_dict["rank"] = str(rank)
            card_dict["suite"] = suite
            cards_list.append(card_dict)
            card_dict = {}
    return cards_list


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps:
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        if i == j:
            continue
        card_i_suite = deck[i]["suite"]
        if card_i_suite == "H" and j % 5:
            continue
        elif card_i_suite == "C" and j % 3:
            continue
        elif card_i_suite == "d" and j % 2:
            continue
        elif card_i_suite == "S" and j % 7:
            continue
        deck[i], deck[j] = deck[j], deck[i]
        swaps -= 1
    return deck







