__author__ = "Nicholas Palceski"
"""
Nicholas Palceski

This program will give accurate information regarding players Rocket League
career statistics.
"""

# lists of ranks (global assignments)
all_bronze = ["Bronze 1", "Bronze 2", "Bronze 3"]
all_silver = ["Silver 1", "Silver 2", "Silver 3"]
all_gold = ["Gold 1", "Gold 2", "Gold 3"]
all_plat = ["Plat 1", "Plat 2", "Plat 3"]
all_dia = ["Diamond 1", "Diamond 2", "Diamond 3"]
all_champ = ["Champ 1", "Champ 2", "Champ 3"]
all_gc = ["Grand Champ 1", "Grand Champ 2", "Grand Champ 3"]
ssl = ["Supersonic Legend"]


def print_sprint_req():
    """
    Prints sprint requirements.
    """
    print("--- SPRINT REQUIREMENTS ---")
    print()
    print("** --> 6**3 is 6 to the power of 3 which is 216")
    print("* used")
    print("/ used")
    print("% used")
    print("// used")
    print("+ used")
    print("- used")
    print("sep='' used")
    print("'or' used")
    print("while loop used")
    print("def functions used")
    print("end="" brings together strings on separate lines and only ")
    print("put special character between the strings rather than sep= which ")
    print("puts special character between the words in a string.")
    print("x = 1")
    print("x += 1 = 2")
    print("If / else statement used")
    print("realMoney = True")
    print("if money != realMoney:")
    print("    return False")
    print("'not' functions return a boolean expression whether two variables")
    print("are equal or not.")
    print("for x in range(1, 11):")
    print("  print(x)")
    print("prints the value of x 1 through 10.")
    for x in range(1, 11):
        print(x)
    print("-"*31)


def print_greetings():
    """
    Prints greeting to program and introduces UI.
    """
    print("Greetings!\nWelcome to my Rocket League inspired program!")
    print("-----[ Rocket League MMR ]-----")
    print("        1v1 , 2v2 , 3v3")


def print_ranks():
    """
    Print the list of all the ranks in Rocket League.
    """
    print("-" * 31)
    print('   '.join(all_bronze), "\n", '   '.join(all_silver))
    print('   '.join(all_gold), "\n", '   '.join(all_plat))
    print('   '.join(all_dia), "\n", '   '.join(all_champ))
    print('   '.join(all_gc), "\n", '   '.join(ssl))
    print("-" * 31)


def calculate_mmr(r, gm):
    """
    Calculates Matchmaking Rank (MMR) based on one of the available game modes.
    Parameters:
            r (str): Rank that user chooses from options.
            gm (str): Game mode that user chooses from options.
    Returns:
        Print statement that gives estimate MMR.
    """
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


def print_statistics_format():
    """
    Prints format to separate program to next section.
    """
    print("------[ Statistics ]------")


def get_stats(ws):
    """
    Gets extra statistics that the user inputs if they decide.
    Parameters:
            ws (str): Asks user if they want to see additional stats.
    Returns:
        Statistics that user wants to see.
    """
    while True:
        if ws == "yes" or ws == "Yes":
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
            get_time(int(total_games))
            # output games lost.
            games_lost = total_games - games_won
            print("Total games lost:", format(games_lost, '.0f'))
            # output total shots missed.
            shots_missed = total_shots - total_goals
            # format to remove decimal places.
            print("Total shots missed:", format(shots_missed, '.0f'))
            print("-" * 31)
            ws = input("Want to reenter stats? ")
        # if user want no additional stats
        elif ws == "no" or ws == "No":
            print("    Thank you for using our program,")
            print("          Goodbye!")
            break
        else:
            # concatenate two strings together then separates the strings
            # with a space.
            print("Please enter" + "a valid answer.", sep=" ")
            ws = input("Want additional stats? ")


def get_time(t_g):
    """
    Gets the total time played by converting the minutes to days and hours.
    Every Rocket League game is roughly 5-6 minutes.
            Parameters:
                    t_g (int): Total games played.
            Returns:
                Print statement that gives an estimate time played in-game.
    """
    minutes = t_g * 5.5
    hours = minutes // 60
    days = hours // 24
    minutes_left = minutes % 60
    hours_left = hours % 24
    print("In-Game:\n", days, "d :", hours_left, "h :", minutes_left, "m")


def main():
    """
    Calculates MMR based on rank and game mode entered for Rocket League.
    Can show additional statistics if user chooses to do so.
    Additional statistics such as games lost, goals missed, total time in-game,
    etc.
    """
    print_sprint_req()
    print_greetings()
    game_mode = input("Enter a game mode: ")
    print_ranks()
    rank = input("Enter competitive rank: ")
    calculate_mmr(rank, game_mode)
    print_statistics_format()
    want_stats = input("Want to see additional stats? (yes/no): ")
    get_stats(want_stats)


if __name__ == "__main__":
    main()
