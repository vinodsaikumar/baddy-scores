#!/usr/bin/env python

import itertools
import json

player_ids=[1,2,3,4]
player_metrics={"won","lost","rank"}
player_with_partner_metrics={"won","lost"}

metrics_json_file_path="../datasource/metrics.json"

def __create_metrics_template():
    keys=[]
    for id in player_ids:
        for p_metric in player_metrics:
            keys.append("{0}_{1}".format(id,p_metric))
    for comb in itertools.combinations(player_ids, 2):
        for partner_metric in player_with_partner_metrics:
            keys.append("{0}_{1}_{2}".format(comb[0],comb[1],partner_metric))
    metrics = dict((el,0) for el in keys)
    with open(metrics_json_file_path, 'w') as fp:
        json.dump(metrics, fp)

__create_metrics_template()
