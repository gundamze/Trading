
x = 1
"""_________________________________________________________
                           API
   _________________________________________________________
"""
import requests
url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp = requests.get(url)
resp
type(resp)

import json
data = json.loads(resp.text)

data[0]
type(data[0])
data[0].keys()

colname = data[0].keys()

from pandas import DataFrame
values = DataFrame(data[0], index = [0])

