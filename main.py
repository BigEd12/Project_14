from art import logo
from art import vs
import random
from game_data import data

end_of_game = 0
user_score = 0


def random_number():
    """Returns a random entry from data"""
    return random.choice(data)


def comparison(input_a, input_b, choice):
    global user_score
    global end_of_game
    followers_a = input_a["follower_count"]
    followers_b = input_b["follower_count"]
    name_a = input_a["name"]
    name_b = input_b["name"]
    print(f"{name_a} has {followers_a} million followers and {name_b} has {followers_b} million followers.")
    if followers_a > followers_b and choice == "a":
        user_score += 1
        return f"You are correct. Well done\nYour current score is {user_score}"
    elif followers_a < followers_b and choice == "b":
        user_score += 1
        return f"You are correct. Well done.\nYour current score is {user_score}"
    else:
        end_of_game = 1
        return f"You are incorrect. Game over.\nYour final score is {user_score}"


def game_play():
    global game_in_play
    print(
        f"{logo}\nWelcome to the Higher Lower game.\nYou have to guess which person or organisation has the most followers on Instagram.")
    one = random_number()
    two = random_number()
    one_name = one["name"]
    one_description = one["description"]
    one_country = one["country"]
    two_name = two["name"]
    two_description = two["description"]
    two_country = two["country"]
    choice = input(
        f"Compare A: {one_name}, a {one_description} from {one_country}\n{vs}\nAgainst B: {two_name}, a {two_description} from {two_country}.\n")
    print(f"{comparison(one, two, choice)}")
    while end_of_game != 1:
        one = two
        two = random_number()
        one_name = one["name"]
        one_description = one["description"]
        one_country = one["country"]
        two_name = two["name"]
        two_description = two["description"]
        two_country = two["country"]
        choice = input(
            f"Compare A: {one_name}, a {one_description} from {one_country}\n{vs}\nAgainst B: {two_name}, a {two_description} from {two_country}.\n")
        print(f"{comparison(one, two, choice)}")


while end_of_game != 1:
    game_play()
