# Z Tournament Battle Tracker

**Z Tournament Battle Tracker** is a Python based application designed for **Dragon Ball Z** fans to track battles, characters, and skills as they watch the series. As a big DBZ fan I wanted to incorporate my love for the show with my project. The purpose of this tool was to make the process of watching the show more interactive. This allows users to feel more involved, and once they get to the end, have a comprehensive database on their new favourite show, giving them something to remember it by even after its done. The application is integrated with Google Sheets, ensuring that the data is easily stored and updated.

## Purpose

The **Z Tournament Battle Tracker** aims to provide **Dragon Ball Z** fans with a fun and engaging way to track the show's battles and characters as they appear in the series.
 Allowing users to:
- Monitor the progression of characters (e.g., power level, health, and affiliation).
- Track iconic battles by logging the characters, outcomes, damage dealt, and locations.
- store and view skills and techniques used by the characters, including power ratings and energy costs.
This project is designed to enhance the viewing experience of this great show, giving fans a new way to get involved.

## Features

### Current Features

1. **Character Management**:
   - List all characters that are stored in the tracker with attributes such as power level, race, health, energy, and affiliation.
   - Add new characters as they are introduced in the series, with real-time updates to a Google Sheets database.

2. **Battle Tracking**:
   - List previously logged battles with information like the winner, damage dealt, battle duration, and location.
   - Add new battles, logging details of the fighters involved and the outcome.

3. **Skill Management**:
   - View skills logged in the tracker, including details such as power rating and energy cost.
   - Add new skills as characters develop new abilities in the series and new characters skills are revealed.

### Future Enhancements

1. **Battle Analytics**:
   - Generate statistics like win rates, damage averages, and comparisons of fighters over time.
   
2. **Search Functionality**:
   - Implement a search feature for users to find battles, characters, and skills quickly.

3. **Battle Outcome Predictions**:
   - Integrate a prediction model to analyse potential outcomes of battles based on character stats.

## Data Model

The application's data model is structured in three Google Sheets for efficient storage and retrieval of characters, battles, and skills:

1. **Characters Sheet**:
   - **Power Level**: (1-15,000) A character’s power level throughout the series.
   - **Race**: (Saiyan, Alien, Human, Android).
   - **Health**: (0-100) Indicates a character’s health.
   - **Energy**: (0-150) Measures energy available for powerful attacks.
   - **Affiliation**: Identifies whether a character is a **Z Fighter** or a **Villain**.

2. **Battles Sheet**:
   - **Character1** and **Character2**: Participants from the characters sheet.
   - **Outcome**: 'C1 wins' or 'C2 wins', depending on the winner.
   - **Damage Dealt**: (0-100) Tracks the level of damage in a battle.
   - **Duration**: (0-10) Represents the time span of the battle.
   - **Location**: (Planet Namek, Tournament Arena, Hyperbolic Time Chamber, Earth, etc.).

3. **Skills Sheet**:
   - **Skill Name**: The name of the ability (e.g., Kamehameha).
   - **Power Rating**: (0-1000) Indicates the strength of the technique.
   - **Energy Cost**: (0-150) Represents the energy required to perform the skill.

## Deployment steps

1. **Clone the Repository**: Use the template given by Code institute to create a repository 

2. **Set Up Google Sheets API**: Create a Google Cloud project and enable the Google Sheets API and download the API credentials and store them as `creds.json` in the project directory.

3. **Deploy the project on a cloud platform**: Create an account with Heroku and link my GitHub repository adding the necessary buildpacks (Python, NodeJS)

4. **Deploy the project using Heroku**: This is done by clicking deploying once everything is set up

## Testing

**Solved Bugs**:
1.	When I first wrote my code, I forgot to add any validators or parameters for the text entry, therefore incorrect entry would not result in any response from the system. When this was picked up changes were made so that only relevant information could be entered and if it wasn’t relevant the user would be alerted. 

2.	Syntax errors meant that certain functions and inputs were not being called these were picked up during testing and corrected.

3.	In my first iteration I did not make the functions atomic, this was picked up and corrected.

**Remaining Bugs**:
•	During my testing phase I was running my project through the terminal and the visibility was clear, when setting it up in Heroku I noticed that the text on the tales was squished and visibility was poor, I was unable to make the necessary changes in time. 

**Validator Testing**:
I used PEP8 to test my code and didn’t find any issues other than lines of code exceeding the limit. 
