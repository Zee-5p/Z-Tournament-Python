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

# Function to list all skills from the 'Skills' worksheet.
def get_all_skills():
    try:
        headers, data = get_headers_and_data(skills_sheet)
        if not data:
            print("No skills found.")
        else:
            display_table(headers, data)
    except Exception as e:
        print(f"Error retrieveing skills: {e}")

def add_new_character():

    try:
        name =input("Enter Character name:").strip()

        races = ["Saiyan", "Alien", "Human", "Android"]
        print("Choose a race:")
        for i, race in enumerate(races, 1):
            print(f"{i}.{race}")
        race_choice = input("enter the number corresponding to the race:").strip()
        race = races[int(race_choice) - 1] if race_choice.isdigit() and 1 <= int(race_choice) <= len(races) else None

        if not race:
            print("Invalid race choice.")
            return
        
        while True:
            power_level = input("Enter character power level (1-15000): ").strip()
            if power_level.isdigit() and 1 <= int(power_level) <= 15000:
                break
            else:
                print("Invalid power level. Please enter a number between 1 and 15000.")

        while True:
            health = input("Enter character health (0-100): ").strip()
            if health.isdigit() and 0 <= int(health) <= 100:
                break
            else:
                print("Invalid health value. Please enter a number between 0 and 100.")

        while True:
            energy = input("Enter character energy (0-150): ").strip()
            if energy.isdigit() and 0 <= int(energy) <= 150:
                break
            else:
                print("Invalid energy value. Please enter a number between 0 and 150.")

        affiliations = ["Z Fighter", "Villain"]
        print("Choose an affiliation:")
        for i, affiliation in enumerate(affiliations, 1):
            print(f"{i}. {affiliation}")
        affiliation_choice = input("Enter the number corresponding to the affiliation: ").strip()
        affiliation = affiliations[int(affiliation_choice) - 1] if affiliation_choice.isdigit() and 1 <= int(affiliation_choice) <= len(affiliations) else None
             
        if not affiliation:
            print("Invalid affiliation choice.")
            return
        
        characters_sheet.append_row([name, race, power_level, health, nergy, affiliation])
        print("New character added successfully!")
    except Exception as e:
        print(f"Error adding new character: {e}")

def add_new_skills():

    try:
        skill_name = input("Enter skill name:").strip()

        while True:
            power_rating = input("Enter power rating (0-1000):").strip()
            if power_rating.isdigit() and 0 <= int(power_rating) <= 1000:
                break
            else:
                print("Invalid power rating. Please enter a number between 0 and 1000.")
        
        while True:
            energy_cost = input("Enter energy cost (0-150): ").strip()
            if energy_cost.isdigit() and 0 <= int(energy_cost) <= 150:
                break
            else:
                print("Invalid energy cost. Please enter a number between 0 and 150.")

        skills_sheet.append_row([skill_name, power_rating, energy_cost])
        print("New skill added successfully!")
    except Exception as e:
        print(f"Error adding new skill: {e}")



