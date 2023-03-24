# Nicholas Palceski
# This program will give accurate information regarding players Rocket League
# career statistics.
# SPRINT 1
# ** --> 6**3 is 6 to the power of 3 which is 216
# * used
# / used
# % used
# // used
# + used
# - used
# sep="" used
# end="" brings together strings on separate lines and only put special
# character between the strings rather than sep= which puts special character
# between the words in a string.
# SPRINT 2
# x += 1 is a shortcut operator for x = x + 1 (Can be used with subtraction
# and multiplication as well)
# if else statements used
# != (not equal) is the same as function "not" (not equal) except "not"
# function returns a boolean expression whether two variables are equal or not.
# that's why != is a relation operator and "not" function is a boolean operator
# "and" operator checks if two conditions are met to then run a computation of
# code.
# "or" used
# while loop used
# for loops are used when you know how many times you want to loop a segment of
# code. EX: for x in range(1, 11): will do a thing a code for x from 1-10
# def functions used with parameters


# lists of ranks (global assignments)
all_bronze = ["Bronze 1", "Bronze 2", "Bronze 3"]
all_silver = ["Silver 1", "Silver 2", "Silver 3"]
all_gold = ["Gold 1", "Gold 2", "Gold 3"]
all_plat = ["Plat 1", "Plat 2", "Plat 3"]
all_dia = ["Diamond 1", "Diamond 2", "Diamond 3"]
all_champ = ["Champ 1", "Champ 2", "Champ 3"]
all_gc = ["Grand Champ 1", "Grand Champ 2", "Grand Champ 3"]
ssl = ["Supersonic Legend"]


