############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random


new_game = True
while new_game:
    print(logo)
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_deck = []
    opp_deck = []
    
    def total(list):
        sum = 0
        for i in list :
            sum += i   
        return sum
    
    ## 2 bana 2 kasaya
    ##my_deck.append(random.choice(cards))
    ##my_deck.append(random.choice(cards))
    my_deck.append(11)
    my_deck.append(11)
    
    opp_deck.append(random.choice(cards))
    opp_deck.append(random.choice(cards))
    
    print(f"My deck: {my_deck[0]}, {my_deck[1]}")
    print(f"Computer: {opp_deck[0]}, x")
    
    ###..............FLAG - 1
    if total(my_deck) == 21:
        print("You hit the BLACKJACK!!!")
    else:
        ## Part 2 - Card picking
        new_card = "yes"
        end_game = False

        while new_card == "yes" and not end_game:
            new_card = input("Wanna pick a card? Type 'yes' or 'no': ")
            if(new_card == "yes"):
                my_deck.append(random.choice(cards))
                print(f"My deck: {my_deck}")

            if total(my_deck)>21:
                ace_change = False
                ########...............ACE CHANGE...........#######
                for i in my_deck :
                    if i == 11 and total(my_deck) > 21:
                        my_deck[my_deck.index(i)] = 1
                        ace_change = True
                        print(f"My deck: {my_deck}")
                        
                if not ace_change:
                    print("BUST... You lose")
                    end_game = True
            elif total(my_deck) == 21:
                print("You hit the BLACKJACK!!!")
                end_game = True
    
        ### Part 3 - opponent's turn
        while total(opp_deck) < 17 and not end_game:
            opp_deck.append(random.choice(cards))
            if total(opp_deck)>21: 
                ace_change = False
                ########...............ACE CHANGE...........#######
                for i in opp_deck :
                    if i == 11 and total(opp_deck) > 21:
                        opp_deck[opp_deck.index(i)] = 1
                        ace_change = True

                if not ace_change:
                    end_game = True
                    print(f"Computer: {opp_deck}")
                    print("Computer BUST...You WON!!!")
            elif total(opp_deck)== 21:
                end_game = True
                print(f"Computer: {opp_deck}")
                print("Computer hit the BLACKJACK...You LOSE!!!")
        
        ###Part 4 - Who is closer?
        if not end_game:
            print(f"My deck: {my_deck}")
            print(f"Computer: {opp_deck}")
            my_total = total(my_deck)
            opp_total = total(opp_deck)
            
            if my_total > opp_total :
                print("You WIN...")
            elif opp_total > my_total:
                print("You LOSE...")
            else:
                print("Draw...")

    again = input("Wanna play again? Type yes/no: ").lower()
    if again == "no":
        print("Bye..")
        new_game = False
        
print("...game over...") 

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

