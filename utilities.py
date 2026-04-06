import math

# Represents one NBA player and the stats this program needs.
class Player:

    def __init__(self, name, position, team, games, ppg, rebounds, assists):
        # Store the raw values loaded from the CSV file.
        self.name = name
        self.position = position
        self.team = team
        self.games = games
        self.ppg = ppg
        self.rebounds = rebounds
        self.assists = assists

        # Build extra values once so the program can reuse them later.
        self.pra = self.ppg + self.rebounds + self.assists
        self.total_points = math.floor(self.ppg * self.games)


def menu(player_list):
    # Keep showing the menu until the user chooses to quit.
    while True:

        print("\nMain Menu")
        print("\nOptions: " \
        "\nTP: Displays players ranked by total points" \
        "\nPRA: Displays Players Ranked by points per game, assists, and rebound Average" \
        "\nPPG Combos: Displays combinations of 2 players on the same team with 50+ points per game combined" \
        "\nPlayer Search: Displays data for a specified player"
        "\nTeam Search: Displays data for players on a specified team"
        "\nQuit: Exits the program")

        selection = input("\nPlease enter selection: ")
        # Clean and validate the user's menu choice before using it.
        selection = sel_check(selection)

        # Run the matching feature based on the user's selection.
        match selection:
            case "tp":
                num_players = input("Please enter the number of players you want to display: ")
                num_players = quant_check(num_players, player_list)

                top_x_total_points(player_list, num_players)
            case "pra":
                num_players = input("Please enter the number of players you want to display: ")
                num_players = quant_check(num_players, player_list)

                top_x_pra_avg(player_list, num_players)
            case "ppg combos":
                combined_ppg(player_list)
            case "player search":
                name = input("Please input the name of the player: ")
                player_search(player_list, name)
            case "team search":
                team = input("Please enter the three-letter abbreviation of the team you want to search: ")
                team_search(player_list, team)
            case "quit":
                print("\nHave a nice day!")
                break

def sel_check(sel):
    # Repeatedly prompt until the user enters one of the allowed commands.
    while True:
        sel = sel.strip().lower()

        if sel in ["tp", "pra", "ppg combos", "player search", "team search", "quit"]:
            return sel

        sel = input("Please make a valid selection: ")

def quant_check(quant, player_list):
    # Make sure the requested number of players is an integer within range.
    while True:
        try: 
            quant = int(quant)

        except ValueError:
            quant = input("Please enter a valid number of players: ")
            continue

        if quant > 0 and quant <= len(player_list):
            return quant
        else: quant = input("Please enter a valid number of players: ")

def top_x_pra_avg(player_list, x):
    # Sort players from highest PRA to lowest before printing the top results.
    player_list.sort(key=lambda Player: Player.pra, reverse=True)

    print(f"\nTop {x} Players by PRA Average:\n")
    for i in range(x):
        p = player_list[i]
        print(f"#{i+1}: {p.name}---{p.pra} pra average")

def top_x_total_points(player_list, x):
    # Sort players by total points scored, highest first.
    player_list.sort(key=lambda Player: Player.total_points, reverse=True)
    
    print(f"\nTop {x} Players by Total Points Scored:\n")
    for i in range(x):
        p = player_list[i]
        print(f"#{i+1}: {p.name}---{p.total_points} total points")

def combined_ppg(player_list):
    # Group same-team players together so it is easier to compare teammates.
    player_list.sort(key=lambda Player: Player.team)

    print("\nPlayer Duos with Combined PPG >= 50:\n")
    # Check every unique pair of players and print duos from the same team
    # whose combined points per game meet the requirement.
    for i in range (len(player_list)):
        for j in range(i+1, len(player_list)):

            p1 = player_list[i]
            p2 = player_list[j]

            if p1.team == p2.team:
                total_ppg = p1.ppg + p2.ppg

                if total_ppg >= 50:
                    print(f"Team: {p1.team}  "
                          f"Players: {p1.name} and {p2.name}  "
                          f"Combined PPG: {total_ppg}")

def player_search(player_list, name):
    # Normalize the input so capitalization and extra spaces do not matter.
    name = name.lower().strip()
    
    # Look through the list until an exact player name match is found.
    for player in player_list:
        if name == player.name.lower().strip():
            print(f"\n{player.name} Data: ")
            print(f"Position: {player.position}")
            print(f"Team: {player.team}")
            print(f"Games Played: {player.games}")
            print(f"Total Points: {player.total_points}")
            print(f"Points Per Game: {player.ppg}")
            print(f"Rebounds Per Game: {player.rebounds}")
            print(f"Assists Per Game: {player.assists}")
            print(f"PRA Average: {player.pra}")

            return
    # If no match is found, ask again and repeat the search.
    print(f"\nNo player named {name} was found.")
    name = input("Please enter a valid player name: ")
    player_search(player_list, name)
            
def team_search(player_list, team):
    # Track whether at least one player on the requested team is found.
    team_found = False
    team = team.lower().strip()

    print(f"\n{team.upper().strip()} Players: ")
    # Print every player whose team abbreviation matches the search.
    for player in player_list:
        if team == player.team.lower().strip():

            team_found = True
            print(f"\n{player.name}: ")
            print(f"Position: {player.position}")
            print(f"Games Played: {player.games}")
            print(f"Total Points: {player.total_points}")
            print(f"Points Per Game: {player.ppg}")
            print(f"Rebounds Per Game: {player.rebounds}")
            print(f"Assists Per Game: {player.assists}")
            print(f"PRA Average: {player.pra}")

    # If no team was found, prompt again and rerun the search.
    if team_found == False:
        print(f"\nNo team matching {team.upper().strip()} was found!")
        team = input("Please enter a valid team abbreviation: ")
        team_search(player_list, team)
