#!/usr/bin/env python

d1 = dict()

airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

d2 = {}
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)

pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
         ('Oregon', 'Salem'), ('California', 'Sacramento')]

state_caps = dict(pairs)

print(d3['red'])
print(airports['LAX'])

airports['SLC'] = 'Salt Lake City'
airports['LAX'] = 'Lost Angels'
print(airports['SLC'])  # <1>

key = 'PSP'
if key in airports:
    print(airports[key])  # <2>

print(airports.get(key))  # <3>
print(airports.get(key, 'NO SUCH AIRPORT'))  # <4>

print(airports.setdefault(key, 'Palm Springs'))  # <5>
print(key in airports)  # <6>
