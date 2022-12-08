#importing packages
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import json

#connecting to the API
sc = OAuth2(None, None, from_file='oauth2.json')

#accessing game object
gm = yfa.Game(sc, 'nba')

#getting league information/ID.  What leagues the player is in.
gm.league_ids(year=2022)
league = gm.league_ids()
print(f'League info is: {league}')

#creating league object. lg. will always reference this part of the code
lg = gm.to_league('418.l.184358')


#getting current week information
current_week = lg.current_week()
print(f'Current week is: {current_week}')

#getting draft order
# draft_res = lg.draft_results()
# print(len(draft_res))

#returnig free agents in 'Center' position
fa_C = lg.free_agents('C')
# #print(len(fa_C))
pretty = json.dumps(fa_C[0:20], indent=4)
# print(f'Available center is: {fa_C[0:10]}')
print(pretty)

fa_SG = lg.free_agents('SG')
# print(f'Available Shooting Guard is: {fa_SG[0:10]}')
pretty2 = json.dumps(fa_SG[0:20], indent=4)
print(pretty2)


# #print specific player data based on player id
# specific_player_id = lg.player_stats([4896],'season')
# print(specific_player_id)

specific_player = lg.player_details('Jayson Tatum')
jayson_tatum_pretty = json.dumps(specific_player, indent=4)
print(specific_player)