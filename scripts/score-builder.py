#!/usr/bin/env python

import itertools
import json
import csv

player_ids = [1, 2, 3, 4, 5, 6, 7]
metrics_json_file_path = "../datasource/metrics.json"
games_file_path = "../datasource/games.csv"


# if game is 1,2,3,4 then 1,2 has beaten 3, 4
def __count_n_update_won_lost(game, metrics):
    metrics["{0}_{1}".format(game[0], "won")] += 1
    metrics["{0}_{1}".format(game[1], "won")] += 1
    metrics["{0}_{1}".format(game[2], "lost")] += 1
    metrics["{0}_{1}".format(game[3], "lost")] += 1


# so, 1,2 is same as 2,1 in a game
def __count_n_update_won_lost_with_partners(game, metrics):
    key_won = "{0}_{1}_{2}".format(game[0], game[1], "won")
    if key_won in metrics:
        metrics[key_won] += 1
    else:
        key_won_rev = "{0}_{1}_{2}".format(game[1], game[0], "won")
        if key_won_rev in metrics:
            metrics[key_won_rev] += 1
    key_lost = "{0}_{1}_{2}".format(game[2], game[3], "lost")
    if key_lost in metrics:
        metrics[key_lost] += 1
    else:
        key_lost_rev = "{0}_{1}_{2}".format(game[3], game[2], "lost")
        if key_lost_rev in metrics:
            metrics[key_lost_rev] += 1


def __calculate_rank_n_update(metrics):
    players_rank = {}
    for player_id in player_ids:
        players_rank[player_id] = metrics["{0}_{1}".format(player_id, "won")] - metrics[
            "{0}_{1}".format(player_id, "lost")]
    player_ids_sorted = sorted(players_rank, key=players_rank.get, reverse=True)
    for rank, player_id in enumerate(player_ids_sorted):
        metrics["{0}_{1}".format(player_id, "rank")] = rank + 1


def __main():
    with open(metrics_json_file_path, 'r') as metrics_template:
        metrics = json.load(metrics_template)
    with open(games_file_path, 'rb') as games_data:
        games = csv.reader(games_data, delimiter=',')
        for game in games:
            __count_n_update_won_lost(game, metrics)
            __count_n_update_won_lost_with_partners(game, metrics)
    __calculate_rank_n_update(metrics)
    with open(metrics_json_file_path, 'w') as fp:
        json.dump(metrics, fp, sort_keys=True, indent=4, separators=(',', ': '))


__main()
