import blackjack

def test_hand_score():
    exp = 16
    hand = ["5D", "10S", "AS"]
    res = blackjack.hand_score(hand)
    assert exp == res

def test_dealer_hit_or_stand():
    player_hand = ["5D", "10S"]
    dealer_hand = ["2S", "JC"]
    exp = True
    res = blackjack.dealer_hit_or_stand(player_hand, dealer_hand)
    assert exp == res