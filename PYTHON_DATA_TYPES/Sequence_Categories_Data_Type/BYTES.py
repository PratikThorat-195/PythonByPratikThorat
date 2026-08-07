# lst = [10,34,100,56, 256, 0,102]
# print(lst, type(lst))
# b=bytes(lst)
# print(b, type(b))

lst = [10,34,100,56,255,0,102]
print(lst, type(lst))
b=bytes(lst)
print(b, type(b))
for val in b:
 print(val, id(val))

