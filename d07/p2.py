CARDS_POWER = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1, # J's are the weakest now
    'T': 10,
}

hands = []

with open('input.txt', 'r') as file:
    for line in file:
        data = line.split(' ')
        hands.append({
            'cards': data[0],
            'bid': int(data[1]),
            'power': 0,
        })

for hand in hands:
    # first let's count how many cards of each type we have
    cards_count = [0] * 15
    for card in hand['cards']:
        card_power = CARDS_POWER[card] if card in CARDS_POWER else int(card)
        cards_count[card_power] += 1

    # Now let's see if we need to play around with the joker
    print('hand', hand['cards'])
    print('b joker', cards_count)

    if 'J' in hand['cards']:
        highest_count = 0
        highest_card_power = 1
        for card_power, card_count in enumerate(cards_count):
            if card_power != 1 and card_count > 0:
                # J shouldn't count to avoid that if J is the highest count, e.g. T1JJK, in here the clear winner is T1KKK and not T1JJK
                # also avoice JJJJJ, which cause all card_counts but J to be 0
                if card_count > highest_count:
                    # keep a track of the car that has the highest count, as this will be the joker
                    highest_card_power = card_power
                    highest_count = card_count
                elif card_count == highest_count and card_power > highest_card_power:
                    # the max can be because of the count is higher, or the card size is bigger
                    highest_card_power = card_power

        if highest_card_power != 1:
            # If the result turns out to be different from the joker, use the joker
            cards_count[highest_card_power] += cards_count[1]
            cards_count[1] = 0

    # calculate the hand power, the more cards of the same kind you have, the better
    hand_power = 0
    print('a joker', cards_count)
    print('-----')
    for card_count in cards_count:
        if card_count > 0:
            # ['A']: 5                                                            # 25
            # ['A']: 4 + ['B']: 1                                                 # 16+1=17
            # ['A']: 3 + ['B']: 2                                                 # 9+4=13
            # ['A']: 3 + ['B']: 1 + ['C']: 1                                      # 9+1+1=11
            # ['A']: 2 + ['B']: 2 + ['C']: 1                                      # 4+4+1=9
            # ['A']: 2 + ['B']: 1 + ['C']: 1 + ['D']: 1                           # 4+1+1+1=7
            # ['A']: 1 + ['B']: 1 + ['C']: 1 + ['D']: 1 + ['E']: 1                # 1+1+1+1+1=5
            hand_power += card_count * card_count

    hand['power'] = hand_power

# now that we calculated the powers we sort them by power
for hand in hands:
    hand['power'] = hand['power'] * 10000000000000 + sum([(CARDS_POWER[card] if card in CARDS_POWER else int(card)) * 100 ** (5-i) for i, card in enumerate(hand['cards'])])

hands = sorted(hands, key=lambda x: x['power'])

# now we calculate the bids portion of it
results_part_2 = 0
for i, hand in enumerate(hands):
    results_part_2 += (i+1)*hand['bid']

print('[part 2]', results_part_2)