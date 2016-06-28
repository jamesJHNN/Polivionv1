import json
import codecs
import time
from math import floor

def read_from_json_line(file_path):
    """ Read json line file """
    data = []
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(json.loads(line)))
    return data

if active:
        data=read_from_json_line('C:/Users/BPR/Desktop/project-james-master/polivion.json')
        a=[int(s) for d in data for s in d['text'].split() if s.isdigit()]
