from utilities import Player
import utilities

filepath = r"nba_data_2.csv"


#Loads all the information into an array of Player objects
with open(filepath, "r", encoding="utf-8-sig") as f:

    f.readline()

    player_list = []

    for line in f:
        stats = line.split(",")

        for i in range(len(stats)):
            try:
                stats[i] = float(stats[i])
            except ValueError:
                continue

        player = Player(stats[0], stats[1], stats[3], stats[4], stats[28], stats[22], stats[23])
        player_list.append(player)


utilities.menu(player_list)



