"""Loesung fuer Problem 54 von Projekt Euler. Meistens kommt richtiges Ergeb von 376 herraus
manchmal kommt 377 aus unbekannten Gruenden raus moeglciher Grund ist Listenabrollen 
bei der for-schleife ueber Funktionen""" 

def to_card(x):
    return card(x[0],x[1])
    
class card():
    def __init__(self,value,suit):
        self.suit = suit
        if(value == 'T'):
            self.value = 10
        elif(value == 'J'):
            self.value = 11
        elif(value == 'Q'):
            self.value = 12
        elif(value == 'K'):
            self.value = 13
        elif(value == 'A'):
            self.value = 14
        else:
            self.value = int(value)
            
    def to_str(self):
        return str(self.suit) + ":" + str(self.value) 
        
def card_compare(card1, card2):
    if card1.value < card2.value:
        return -1
    elif card1.value > card2.value:
        return 1
    else: return 0

def highest_card(list_hand):
    list_hand = sorted(list_hand, cmp=card_compare)
    return list_hand[0]

def check_flush(list_hand):
    s = list_hand[0].suit
    for c in list_hand:
        if c.suit != s:
            return (False,0)
    return (True,highest_card(list_hand))
    
def check_pair(list_hand):
    for c in list_hand:
        temp_list = list(list_hand)
        temp_list.remove(c)
        for a in temp_list:
            if a.value == c.value:
                return (True,(a,c))
    dummy = card(0,0)
    return (False,(dummy,dummy))

def check_three(list_hand):
    for c in list_hand:
        temp_list = list(list_hand)
        temp_list.remove(c)
        two = False
        for a in temp_list:
            if a.value == c.value and not two:
                two = True
            elif a.value == c.value and two:
                return (True,a.value)
    return (False,0)

def check_four(list_hand):
    for c in list_hand:
        temp_list = list(list_hand)
        temp_list.remove(c)
        count = 1
        for a in temp_list:
            if a.value == c.value and count < 3:
                count += 1
            elif a.value == c.value and count == 3:
                return (True,a.value)
    return (False,0)

def check_straight(list_hand):
    list_hand = sorted(list_hand, cmp=card_compare)
    last = list_hand[0].value
    for i in range(1,len(list_hand)):
        if list_hand[i].value != last + 1:
            return (False,0)
        last = list_hand[i].value
    return (True,highest_card(list_hand))

def check_full_house(list_hand):
    b,(c1,c2) = check_pair(list_hand)
    if b == False:
        return (False,0)
    temp_list = list(list_hand)
    temp_list.remove(c1)
    temp_list.remove(c2)
    b,r = check_three(temp_list)
    return (b,r)
    
def check_straight_flush(list_hand):
    b,rank = check_straight(list_hand)
    return (check_flush(list_hand) and b), rank
    
def check_royal_flush(list_hand):
    return (check_straight_flush(list_hand) and highest_card(list_hand).value == 14),14

def check_two_pairs(list_hand):
    b,(c1,c2) = check_pair(list_hand)
    if b == False:
        return (False,0)
    temp_list = list(list_hand)
    temp_list.remove(c1)
    temp_list.remove(c2)
    rank1 = c2.value
    b,rank2 = check_pair(temp_list)
    return (b,max(rank1,rank2))

def read_hands(filename):
    f = open(filename,'r')
    hands = []
    for line in f:
        cards = line.split(' ')
        h1 = [to_card(cards[i]) for i in range(0,5)]
        h2 = [to_card(cards[i]) for i in range(5,10)]
        hands.append((h1,h2))
    return hands

def print_hand(h):
    string  = ""
    for c in h:
        string += c.to_str() + "|"
    print string

def cmp_hands(h1, h2): #returns whether h1 is better than h2
    
    funcs = [check_royal_flush, check_straight_flush, 
             check_four, check_full_house, check_flush, check_straight, check_three, check_two_pairs, check_pair]

    for func in funcs:
        #print func.__name__
        b1, r1 = func(h1)
        b2, r2 = func(h2)
        if (func == check_pair):
            c1,c2 = r1
            r1 = c1.value
            c1,c2 = r2
            r2 = c1.value
            
        if b1 and not b2:
                return True
        elif b2 and not b1:
                return False
        elif b1 and b2:
            #print "lvl1 " +  func.__name__
            if r1 > r2:
                return True
            elif r1 < r2:
                return False
            else:
                #print func.__name__
                #print_hand(h1)
                #print_hand(h2)
                return highest_card(h1) > highest_card(h2)
                                
    # highest card has to decide
    h1 = sorted(h1, cmp=card_compare)
    h2 = sorted(h2, cmp=card_compare)
    #print_hand(h1)
    #print_hand(h2)
    i = len(h1) - 1       
    while h1[i].value == h2[i].value:
        i -= 1
    #print h1[i].value > h2[i].value
    return h1[i].value > h2[i].value
    
hands = read_hands('prob54file')
i = 0
print "read " + str(len(hands)) + " pokerhands"

for h1,h2 in hands:
    if cmp_hands(h1,h2):
        i += 1
    
print "hand 1 wins: " + str(i)