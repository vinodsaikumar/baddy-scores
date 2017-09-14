#!/usr/bin/env python

import itertools
import json

player_ids = [1, 2, 3, 4, 5, 6, 7]
player_names = {
    "1_name": "Basavaraj",
    "2_name": "Deepthi",
    "3_name": "Goutham",
    "4_name": "Sharan",
    "5_name": "Vinayak",
    "6_name": "Vinod",
    "7_name": "Paneendra"
}
player_metrics = ["name", "won", "lost", "rank"]
player_with_partner_metrics = ["won", "lost"]

metrics_json_file_path = "../datasource/metrics.json"


def __create_metrics_template():
    keys = []
    for player_id in player_ids:
        for p_metric in player_metrics:
            keys.append("{0}_{1}".format(player_id, p_metric))
    for comb in itertools.combinations(player_ids, 2):
        for partner_metric in player_with_partner_metrics:
            keys.append("{0}_{1}_{2}".format(comb[0], comb[1], partner_metric))
    metrics = dict((el, 0) for el in keys)
    metrics.update(player_names)
    with open(metrics_json_file_path, 'w') as fp:
        json.dump(metrics, fp, sort_keys=True, indent=4, separators=(',', ': '))


__create_metrics_template()
