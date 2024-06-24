import random
def find_winner(user_choice,computer_choice):
    rules={('rock','scissors'):'User',('scissors','paper'):'User',('paper','rock'):'User',('scissors','rock'):'Computer',('paper','scissors'):'Computer',('rock','paper'):'Computer'}
    if user_choice==computer_choice:
        return "It's a tie!"
    elif (user_choice,computer_choice)in rules:
        return f"{rules[user_choice,computer_choice]} wins!"
    else:
        return f"{rules[computer_choice,user_choice]} wins!"
def main():
    user_score=0
    computer_score=0
    choices=['rock','paper','scissors']
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Choose: rock, paper, or scissors")
        user_choice=input("Your choice: ").lower()
        while user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice=input("Your choice: ").lower()
        computer_choice=random.choice(choices)
        result=find_winner(user_choice,computer_choice)
        print("\nUser's choice:", user_choice.capitalize())
        print("Computer's choice:", computer_choice.capitalize())
        print("\nResult:", result)
        if result.startswith('User'):
            user_score+=1
        elif result.startswith('Computer'):
            computer_score+=1
        print("\nCurrent Scores - User:", user_score, "Computer:", computer_score)
        play_again=input("\nDo you want to play again? yes/no: ").lower()
        if play_again!='yes':
            print("Thanks for playing!")
            break
main()
