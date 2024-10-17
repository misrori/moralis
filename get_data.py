import os
from scrapethat import *
from datetime import datetime, timedelta

today = datetime.today()
today_date_file_name = f"data/life1_class_{today.strftime('%Y-%m-%d')}.csv"

# if data folder not exist create it
if not os.path.exists("data"):
    os.makedirs("data")
 from scrapethat import *
import requests
import json
import datetime
t = read_cloud('https://moralis.com/api/search/trendingTokens')
data = json.loads(t.text)

now = datetime.datetime.now()
day = now.strftime("%y_%m_%d")
hour = now.strftime("%H_%M")

# Create a dynamic filename
filename = f"data_{day}_{hour}.json"

# Save the list to a file
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)