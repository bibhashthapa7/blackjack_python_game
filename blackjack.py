import re
import cards

def swap(a_list, a, b):
    temp = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = temp

def hand_score(hand):
    score = 0 #initializing the score
    for i in range(len(hand)): #iterating through the list of hand of cards
        for rank in re.findall("\d+",hand[i]): #using regex to find the rank of the card (if it is numeric)
            score += int(rank) #incrementing the score by the rank of card

        if hand[i][1] == 'J' or hand[i][1] == 'Q' or hand[i][1] == 'K': #checks if the card is a face card (Jack, Queen, or King)
            score += 10 #increments score by 10

        elif hand[i][0] == 'A': #checks if card is an Ace
            if score + 11 > 21: #checks if score will bust
                score += 1 #increments score by 1 if it will bust
            else:
                score += 11 #increments score by 11 if it does not bust
    
    return score #returning score

def reg_ex_rank(card): #using a helper function to return the value of facecards (A, Q, K, J) and numeric cards
    for rank in re.findall('[AKQJ]\w{0}|\d+', card):
        if rank == 'A':
            rank = 14
            return rank
        elif rank == 'K':
            rank = 13
            return rank
        elif rank == 'Q':
            rank = 12
            return rank
        elif rank == 'J':
            rank = 11
            return rank
        else: 
            return rank

def print_hand_and_score(name, hand):
    print(name, ":", sep="") #printing name
    
    for _ in range(len(hand)): #iterating through each element
        for index in range(1, len(hand)): #iterating through each element starting from i
            rank_1 = reg_ex_rank(hand[index - 1]) #assigning the rank value by calling the helper function
            rank_2 = reg_ex_rank(hand[index]) #assigning the rank value by calling the helper function
            while index > 0 and (int(rank_2) < int(rank_1)):  #checks if the two values are swap-able and sorts
                swap(hand, index, index - 1) #swaps
                index -= 1 #decrements index
        
    sorted_list = [i for i in hand] #using list comprehension
    for i in range(len(sorted_list)): #iterating through each element in list of hand
        print(hand[i]," ", end="") #prints the cards in ascending order of rank 

    total_score = hand_score(hand) #calling the hand_score function
    if total_score > 21:
        print("\nScore:", total_score, "(busted)") #prints total score 
    else:
        print("\nScore:", total_score) #prints total score 

    return total_score

def win_lose_or_draw(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        print("Draw")
    elif player_score > 21 and dealer_score <= 21:
        print("Dealer wins")
    elif player_score <= 21 and dealer_score > 21:
        print("You win")
    else:
        if player_score > dealer_score:
            print("You win")
        elif dealer_score > player_score:
                print("Dealer wins")
        else:
            print("Draw")

def dealer_hit_or_stand(player_hand, dealer_hand):
    dealer_score = hand_score(dealer_hand)
    player_score = hand_score(player_hand)
    if dealer_score < 17 or dealer_score < player_score:
        print("Dealer hits...")
        return True
    else:
        print("Dealer stands.")
        return False

def player_hit_or_stand():
    input_user = input("Enter 'H' (or 'h') to hit or 'S' (or 's') to stand: ") #input from user
    h_or_s = input_user.upper() #converts string to uppercase
    while h_or_s != 'H' and h_or_s != 'S': #loops until user enters a valid input ('H' or 'S' or 'h' or 's')
        input_user1 = input("Enter 'H' (or 'h') to hit or 'S' (or 's') to stand: ")
        h_or_s = input_user1.upper()
    
    if h_or_s == 'H':
        print("Player hits...")
        return True 
    else:
        print("Player stands.")
        return False

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    dealer_name = "Dealer"

    deck = cards.make_deck(cards.make_card)
    shuffled_deck = cards.shuffle(deck)

    top_half, bottom_half = cards.cut(shuffled_deck)

    player_hand, dealer_hand = cards.deal(bottom_half, 2)

    player_score = print_hand_and_score(player_name, player_hand)
    print("\n")
    dealer_score = print_hand_and_score(dealer_name, dealer_hand)

    print("\n")
    player_decision = player_hit_or_stand()
    
    if player_decision == True:
        player_hand_2 = cards.draw(bottom_half, player_hand)

    player_score = print_hand_and_score(player_name, player_hand_2)

    print("\n")
    dealer_decision = dealer_hit_or_stand(player_hand_2, dealer_hand)

    if dealer_decision == True:
        dealer_hand_2 = cards.draw(bottom_half, dealer_hand)

    dealer_score = print_hand_and_score(dealer_name, dealer_hand_2)

    print("\n")
    win_lose_or_draw(player_score, dealer_score)