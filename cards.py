import random

def make_card(rank, suit):
    if rank == 11:
        name = "Jack of " + suit
        shorthand = " J" + suit[0] #concatenating initial of rank and suit

    elif rank == 12:
        name = "Queen of " + suit
        shorthand = " Q" + suit[0] #concatenating initial of rank and suit

    elif rank == 13:
        name = "King of " + suit
        shorthand = " K" + suit[0] #concatenating initial of rank and suit
    elif rank == 14:
        name = "Ace of " + suit
        shorthand = " A" + suit[0] #concatenating initial of rank and suit
    else:
        if rank == 10:
            name = str(rank) + " of " + suit
            shorthand = str(rank) + suit[0] #concatenating initial of rank and suit
        else:
            name = str(rank) + " of " + suit
            shorthand = " " + str(rank) + suit[0] #concatenating initial of rank and suit
    
    """
    if suit == "Diamonds" or suit == "Hearts":
        shorthand = "\033[31m" + shorthand + "\033[37m"
    else:
        shorthand = "\033[34m" + shorthand + "\033[37m"
    """
    card_tuple = (shorthand) #creating a tuple containing rank, suit, name, and shorthand

    return card_tuple

def make_deck(make_card):
    card_deck = [] #creating an empty list
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"] #creating a list of suit 

    for suit in suit_list: #iterating through each suit
        for i in range(2, 15): #iterating through the 13 cards of each suit
            result = make_card(i, suit) #calling the make_card function which returns the tuple
            card_deck.append(result) #storing the tuple into card_deck

    return card_deck

def shuffle(deck):
    for index in range(len(deck)):
        j = random.randint(index, len(deck) - 1) #assigning j a random index in the list 
        temp = deck[index] #swapping 1st step
        deck[index] = deck[j] #swapping 2nd step
        deck[j] = temp #swapping 3rd step
 
    return deck #returning shuffled deck

def draw(deck, hand = []):
    if len(deck) == 0: #if deck is empty, returns none
        return None
    else:
        random_index = random.randint(0, len(deck) - 1) #assigning a random index 
        drawn_card = deck.pop(random_index) #removing the drawn card from the deck and assigning to variable drawn_card
        hand.append(drawn_card) #appending the list with the drawn card

    return hand

def deal(deck, number_of_cards):
    hand_1 = [] #initializing an empty list
    hand_2 = [] #initializing an empty list

    for i in range(1, number_of_cards + 1): #iterating n times, where n = number_of_cards
        hand1 = draw(deck, hand_1) #drawing a card and storing it in hand1 list
        hand2 = draw(deck, hand_2) #drawing a card and storing it in hand2 list

    return hand1, hand2

def cut(deck):
    if len(deck) > 1:
        top_half = deck[0:int(len(deck)/2)]
        bottom_half = deck[int(len(deck)/2):]
    else:
        raise ValueError
    return top_half, bottom_half

if __name__ == "__main__":
    #make_card(7, "Spades")
    #make_card(9, "Hearts")
    #make_card(10, "Clubs")
    #make_card(14, "Diamonds")
    print("Making a deck of 52 cards:")
    print(make_deck(make_card))

    """
    deck = make_deck(make_card)

    print("Shuffled deck:")
    print(shuffle(deck))
    
    #print("Drawn card:")
    #print(draw(deck))

    hand1, hand2 = deal(deck, 2)
    print("Hand1:",hand1)
    print("Hand2:",hand2)   

    deck2 = make_deck(make_card)
    top, bottom = cut(deck2)
    print("Top:", top)
    print("Bottom:", bottom)
    """