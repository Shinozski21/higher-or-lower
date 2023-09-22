from art import logo, vs
from game_data import data
import random
#from replit import clear

print(logo)


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        against_b = random.choice(data)


    def format_data(account):
        acct_name = account["name"]
        acct_desc = account["description"]
        acct_country = account["country"]
        return f"{acct_name} a/an {acct_desc} from {acct_country}."


    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")


    guess = input("Which one has more follower? Type A or B: ").lower()
    # def games():
    #     if compare(compare_a[int(['follower_count'])) > against(against_b['follower_count']) and guess_answer == "A":
    #         print("You win!")
    #     elif compare(compare_a['follower_count']) < against(against_b['follower_count']) and guess_answer == "B":
    #         print("You win!")
    #     return score()
    #games()


    def check_answer(guess, a_followers, b_followers):
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    #clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right: Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
 