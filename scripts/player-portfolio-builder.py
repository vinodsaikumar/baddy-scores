#!/usr/bin/env python

from bs4 import BeautifulSoup
import json
import copy

player_ids = [1, 2, 3, 4, 5, 6]
metrics_json_file_path = "../datasource/metrics.json"
players_generic_file = "../docs/generic.html"
players_rank_file = "../docs/rank.html"
players_file_path = "../docs"


def __create_leader_board(metrics, rank_soup):
    leader_board = {}
    for player_id in player_ids:
        leader_board[player_id] = metrics["{0}_{1}".format(player_id, "rank")]
    player_ids_sorted = sorted(leader_board, key=leader_board.get)
    table_body = rank_soup.new_tag("tbody", id="players_rank")
    for player_id in player_ids_sorted:
        player_name = metrics["{0}_{1}".format(player_id, "name")]
        player_rank = metrics["{0}_{1}".format(player_id, "rank")]
        row_tag = "<tr><td>{0}</td><td>{1}</td></tr>".format(player_name, player_rank)
        row_soup = BeautifulSoup(row_tag, "html.parser")
        table_body.append(row_soup)
    original_table_body = rank_soup.find(id="players_rank")
    original_table_body.replace_with(table_body)
    with open(players_rank_file, "w") as rank_file:
        rank_file.write(str(rank_soup.prettify()))


def __create_portfolio(metrics, player_id, soup):
    player_rank = metrics["{0}_{1}".format(player_id, "rank")]
    player_won = metrics["{0}_{1}".format(player_id, "won")]
    player_lost = metrics["{0}_{1}".format(player_id, "lost")]
    player_name = metrics["{0}_{1}".format(player_id, "name")]
    soup.find(id="player_rank").insert(1, "{0}".format(player_rank))
    soup.find(id="player_won").insert(1, "{0}".format(player_won))
    soup.find(id="player_lost").insert(1, "{0}".format(player_lost))
    soup.find(id="player_name").insert(1, "{0}".format(player_name))
    for partner_id in player_ids:
        partner_name = metrics["{0}_{1}".format(partner_id, "name")]
        key_partner_won = "{0}_{1}_{2}".format(player_id, partner_id, "won")
        key_partner_lost = "{0}_{1}_{2}".format(player_id, partner_id, "lost")
        key_partner_won_rev = "{0}_{1}_{2}".format(partner_id, player_id, "won")
        key_partner_lost_rev = "{0}_{1}_{2}".format(partner_id, player_id, "lost")
        if key_partner_won in metrics and key_partner_lost in metrics:
            partner_won = metrics[key_partner_won]
            partner_lost = metrics[key_partner_lost]
            row_tag = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(partner_name, partner_won, partner_lost)
            row_soup = BeautifulSoup(row_tag, "html.parser")
            soup.find(id="player_partner_metrics").insert(1, row_soup)
        if key_partner_won_rev in metrics and key_partner_lost_rev in metrics:
            partner_won = metrics[key_partner_won_rev]
            partner_lost = metrics[key_partner_lost_rev]
            row_tag = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(partner_name, partner_won, partner_lost)
            row_soup = BeautifulSoup(row_tag, "html.parser")
            soup.find(id="player_partner_metrics").insert(1, row_soup)
    with open("{0}/{1}.html".format(players_file_path, player_id), "w") as player_html_file:
        player_html_file.write(str(soup.prettify()))


def __main():
    with open(metrics_json_file_path, 'r') as metrics_template:
        metrics = json.load(metrics_template)
    with open(players_generic_file, 'r') as portfolio_template:
        soup = BeautifulSoup(portfolio_template, 'html.parser')
    for player_id in player_ids:
        soup_copy = copy.copy(soup)
        __create_portfolio(metrics, player_id, soup_copy)
    with open(players_rank_file, 'r') as rank_file:
        rank_soup = BeautifulSoup(rank_file, 'html.parser')
    __create_leader_board(metrics, rank_soup)


__main()
