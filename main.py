#Seth Fleshman
#This program analyzes a video game database, updates a record of the user's gaming history, and makes a recommendation
import pandas as pd

#Creates a panda dataframe based on the video games csv
video_games = pd.read_csv("video_games_raw.csv")

#Creates a list of statuses to use later for input validation
statuses = ["backlog", "playing", "completed", "dropped"]

print("VIDEO GAME CATALOG MANAGER")

# Obtain user input for which row to manage
while True:
    try:
        current_row = int(input("What row would you like to analyze?: "))

    except ValueError:
        print(f"Please enter a valid row between 1 and {len(video_games)}")

    else:
        if current_row < 1 or current_row > len(video_games):
            print(f"Please enter a valid row between 1 and {len(video_games)}")
        else:
            break

#Display info on the current row
print(f"\n{video_games.iloc[current_row - 1].to_string()}")

# Ask the user what their new completion status is
while True:
    completion = input("\nEnter a new status (IE \"backlog\", \"playing\", \"completed\", or \"dropped\"): ")
    
    if completion.lower() in statuses:
        break
    else:
        print("Please enter a valid status.")

# Change the value of statuse in the current row to the user's input
video_games.at[current_row - 1, "Status"] = completion.capitalize()

# Create a new column called recommended and set it to no for each row
video_games["Recommended"] = "No"

# Change to Yes when the rating is at least 8 and the price is at least 40
video_games.loc[
    (video_games["Rating"] >= 8) & (video_games["Price"] <= 40),
    "Recommended"
] = "Yes"

# Display only recommended games
print("\nRecommended Games:")
print(
    video_games.query('Recommended == "Yes"')[
        ["Title", "Platform", "Price", "Rating"]
    ].to_string()
)

video_games.to_csv("video_games_cleaned.csv", index=False)

# Print the concluding statements
print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv")
print()
