#!/usr/bin/env python

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

for person in people:  # <1>
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product = person  # <2>
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product in people:  # <3>
    print(first_name, last_name)
print('-' * 60)
