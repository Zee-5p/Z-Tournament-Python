import gspread
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Z Tournament Database')

characters = SHEET.worksheet('Characters')
battles = SHEET.worksheet('Battles')
skills = SHEET.worksheet('Skills')

def list_characters():
    data = characters.get_all_values()
    print(data)

def add_characters(name, power_level, race, abilities, health, energy, affiliation):
    characters.append_row([name, power_level, race, abilities, health, energy, affiliation])
    
def list_battles():
    data = battles.get_all_records()
    print(data)

def add_battle(char1, char2, outcome, damage_dealt, duration, location):
    battles.appennd_row([char1, char2, outcome, damage_dealt, duration, location])

def list_skills():
    data = skills.get_all_records()
    print(data)

def add_skill(move_name, power_rating, energy_cost, move_type, description):
    skills.append_row([move_name, power_rating, energy_cost, move_type, description])

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