# calculates MMR based on rank and game mode selected.
def calculate_mmr(r, gm):
    while gm == "1v1" or gm == "2v2" or gm == "3v3":
        if gm == "1v1":
            if r == "bronze 1" or r == "Bronze 1":
                print("Your estimate MMR for ranked 1v1: -100")
                break
            elif r == "bronze 2" or r == "Bronze 2":
                print("Your estimate MMR for ranked 1v1: 145")
                break
            elif r == "bronze 3" or r == "Bronze 3":
                print("Your estimate MMR for ranked 1v1: 210")
                break
            elif r == "silver 1" or r == "Silver 1":
                print("Your estimate MMR for ranked 1v1: 275")
                break
            elif r == "silver 2" or r == "Silver 2":
                print("Your estimate MMR for ranked 1v1: 335")
                break
            elif r == "silver 3" or r == "Silver 3":
                print("Your estimate MMR for ranked 1v1: 395")
                break
            elif r == "gold 1" or r == "Gold 1":
                print("Your estimate MMR for ranked 1v1: 455")
                break
            elif r == "gold 2" or r == "Gold 2":
                print("Your estimate MMR for ranked 1v1: 515")
                break
            elif r == "gold 3" or r == "Gold 3":
                print("Your estimate MMR for ranked 1v1: 575")
                break
            elif r == "plat 1" or r == "Plat 1":
                print("Your estimate MMR for ranked 1v1: 635")
                break
            elif r == "plat 2" or r == "Plat 2":
                print("Your estimate MMR for ranked 1v1: 695")
                break
            elif r == "plat 3" or r == "Plat 3":
                print("Your estimate MMR for ranked 1v1: 755")
                break
            elif r == "diamond 1" or r == "Diamond 1":
                print("Your estimate MMR for ranked 1v1: 815")
                break
            elif r == "diamond 2" or r == "Diamond 2":
                print("Your estimate MMR for ranked 1v1: 875")
                break
            elif r == "diamond 3" or r == "Diamond 3":
                print("Your estimate MMR for ranked 1v1: 935")
                break
            elif r == "champ 1" or r == "Champ 1":
                print("Your estimate MMR for ranked 1v1: 995")
                break
            elif r == "champ 2" or r == "Champ 2":
                print("Your estimate MMR for ranked 1v1: 1055")
                break
            elif r == "champ 3" or r == "Champ 3":
                print("Your estimate MMR for ranked 1v1: 1115")
                break
            elif r == "grand champ 1" or r == "Grand Champ 1":
                print("Your estimate MMR for ranked 1v1: 1175")
                break
            elif r == "grand champ 2" or r == "Grand Champ 2":
                print("Your estimate MMR for ranked 1v1: 1231")
                break
            elif r == "grand champ 3" or r == "Grand Champ 3":
                print("Your estimate MMR for ranked 1v1: 1287")
                break
            elif r == "supersonic legend" or r == "Supersonic Legend":
                print("Your estimate MMR for ranked 1v1: 1343+")
                break
            else:
                print("Please enter a valid rank.")
                r = input("Enter competitive rank: ")
        # output est. MMR for ranked 2v2
        elif gm == "2v2":
            if r == "bronze 1" or r == "Bronze 1":
                print("Your estimate MMR for ranked 2v2: -100")
                break
            elif r == "bronze 2" or r == "Bronze 2":
                print("Your estimate MMR for ranked 2v2: 175")
                break
            elif r == "bronze 3" or r == "Bronze 3":
                print("Your estimate MMR for ranked 2v2: 223")
                break
            elif r == "silver 1" or r == "Silver 1":
                print("Your estimate MMR for ranked 2v2: 292")
                break
            elif r == "silver 2" or r == "Silver 2":
                print("Your estimate MMR for ranked 2v2: 349")
                break
            elif r == "silver 3" or r == "Silver 3":
                print("Your estimate MMR for ranked 2v2: 415")
                break
            elif r == "gold 1" or r == "Gold 1":
                print("Your estimate MMR for ranked 2v2: 474")
                break
            elif r == "gold 2" or r == "Gold 2":
                print("Your estimate MMR for ranked 2v2: 535")
                break
            elif r == "gold 3" or r == "Gold 3":
                print("Your estimate MMR for ranked 2v2: 591")
                break
            elif r == "plat 1" or r == "Plat 1":
                print("Your estimate MMR for ranked 2v2: 654")
                break
            elif r == "plat 2" or r == "Plat 2":
                print("Your estimate MMR for ranked 2v2: 713")
                break
            elif r == "plat 3" or r == "Plat 3":
                print("Your estimate MMR for ranked 2v2: 773")
                break
            elif r == "diamond 1" or r == "Diamond 1":
                print("Your estimate MMR for ranked 2v2: 835")
                break
            elif r == "diamond 2" or r == "Diamond 2":
                print("Your estimate MMR for ranked 2v2: 915")
                break
            elif r == "diamond 3" or r == "Diamond 3":
                print("Your estimate MMR for ranked 2v2: 995")
                break
            elif r == "champ 1" or r == "Champ 1":
                print("Your estimate MMR for ranked 2v2: 1075")
                break
            elif r == "champ 2" or r == "Champ 2":
                print("Your estimate MMR for ranked 2v2: 1195")
                break
            elif r == "champ 3" or r == "Champ 3":
                print("Your estimate MMR for ranked 2v2: 1315")
                break
            elif r == "grand champ 1" or r == "Grand Champ 1":
                print("Your estimate MMR for ranked 2v2: 1435")
                break
            elif r == "grand champ 2" or r == "Grand Champ 2":
                print("Your estimate MMR for ranked 2v2: 1575")
                break
            elif r == "grand champ 3" or r == "Grand Champ 3":
                print("Your estimate MMR for ranked 2v2: 1713")
                break
            elif r == "supersonic legend" or r == "Supersonic Legend":
                print("Your estimate MMR for ranked 2v2: 1862+")
                break
            else:
                print("Please enter a valid rank.")
                r = input("Enter comp rank: ")
        # output est. MMR for ranked 3v3
        elif gm == "3v3":
            if r == "bronze 1" or r == "Bronze 1":
                print("Your estimate MMR for ranked 3v3: -100")
                break
            elif r == "bronze 2" or r == "Bronze 2":
                print("Your estimate MMR for ranked 1v1: 171")
                break
            elif r == "bronze 3" or r == "Bronze 3":
                print("Your estimate MMR for ranked 1v1: 235")
                break
            elif r == "silver 1" or r == "Silver 1":
                print("Your estimate MMR for ranked 1v1: 295")
                break
            elif r == "silver 2" or r == "Silver 2":
                print("Your estimate MMR for ranked 1v1: 355")
                break
            elif r == "silver 3" or r == "Silver 3":
                print("Your estimate MMR for ranked 1v1: 415")
                break
            elif r == "gold 1" or r == "Gold 1":
                print("Your estimate MMR for ranked 1v1: 475")
                break
            elif r == "gold 2" or r == "Gold 2":
                print("Your estimate MMR for ranked 1v1: 535")
                break
            elif r == "gold 3" or r == "Gold 3":
                print("Your estimate MMR for ranked 1v1: 595")
                break
            elif r == "plat 1" or r == "Plat 1":
                print("Your estimate MMR for ranked 1v1: 655")
                break
            elif r == "plat 2" or r == "Plat 2":
                print("Your estimate MMR for ranked 1v1: 715")
                break
            elif r == "plat 3" or r == "Plat 3":
                print("Your estimate MMR for ranked 1v1: 775")
                break
            elif r == "diamond 1" or r == "Diamond 1":
                print("Your estimate MMR for ranked 1v1: 835")
                break
            elif r == "diamond 2" or r == "Diamond 2":
                print("Your estimate MMR for ranked 1v1: 915")
                break
            elif r == "diamond 3" or r == "Diamond 3":
                print("Your estimate MMR for ranked 1v1: 995")
                break
            elif r == "champ 1" or r == "Champ 1":
                print("Your estimate MMR for ranked 1v1: 1075")
                break
            elif r == "champ 2" or r == "Champ 2":
                print("Your estimate MMR for ranked 1v1: 1195")
                break
            elif r == "champ 3" or r == "Champ 3":
                print("Your estimate MMR for ranked 1v1: 1315")
                break
            elif r == "grand champ 1" or r == "Grand Champ 1":
                print("Your estimate MMR for ranked 1v1: 1435")
                break
            elif r == "grand champ 2" or r == "Grand Champ 2":
                print("Your estimate MMR for ranked 1v1: 1575")
                break
            elif r == "grand champ 3" or r == "Grand Champ 3":
                print("Your estimate MMR for ranked 1v1: 1707")
                break
            elif r == "supersonic legend" or r == "Supersonic Legend":
                print("Your estimate MMR for ranked 1v1: 1861+")
                break
            else:
                print("Please enter a valid rank.")
                r = input("Enter competitive rank: ")


