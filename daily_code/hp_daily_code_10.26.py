

tuple_example = {"code":3221229823,"flags":6,"namespace":"FRONTBOARD","reasons":["<RBSTerminateContext| domain:10 code:0xC00010FF explanation:%CPU:                41.92% (sampled for 10.0 s)","ProcessVisibility: Background","ProcessState: Running","ThermalInfo: (","\"Thermal Level:   12\",","\"Thermal Sensors: 0\"",") reportType:CrashLog maxTerminationResistance:Interactive>"]}

dict_convert = dict(tuple_example)
print(type(dict_convert))
list_in_dict = dict_convert["reasons"]
print(type(list_in_dict))

# if "code" in list_in_dict:
#     print('Found the code!')
# else:
#     print('Did not find code :(')

s1 = list_in_dict[0]
if "code" in s1:
    l1 = s1.split(" ")

for x in l1:
    if "code:" in x:
        print(x.replace("code:", "Test: "))



# for i in list_in_dict:
#     print(i)
#     if "code" in i:
#         arg1 = i[0]       
#         print(arg1)

# arg_2 = list_in_dict[0]
# print(type(arg_2))

# split_strg = arg_2.split()
# print(type(split_strg))
# print(split_strg)






# for x in tuple_example:
#     print('In first loop')    
#     print(x,"\n")

#     if "reasons" in x:
#         print('You are in the 1st if')
#         var1 = x["reasons"]
#         print(var1)
#         print(type(var1), "\n")
#         print(var1[0], "\n")

#         for x in var1:
#             print('In second loop')    
#             print(x, "\n")
#             string1 = "<RBSTerminateContext| domain:10 code:0xC00010FF explanation:%CPU:                41.92% (sampled for 10.0 s)"
#             if string1 in var1:
#                 print('You are in the 2nd if')
#                 print(len(string1))
#                 print(string1[32:47],"\n")
#                 break
#         else:
#             break
#     break
# print('Out of the first for loop\n')



