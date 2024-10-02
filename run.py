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

def add_characters(name, power_level, race, abilities, health, energy, affiliation);
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
            energy = input("enter affiliation:")
            add_character(name, power_level, race, abilities, health, energy, affiliation)