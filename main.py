from utilities import Player
import utilities

# CSV file that stores the NBA stats used by this program.
filepath = r"nba_data_2.csv"


# Load the CSV data and turn each row into a Player object.
with open(filepath, "r", encoding="utf-8-sig") as f:

    # Skip the header row so only player data is processed.
    f.readline()

    # This list will hold every Player created from the file.
    player_list = []

    # Read the remaining file one line at a time.
    for line in f:

        # Break the row into individual columns.
        stats = line.split(",")

        # Convert any numeric-looking values to floats and leave text fields alone.
        for i in range(len(stats)):
            try:
                stats[i] = float(stats[i])
            except ValueError:
                continue
        
        # Create a Player using the columns this assignment cares about,
        # then save that player in the main list.
        player = Player(stats[0], stats[1], stats[3], stats[4], stats[28], stats[22], stats[23])
        player_list.append(player)

print("Welcome to the NBA stat tracker program!\n" \
"This program allows you to query a database of NBA players, and find several relevant statistics for them.\n" \
"To execute a command, please type the name of the command when prompted in the main menu, and follow all instructions.")
# Start the menu-driven part of the program once all data is loaded.
utilities.menu(player_list)



