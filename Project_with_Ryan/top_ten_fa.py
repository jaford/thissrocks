#importing packages
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import json
import numpy as np
import pandas as pd

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

# #returnig free agents in 'Center' position
# fa_C = lg.free_agents('C')
# print('Top 10 Centers are:\n '
#       , pd.DataFrame(fa_C[0:10]))
# # #print(len(fa_C))
# pretty = json.dumps(fa_C[0:20], indent=4)
# # print(f'Available center is: {fa_C[0:10]}')
# print(pretty)

#Printing top ten free agents by position
# fa_SG = lg.free_agents('SG')
# print('Top 10 Shooting Guards are:\n '
#       , pd.DataFrame(fa_SG[0:10]))
# top_ten_fa_SG = json.dumps(fa_SG[0:10], indent=4)
# print(top_ten_fa_SG)

#
# fa_PF = lg.free_agents('PF')
# #using pandas to print data
# print('Top 10 Power Forwards are:\n '
#       , pd.DataFrame(fa_PF[0:10]))
#using json to print out data
# top_ten_fa_PF = json.dumps(fa_PF[0:10], indent=4)
# print(top_ten_fa_PF)
#
fa_F = lg.free_agents('F')
#print(lg.free_agents('F'))
# print('Top 10 Forwards are:\n '
#       , pd.DataFrame(fa_F[0:10]))
#top_ten_fa_F = json.dumps(fa_F[0:10], indent=4)
#print(top_ten_fa_F)
print('Top 10 Forwards are:\n '
      , pd.DataFrame(fa_F[0:10]))
#
# fa_Util = lg.free_agents('Util')
# print('Top 10 Util Players are:\n '
#       , pd.DataFrame(fa_Util[0:10]))
# top_ten_fa_Util = json.dumps(fa_Util[0:10], indent=4)
# print(top_ten_fa_Util)
#
#Print specific player bsaed on player ID
# player_stats = lg.player_stats([5765,3704],'season')
# #print(player_stats)
# print(pd.DataFrame(fa_PF))
#
# specific_player = lg.player_details('Jayson Tatum')
# jayson_tatum_pretty = json.dumps(specific_player, indent=4)
# print(jayson_tatum_pretty)

