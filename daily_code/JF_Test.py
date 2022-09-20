
import sys
from radarclient import RadarClient, AuthenticationStrategySPNego, ClientSystemIdentifier



system_identifier = ClientSystemIdentifier('test', '0.0.1')
print(f'system_identifier: {system_identifier}')
print(f'system_identifier: {repr(system_identifier)}')

my_radar_client = RadarClient(AuthenticationStrategySPNego(), system_identifier)
# User supplies radar # id in CLI interface
if len(sys.argv) >= 2:
    arg = sys.argv[1]
    radar_id = arg
#moved from after else statement
    my_radar = my_radar_client.radar_for_id(radar_id)
    print(my_radar)
    print(f'id: {my_radar.id}')
    for key, value in vars(my_radar).items():
        print(f'key: {key}  value: {value}')
    print(my_radar.component)
    print(my_radar.component['id'])
else:
    print("Error: a radar id is required.")
#Test code
#radar_id = 96014817
#print(f'vars of radar instance: {vars(my_radar)}')
