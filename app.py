from constants import *

panthers = []
warriors = []
bandits = []
experienced_players = []
inexperienced_players = []

# @PARAMS: PLAYERS


def cleaned_data(new_data):
    # Height
    for data in new_data:
        new_height = data['height'].split()
        if new_height and new_height[0].isnumeric():
            data['height'] = int(new_height[0])
            print(data['height'])
    # Experience
        if data["experience"] == "YES":
            data["experience"] = True
        else:
            data["experience"] = False
        print(data["experience"])
    # Guardians
        data["guardians"] = data["guardians"].split(" and ")
        print(data["guardians"])


def sort_experience(data):
    pass


cleaned_data(PLAYERS)
# def game_menu():
#     pass


# if __name__ == "__main__":
#     game_menu()
