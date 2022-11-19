#importing packages
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

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
#print(len(fa_C))
print(f'Available center is: {fa_C[0:10]}')

fa_SG = lg.free_agents('SG')
print(f'Available Shooting Guard is: {fa_SG[0:10]}')

