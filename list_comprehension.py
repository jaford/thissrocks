num:[]
for num in range(1,101):
    if num % 5 == 0 and num % 25 == 0:
        print(num)

#x for x in interable
newlist = [num for num in range(1,101) if num % 5 == 0 and num % 25 ==0]
print(newlist)
