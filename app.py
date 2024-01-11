import copy

from constants import *


panthers = []
warriors = []
bandits = []
experienced_players = []
inexperienced_players = []


def cleaned_data(new_data):
    # Height
    for data in new_data:
        new_height = data['height'].split()
        if new_height and new_height[0].isnumeric():
            data['height'] = int(new_height[0])
    # Experience
        if data["experience"] == "YES":
            data["experience"] = True
        else:
            data["experience"] = False
    # Guardians
        data["guardians"] = data["guardians"].split(" and ")


def sort_experience(data):
    for player in data:
        if player["experience"] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)


def balance_teams():
    # balance the teams by experience and equally, and sort by height
    # experienced players
    panthers.extend(experienced_players[:3])
    warriors.extend(experienced_players[3:6])
    bandits.extend(experienced_players[6:9])
    # inexperienced players
    panthers.extend(inexperienced_players[:3])
    warriors.extend(inexperienced_players[3:6])
    bandits.extend(inexperienced_players[6:9])
    # sort by height
    panthers.sort(key=lambda player: player["height"], reverse=True)
    warriors.sort(key=lambda player: player["height"], reverse=True)
    bandits.sort(key=lambda player: player["height"], reverse=True)


def game_menu():
    print("BASKETBALL TEAM STATS")
    print("---- MENU----")
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    menu_choice = input("Enter an option > ")
    if menu_choice == "1":
        print("1) Panthers")
        print("2) Warriors")
        print("3) Bandits")
        team_choice = input("Enter an option > ")
        if team_choice == "1":
            print("Team: Panthers Stats")
            print("--------------------")
            print("Players on Team: ")
            print(", ".join([player["name"] for player in panthers]))
            print("Guardians: ")
            print(", ".join([", ".join(player["guardians"])
                  for player in panthers]))
            print("Total players: {}".format(len(panthers)))
            print("Total Experienced Players: {}".format(
                len(experienced_players[:3])))
            print("Total Inexperienced Players: {}".format(
                len(inexperienced_players[:3])))
            print("Average Height: ")
            print(round(sum([player["height"]
                  for player in panthers]) / len(panthers), 2))
            # create an option to return to menu
            print("Press ENTER to return to menu")
            if input() == "":
                game_menu()

        elif team_choice == "2":
            print("Team: Warriors Stats")
            print("--------------------")
            print("Players on Team: ")
            print(", ".join([player["name"] for player in warriors]))
            print("Guardians: ")
            print(", ".join([", ".join(player["guardians"])
                  for player in warriors]))
            print("Total players: {}".format(len(warriors)))
            print("Total Experienced Players: {}".format(
                len(experienced_players[:3])))
            print("Total Inexperienced Players: {}".format(
                len(inexperienced_players[:3])))
            print("Average Height: ")
            print(round(sum([player["height"]
                  for player in warriors]) / len(warriors), 2))
            # create an option to return to menu
            print("\n Press ENTER to return to menu")
            if input() == "":
                game_menu()
        elif team_choice == "3":
            print("Team: Bandits Stats")
            print("--------------------")
            print("Players on Team: ")
            print(", ".join([player["name"] for player in bandits]))
            print("Guardians: ")
            print(", ".join([", ".join(player["guardians"])
                  for player in bandits]))
            print("Total players: {}".format(len(bandits)))
            print("Total Experienced Players: {}".format(
                len(experienced_players[:3])))
            print("Total Inexperienced Players: {}".format(
                len(inexperienced_players[:3])))
            print("Average Height: ")
            print(round(sum([player["height"]
                  for player in bandits]) / len(bandits), 2))
            # create an option to return to menu
            print("Press ENTER to return to menu")
            if input() == "":
                game_menu()
        else:
            print("Invalid option. Please try again.")
            game_menu()
    elif menu_choice == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid option. Please try again.")
        game_menu()


if __name__ == "__main__":
    new_players = copy.deepcopy(PLAYERS)
    cleaned_data(new_players)
    sort_experience(new_players)
    balance_teams()
    game_menu()
