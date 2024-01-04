#rock-paper-scissors game
import random
print("-"*50,"Lets play rock-paper-scissors!!!","-"*50)
choices = ['r','s','p']

user_score = 0
comp_score = 0
while True:
    print("-"*134)
    u_score = c_score = 0
    #user input
    user_choice = input("Enter 'r' for rocks, 'p' for paper and 's' for scissors : ")
    #computer selection
    comp_choice = random.choice(choices)
    
    #rock beats scissors, scissors beat paper, paper beats rock
    print(f"User's choice : {user_choice}\nComputer's choice : {comp_choice}")
    if user_choice == 'r':
        if comp_choice =='s':
            u_score = 1
        elif comp_score == 'p':
            c_score = 1

    elif user_choice == 's':
        if comp_choice == 'r':
            c_score = 1
        elif comp_choice == 'p':
            u_score = 1

    elif user_choice == 'p':
        if comp_choice == 's':
            c_score = 1
        elif comp_choice == 'r':
            u_score = 1

    else:
        print("ALERT : You have entered an invalid choice.")
        break

        
    print("RESULT ->")
    if u_score > c_score:
        user_score += 1
        print("Hurray!! You won the game this time :)")
    elif u_score < c_score:
        comp_score += 1
        print("Oops!! You lost this time :(")
    else:
        print("Its a tie..")

    

    ch = input("Do you want to play again (yes/no)? ")
    if ch.lower() == 'no':
        break

print("-"*134)
print("FINAL RESULTS -->>")
print("Your scores : ",user_score)
print("Computer scores : ",comp_score)
print("THANK YOU FOR PLAYING....")
            
        



