from constants import *


def clean_data(new_data):
    cleaned_data = []
    for player in new_data:
        int_height = player['height'].split()
        print(int_height)


clean_data()
# def game_menu():
#     pass


# if __name__ == "__main__":
#     game_menu()
