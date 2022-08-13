#!/usr/bin/env python

pythons = ["Idle", "Cleese", "Chapman", "Gilliam", "Palin", "Jones"]

characters = "Roger", "Old Woman", "Prince Herbert", "Brother Maynard"

phrase = "She turned me into a newt"

print("pythons:", pythons)
print("pythons[0]", pythons[0])  # <1>
print("pythons[5]", pythons[5])  # <2>
print("pythons[0:3]", pythons[0:3])  # <3>
print("pythons[2:]", pythons[2:])  # <4>
print("pythons[:2]", pythons[:2])  # <5>
print("pythons[1:-1]", pythons[1:-1])  # <6>
print("pythons[0::2]", pythons[0::2])  # <7>
print("pythons[1::2]", pythons[1::2])  # <8>

pythons[3] = "Innes"
print("pythons:", pythons)
print()

print("characters", characters)
print("characters[2]", characters[2])
print("characters[1:]", characters[1:])

# characters[2] = "Patsy"  # ERROR -- can't assign to tuple
print()
print("phrase", phrase)
print("phrase[0]", phrase[0])
print("phrase[-1]", phrase[-1])  # <9>
print("phrase[21:25]", phrase[21:25])
print("phrase[21:]", phrase[21:])
print("phrase[:10]", phrase[:10])
print("phrase[::2]", phrase[::2])
