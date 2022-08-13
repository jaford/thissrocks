#!/usr/bin/env python

d1 = dict()  # <1>

airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',  # <2>
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

d2 = {}
d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)  # <3>

pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
         ('Oregon', 'Salem'), ('California', 'Sacramento')]

state_caps = dict(pairs)  # <4>

print(d3['red'])  # <5>
print(airports['LAX'])

airports['SLC'] = 'Salt Lake City'  # <6>
airports['LAX'] = 'Lost Angels'  # <7>
print(airports['SLC'])
