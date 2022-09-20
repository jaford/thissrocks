import re



m = re.match(r"(\w+) (\w+), (\w+)", "Isaac Newton, physicist")
m.group(1,2,3)

print(m.group())