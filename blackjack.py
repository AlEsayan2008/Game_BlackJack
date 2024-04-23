import random

BlackJack_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 20]

# Your numbers:

Your_first_number = random.choice(BlackJack_numbers)
Your_second_number = random.choice(BlackJack_numbers)

# Dealer's numbers:

Dealer_first_number = random.choice(BlackJack_numbers)
Dealer_second_number = random.choice(BlackJack_numbers)

# Your & Dealer cash:
Your_cash = 10000
Dealer_cash = 10000


def checking_your_balance():
    if Your_cash <= 0:
        print("You lose. Try again.")

def checking_diller_balance():
    if Dealer_cash <= 0:
        print("You win this game!")


while True:
    your_choice = input(f"\nYour numbers are {Your_first_number} and {Your_second_number}: Choose please Fold or Continue:\n")
    if your_choice.lower() == "fold":
        Your_cash -= 100
        print(f"Your cash is equal to: {Your_cash}")
        
    elif your_choice.lower() == "continue":
        if (Your_first_number + Your_second_number) < 21:
            if Your_first_number + Your_second_number == Dealer_first_number + Dealer_second_number:
                print("This round is finished by a tie.")
            elif Your_first_number + Your_second_number > Dealer_first_number + Dealer_second_number:
                Your_cash += 500
                Dealer_cash -= 500
                print(f"You win this round!: sum of your card: {Your_first_number + Your_second_number} is higher than dealer's card sum: {Dealer_first_number + Dealer_second_number}")
                print(f"Your cash is equal to: {Your_cash}")
                print(f"Dealer's cash is equal to: {Dealer_cash}")
            else:
                Your_cash -= 500
                Dealer_cash += 500
                print("Dealer wins this round.")
                print(f"You loose this round!: sum of your card: {Your_first_number + Your_second_number} is lower than dealer's card sum: {Dealer_first_number + Dealer_second_number}")
                print(f"Your cash is equal to: {Your_cash}")
                print(f"Dealer's cash is equal to: {Dealer_cash}")
        else:
            Your_cash -= 50
            print("Sorry, the sum of your numbers is higher than 21.")
            print(f"Your cash is equal to: {Your_cash}")
        break
    else:
        print("Invalid input. Please choose 'Fold' or 'Continue'.")

    if checking_your_balance():
        print()
        break
    if checking_diller_balance:
        print()
        break
