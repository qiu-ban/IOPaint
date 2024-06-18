import json

config_map = {}
with open('./conf.json', 'r') as f:
    config_map = json.load(f)