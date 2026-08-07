# tpl = (10, 34, 56, 100, 256, 0, 102)
# print(tpl, type(tpl))
# ba = bytearray(tpl)
# print(ba, type(ba))

tpl = (10, 34, 56, 100, 255, 0, 102)
print(tpl, type(tpl))
ba = bytearray(tpl)
print(ba, type(ba))
ba[0]= 11
print(ba, type(ba))
for val in ba:
    print(val)