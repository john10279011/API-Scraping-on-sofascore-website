import json
import pandas as pd
import requests

data = []

url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2022-03-31"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\^"
}

response = requests.request("GET", url, data=payload, headers=headers)

jsondata = json.loads(response.text)
    
for score in jsondata['events']:    
    legue = score['tournament']['name']
    categorys = score['tournament']['category']['name']
    hometeam = score['homeTeam']['name']
    try:
        homescore =score['homeScore']['current']
    except:
        homescore=''
    
    awayteam = score['awayTeam']['name']
    try:
        awayscore = score['awayScore']['current']
    except:
        awayscore = ''
    if homescore and awayscore is not None:
        played = 'played'
    else:
        played = 'not played'
    details = {
        'hometeam':hometeam,
        'homescore':homescore,
        'awayscore':awayscore,
        'awayteam':awayteam,
        'legue':legue,
        'category':categorys,
        'game status':played,
    }
    data.append(details)
        
df = pd.DataFrame(data)
#df.to_csv('example.csv',index = False)
print(df)