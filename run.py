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


# Function to retrieve the headers and data from the google sheet
def get_headers_and_data(sheet):
    all_data = sheet.get_all_values()
    headers = all_data[0]
    data = all_data[1:]
    return headers, data


def display_table_dynamic_width(headers, data):
    total_header_length = sum(len(header) for header in headers)
    num_columns = len(headers)
    max_width = 80

    if total_header_length >= max_width:
        column_widths = [max(1, max_width // num_columns)] * num_columns
    else:
        column_widths = [(max_width - total_header_length) // num_columns + 1 for _ in range(num_columns)]

    truncated_headers = [header[:width] + '...' if len(header) > width else header for header, width in zip(headers, column_widths)]

    truncated_data = []
    for row in data:
        truncated_row = [cell[:width] + '...' if len(cell) > width else cell for cell, width in zip(row, column_widths)]
        truncated_data.append(truncated_row)

    print(tabulate(truncated_data, truncated_headers, tablefmt="simple"))


# Function to list all characters from the 'Characters' worksheet.
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
        print(f"Error retrieving skills: {e}")


# Function to add new characters to the 'Characters' worksheet.
def add_new_character():
    try:
        name = input("Enter Character name:\n").strip()

        races = ["Saiyan", "Alien", "Human", "Android"]
        print("Choose a race:")
        for i, race in enumerate(races, 1):
            print(f"{i}. {race}")
        race_choice = input("Enter the number corresponding to the race:\n").strip()
        race = races[int(race_choice) - 1] if race_choice.isdigit() and 1 <= int(race_choice) <= len(races) else None

        if not race:
            print("Invalid race choice.")
            return

        while True:
            power_level = input("Enter character power level (1-15000):\n").strip()
            if power_level.isdigit() and 1 <= int(power_level) <= 15000:
                break
            else:
                print("Invalid power level. Please enter a number between 1 and 15000.")

        abilities = input("Enter character's abilities (comma-separated if multiple):\n").strip()

        while True:
            health = input("Enter character health (0-100):\n").strip()
            if health.isdigit() and 0 <= int(health) <= 100:
                break
            else:
                print("Invalid health value. Please enter a number between 0 and 100.")

        while True:
            energy = input("Enter character energy (0-150):\n").strip()
            if energy.isdigit() and 0 <= int(energy) <= 150:
                break
            else:
                print("Invalid energy value. Please enter a number between 0 and 150.")

        affiliations = ["Z Fighter", "Villain"]
        print("Choose an affiliation:")
        for i, affiliation in enumerate(affiliations, 1):
            print(f"{i}. {affiliation}")
        affiliation_choice = input("Enter the number corresponding to the affiliation:\n").strip()
        affiliation = affiliations[int(affiliation_choice) - 1] if affiliation_choice.isdigit() and 1 <= int(affiliation_choice) <= len(affiliations) else None

        if not affiliation:
            print("Invalid affiliation choice.")
            return

        characters_sheet.append_row([name, power_level, race, abilities, health, energy, affiliation])
        print("New character added successfully!")
    except Exception as e:
        print(f"Error adding new character: {e}")


# Function to add new battles to the 'Battles' worksheet.
def add_new_battle():
    try:
        characters_data = characters_sheet.get_all_values()
        character_names = [row[0] for row in characters_data[1:]]

        if len(character_names) < 2:
            print("Not enough characters available to record a battle.")
            return

        char1 = None
        while not char1:
            print("Choose Character 1:")
            for i, name in enumerate(character_names, 1):
                print(f"{i}. {name}")
            char1_choice = input("Enter the number corresponding to Character 1:\n").strip()
            char1 = character_names[int(char1_choice) - 1] if char1_choice.isdigit() and 1 <= int(char1_choice) <= len(character_names) else None
            if not char1:
                print("Invalid choice for Character 1. Please try again.")

        char2 = None
        while not char2:
            print("Choose Character 2:")
            for i, name in enumerate(character_names, 1):
                print(f"{i}. {name}")
            char2_choice = input("Enter the number corresponding to Character 2:\n").strip()
            char2 = character_names[int(char2_choice) - 1] if char2_choice.isdigit() and 1 <= int(char2_choice) <= len(character_names) and character_names[int(char2_choice) - 1] != char1 else None
            if not char2:
                print("Invalid choice for Character 2 or same character chosen. Please try again.")

        outcome_choice = None
        while outcome_choice not in ["1", "2"]:
            print(f"Choose the outcome of the battle between {char1} and {char2}:")
            print(f"1. {char1} wins")
            print(f"2. {char2} wins")
            outcome_choice = input("Enter the number corresponding to the winner:\n").strip()
            outcome = f"{char1} wins" if outcome_choice == "1" else f"{char2} wins" if outcome_choice == "2" else None

        while True:
            damage_dealt = input("Enter damage dealt (0-100):\n").strip()
            if damage_dealt.isdigit() and 0 <= int(damage_dealt) <= 100:
                break
            else:
                print("Invalid damage value. Please enter a number between 0 and 100.")

        while True:
            duration = input("Enter battle duration (0-10):\n").strip()
            if duration.isdigit() and 0 <= int(duration) <= 10:
                break
            else:
                print("Invalid duration value. Please enter a number between 0 and 10.")

        locations = ['Planet Namek', 'Tournament Arena', 'Hyperbolic Time Chamber', 'Earth']
        print("Choose battle location:")
        for i, location in enumerate(locations, 1):
            print(f"{i}. {location}")
        print(f"{len(locations) + 1}. Add a new location")
        location_choice = input(f"Enter the number corresponding to the location or choose {len(locations) + 1} to add a new one: \n").strip()

        if location_choice == str(len(locations) + 1):
            new_location = input("Enter the name of the new location:\n").strip()
            location = new_location if new_location else None
            if location:
                locations.append(location)
                print(f"New location '{new_location}' added successfully.")
            else:
                print("Invalid location name. Location not added.")
                return
        else:
            location = locations[int(location_choice) - 1] if location_choice.isdigit() and 1 <= int(location_choice) <= len(locations) else None

        if not location:
            print("Invalid location choice.")
            return

        battles_sheet.append_row([char1, char2, outcome, damage_dealt, duration, location])
        print("New battle added successfully!")
    except Exception as e:
        print(f"Error adding new battle: {e}")


# Function to add new skills to the 'Skills' worksheet.
def add_new_skill():
    try:
        skill_name = input("Enter skill name:\n").strip()

        while True:
            power_rating = input("Enter power rating (0-1000):\n").strip()
            if power_rating.isdigit() and 0 <= int(power_rating) <= 1000:
                break
            else:
                print("Invalid power rating. Please enter a number between 0 and 1000.")

        while True:
            energy_cost = input("Enter energy cost (0-150):\n").strip()
            if energy_cost.isdigit() and 0 <= int(energy_cost) <= 150:
                break
            else:
                print("Invalid energy cost. Please enter a number between 0 and 150.")

        skills_sheet.append_row([skill_name, power_rating, energy_cost])
        print("New skill added successfully!")
    except Exception as e:
        print(f"Error adding new skill: {e}")


# Main menu for the app
def main_menu():
    while True:
        print("\n--- Z Tournament Battle Tracker ---")
        print("1. List all characters")
        print("2. List all battles")
        print("3. List all skills")
        print("4. Add a new character")
        print("5. Add a new battle")
        print("6. Add a new skill")
        print("7. Exit")

        choice = input("Enter the number of your choice:\n").strip()

        if choice == "1":
            get_all_characters()
        elif choice == "2":
            get_all_battles()
        elif choice == "3":
            get_all_skills()
        elif choice == "4":
            add_new_character()
        elif choice == "5":
            add_new_battle()
        elif choice == "6":
            add_new_skill()
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main_menu()
