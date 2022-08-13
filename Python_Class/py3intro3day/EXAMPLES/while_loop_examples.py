#!/usr/bin/env python

print("Welcome to ticket sales\n")

while True:  # <1>
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # <2>
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # <3>

    quantity = int(raw_quantity)  # could validate via try/except
    print("sending {} ticket(s)".format(quantity))
