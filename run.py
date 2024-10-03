import gspread
from google.oauth2.service_account import Credentials 
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Z Tournament Database')

characters_sheet = SHEET.worksheet('Characters')
battles_sheet = SHEET.worksheet('Battles')
skills_sheet = SHEET.worksheet('Skills')



def get_headers_and_data(sheet):

    all_data = sheet.get_all_values()
    headers = all_data[0]
    data = all_data[1:]
    return headers, data

def display_table(headers, data):

    print(tabulate(data, headers, tablefmt="grid"))

# Function to list all characters from the 'Charcaters' worksheet.
def get_all_characters():

    try:
        headers, data = get_headers_and_data(characters_sheet)
        if not data:
            print("No characters found.")
        else:
            display_table(headers, data)
    except Exception as e:
        print(f"Error retrieving characters: {e}")


# Function to list all battles from the 'Battles' worksheet.
def get_all_battles():
   
    try:
        headers, data = get_headers_and_data(battles_sheet)
        if not data:
            print("No battles found.")
        else:
            display_table(headers, data)
    except Exception as e:
        print(f"Error retrieving battles: {e}")

def get_all_skills():
    try:
        headers, data = get_headers_and_data(skills_sheet)
        if not data:
            print("No skills found.")
        else:
            display_table(headers, data)
    except Exception as e:
        print(f"Error retrieveing skills: {e}")




def main():
    while True:
        print("\nChoose an option:")
        print("1. List Characters")
        print("2. Add Characters")
        print("3. List Battles")
        print("4. Add Battles Record")
        print("5. List Skills")
        print("6. Add Skill")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            list_characters()
        elif choice == '2':
            name = input("Enter character name:")
            power_level = input("Enter power level:")
            race = input("Enter race:")
            abilities = input("Enter abilities (comma seperated):")
            health = input("Enter health:")
            energy = input("Enter energy:")
            affiliation = input("Enter Affiliation:")
            add_characters(name, power_level, race, abilities, health, energy, affiliation)
        elif choice == '3':
            char1 = input("Enter first character:")
            char2 = input("Enter second character:")
            outcome = input("Enter outcome:")
            damage_dealt = input("Enter damage dealt:")
            duration = input("enter battle duration (minutes):")
            location = input("Enter battle location:")
            add_battle(char1, char2, outcome, damage_dealt, duration, location)
        elif choice == '5':
            list_skills()
        elif choice == '6':
            move_name = input("Enter skill name:")
            power_rating = input("Enter power rating:")
            energy_cost = input("Enter enegry cost:")
            move_type = input("Enter skill type:")
            description = input("Enter description:")
            add_skill(move_name, power_rating, energy_cost, move_type, description)
        elif choice == '0':
            print("Exiting ...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()