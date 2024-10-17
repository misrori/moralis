from scrapethat import *
import requests
import json
import datetime
import os

# if data folder not exist create it
if not os.path.exists("data"):
    os.makedirs("data")

t = read_cloud('https://moralis.com/api/search/trendingTokens')
data = json.loads(t.text)

now = datetime.datetime.now()
mtime = now.strftime("%y_%m_%d_%H_%M")


# Create a dynamic filename
filename = f"data/{mtime}.json"

# Save the list to a file
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)