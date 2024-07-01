dict = {2:'red', 'blue':[2,4], 'yellow':3}
print(dict)
print(type(dict['blue']))
#>> {'red': 1, 'blue': 2, 'yellow': 3}

popped1 = dict['blue'].remove(2)
print(popped1)
#>> 2

print(dict[2])
#>> {'red': 1, 'yellow': 3}
