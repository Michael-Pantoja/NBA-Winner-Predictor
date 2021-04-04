import pandas as pd
import requests
from bs4 import BeautifulSoup
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from tqdm import tqdm


playerList = []
df = []

player_dict = players.get_active_players()

for i in player_dict:
    playerList.append(i['id'])

gamelog = playergamelog.PlayerGameLog(player_id = playerList[0], season = SeasonAll.all)

lst = gamelog.get_data_frames()

lst.to_csv('PlayerDataTest.csv')

for i in tqdm(list(range(0, len(playerList)))):
# for i in tqdm(list(range(0, 2))): # This was used to test the parser,
    gl = playergamelog.PlayerGameLog(player_id = playerList[i], season = SeasonAll.all)
    temp_df = gl.get_data_frames()
    temp_df = temp_df[0]
    lst = lst.append(temp_df, ignore_index = True)

lst.to_csv('PlayerData.csv')