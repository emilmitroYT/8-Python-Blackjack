import random

# Skapa kortleken
deck = [6, 7, 8, 9, 10, "J", "Q", "K", 11] * 4

# Blanda kortleken
random.shuffle(deck)

# Spelarens hand
hand = []

# Räkna poäng
def count_points(hand):
    points = sum(hand)
    # Kolla om ess ska räknas som 1 eller 11
    if 11 in hand and points > 21:
        points -= 10
    return points

# Ge ett kort till spelaren
def draw_card():
    card = deck.pop()
    if card == "J" or card == "Q" or card == "K":
        card = 2
    elif card == 11:
        card = 11
    return card

# Starta spelet
print("Game Blackjack!")

# Ge två kort till spelaren
for i in range(2):
    hand.append(draw_card())

# Summera poängen
points = count_points(hand)
# Visa spelarens kort
print("Dina kort är:", hand, " aka ", points, ".")

# Kolla om spelaren har fått 21 poäng
if count_points(hand) == 21:
    print("Grattis! Du har 21!")
else:
    # Fortsätt spelet tills spelaren väljer att stanna eller får över 21 poäng
    while True:
        choice = input("Vill du ha ett till kort? (j/n) ")
        if choice.lower() == "j":
            hand.append(draw_card())
            points = count_points(hand)
            print("Dina kort är:", hand, " aka ", points, ".")
            if points == 21:
                print("Grattis! Du har 21!")
                break
            elif points > 21:
                print("Tyvärr har du förlorat.",  " Aka ", points, ".")
                break
        else:
            print("Du har", count_points(hand), "poäng och GAME IS OVER.")
            break
