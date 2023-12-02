def parse_games(file_name):
    games = {}
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():
                game_title, game_info = line.split(':', 1)
                game_data = [dict(map(lambda x: (x.split()[1], int(x.split()[0])), part.split(','))) 
                             for part in game_info.strip().split(';')]
                games[game_title.strip()] = game_data
    return games

def sum_valid_ids(games, red_max, green_max, blue_max):
    return sum(int(game.split(' ')[1]) for game, parts in games.items()
               if all(part.get('red', 0) <= red_max and 
                      part.get('green', 0) <= green_max and 
                      part.get('blue', 0) <= blue_max for part in parts))

def sum_power_sets(games):
    return sum(max(part.get('red', 0) for part in parts) * 
               max(part.get('green', 0) for part in parts) * 
               max(part.get('blue', 0) for part in parts) for game, parts in games.items())

games_dict = parse_games('cube-conundrum.txt')

valid_ids_sum = sum_valid_ids(games_dict, 12, 13, 14)
power_sets_sum = sum_power_sets(games_dict)

print("Sum of valid game IDs:", valid_ids_sum)
print("Total sum of the power of sets:", power_sets_sum)
