import os
import json
import csv

abs_path = os.path.dirname(__file__)

data = {}
data['members'] = []
data['books'] = []
data['loanItems'] = []

with open(abs_path + '/data/books.json') as f:
    data['books'] = json.load(f) 

with open(abs_path + '/data/members.csv') as f:
    data['members'] = csv.reader(f)

with open(abs_path + '/data/loanItems.json') as f:
    data['loanItems'] = json.load(f)
