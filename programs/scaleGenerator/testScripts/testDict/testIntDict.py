import nba_api.stats.endpoints
from nba_api.stats.endpoints import playercareerstats

career = playercareerstats(player_id='2544') 

playerStats = career.get_data_frames()[0]
minCurrentSeason = player_stats['MIN'].iloc[-1]
minConverted = int(minCurrentSeason)
print(minConverted)
print(type(minConverted))