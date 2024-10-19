import pandas as pd
player_runs = {}

for i in range(5):
    player = input(f"Enter the name of player {i+1}: ")
    runs = int(input(f"Enter the runs scored by {player}: "))
    player_runs[player] = runs

print(player_runs)

player_runs_series = pd.Series(player_runs)

print(player_runs_series)
