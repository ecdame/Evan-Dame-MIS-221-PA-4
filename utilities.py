class Player:

    def __init__(self, name, position, team, games, ppg, rebounds, assists):
        self.name = name
        self.position = position
        self.team = team
        self.games = games
        self.ppg = ppg
        self.rebounds = rebounds
        self.assists = assists

        #Calculated fields
        self.pra = self.ppg + self.rebounds + self.assists
        self.total_points = self.ppg * self.games


def menu(player_list):
    
    while True:

        print("\nOptions: " \
        "\nTP: Displays players ranked by total points" \
        "\nPRA: Displays Players Ranked by points per game, assists, and rebound Average" \
        "\nPPG Combos: Displays combinations of 2 players on the same team with 50+ points per game combined" \
        "\nQuit: Exits the program")

        selection = input("Please enter selection: ")
        selection = sel_check(selection)

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
            case "quit":
                print("Have a nice day!")
                break

def sel_check(sel):

    while True:
        sel = sel.strip().lower()

        if sel in ["tp", "pra", "ppg combos", "quit"]:
            return sel

        sel = input("Please make a valid selection: ")

def quant_check(quant, player_list):

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
    player_list.sort(key=lambda Player: Player.pra, reverse=True)

    print(f"\nTop {x} Players by PRA Average:\n")
    for i in range(x):
        p = player_list[i]
        print(f"#{i+1}: {p.name}---{p.pra} pra average")

def top_x_total_points(player_list, x):
    player_list.sort(key=lambda Player: Player.total_points, reverse=True)
    
    print(f"\nTop {x} Players by Total Points Scored:\n")
    for i in range(x):
        p = player_list[i]
        print(f"#{i+1}: {p.name}---{p.total_points} total points")

def combined_ppg(player_list):

    player_list.sort(key=lambda Player: Player.team)

    print("\nPlayer Duos with Combined PPG >= 50:\n")
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