def get_time(t_g):
    # every RL game is roughly 5-6 minutes.
    # NEED TO CALCULATE MINUTES TO HOURS AND DAYS
    minutes = t_g * 5.5
    hours = minutes // 60
    days = hours // 24
    minutes_left = minutes % 60
    hours_left = hours % 24
    # output est. total time played.
    print("In-Game:\n", days, "d :", hours_left, "h :", minutes_left, "m")


def main():
    # greeting
    print("Greetings!\nWelcome to my Rocket League inspired program!")
    # Choose game mode (each game mode calculates MMR differently)
    print("-----[ Rocket League MMR ]-----")
    print("        1v1 , 2v2 , 3v3")
    game_mode = input("Enter a game mode: ")
    # Ask for list of ranks (if user does not know)
    know_rank = input("Want to see a list of the ranks? (yes/no): ")
    while True:
        if know_rank == "Yes" or know_rank == "yes":
            print("-" * 31)
            print('   '.join(all_bronze), "\n", '   '.join(all_silver))
            print('   '.join(all_gold), "\n", '   '.join(all_plat))
            print('   '.join(all_dia), "\n", '   '.join(all_champ))
            print('   '.join(all_gc), "\n", '   '.join(ssl))
            print("-" * 31)
            break
        elif know_rank == "No" or know_rank == "no":
            print("Great! You know your rank!")
            break
        else:
            print("Please enter a valid response.")
            know_rank = input("Want to see a list of the ranks? ")
    # Enter rank in rocket league. (22 total ranks)
    rank = input("Enter competitive rank: ")
    calculate_mmr(rank, game_mode)
    # separates program --> easier to read.
    print("------[ Statistics ]------")
    # Enter if you want more statistics. (yes/no)
    want_stats = input("Want to see additional stats? (yes/no): ")
    # Gets statistics input and checks it.
    while True:
        if want_stats == "yes" or want_stats == "Yes":
            # Ask for inputs from user before displaying output.
            total_games = float(input("Enter total # games played: "))
            games_won = float(input("Enter # games won: "))
            total_shots = float(input("Enter # of shots on goal: "))
            total_goals = float(input("Enter # of goals: "))
            # Check if total_games is a number and not a string.
            if type(total_games) == float or type(total_games) == int:
                pass
            else:
                print("Please enter a valid number.")
                total_games = float(input("Enter total # of games played: "))
            # Check if games_won is a number and not a string.
            if type(games_won) == int or type(games_won) == float:
                pass
            else:
                print("Please enter valid # of games won.")
                games_won = float(input("Enter # of games won: "))
            # Check if total_shots is a number and not  a string.
            if type(total_shots) == float or type(total_shots) == int:
                pass
            else:
                print("Please enter valid shots on goal.")
                total_shots = float(input("Enter # of shots taken: "))
            # Check if total_goals is a number and not a string.
            if type(total_goals) == float or type(total_goals) == int:
                pass
            else:
                print("Please enter valid goals.")
                total_goals = float(input("Enter total # of goals: "))
            # prints the string 31 times.
            print("-" * 31)
            get_time(total_games)
            # output games lost.
            games_lost = total_games - games_won
            print("Total games lost:", format(games_lost, '.0f'))
            # output total shots missed.
            shots_missed = total_shots - total_goals
            # format to remove decimal places.
            print("Total shots missed:", format(shots_missed, '.0f'))
            print("-" * 31)
            want_stats = input("Want to reenter stats? ")
        # if user want no additional stats
        elif want_stats == "no" or want_stats == "No":
            print("    Thank you for using our program,")
            print("          Goodbye!")
            break
        else:
            # concatenate two strings together then separates the strings
            # with a space.
            print("Please enter" + "a valid answer.", sep=" ")
            want_stats = input("Want additional stats? ")


main()
