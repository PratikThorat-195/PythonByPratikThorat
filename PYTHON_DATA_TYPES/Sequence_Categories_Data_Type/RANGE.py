# range
r = range(6)
print(r, type(r)) # range(0, 6) <class 'range'>

range(0, 6)
for val in range(6):
  print(val)
# 0
# 1
# 2
# 3
# 4
# 5

r = range(10, 16)
print(r, type(r)) # range(10, 16) <class 'range'>
for val in r:
  print(val)

# 10
# 11
# 12
# 13
# 14
# 15
print("-----------------------------------")

r= range(16, 10)
print(r, type(r))
for val in r:
  print(val)

print("----------------------------------")

r = range(-11, 0)
print(r, type(r)) # range(0, -11) <class 'range'>
for val in r:
  print(val)

print("---------------------------------")

q = range(-10, 0)
for val in q:
  print(val)

print("---------------------------------")

c = range(0, 101, 10)
for val in c:
  print(val)

print("-------------------=============================================================================--------------")
for val in range(11):
  print(val)

print("-------------------=============================================================================--------------")
for val in range(10, 21):
  print(val)

print("-------------------=============================================================================--------------")
for val in range(1000, 1006):
    print(val)

print("-------------------=============================================================================--------------")

for val in range(10, 21, 2):
  print(val)

print("-------------------=============================================================================--------------")
for val in range(100, 201, 10):
  print(val)

print("-------------------=============================================================================--------------")
for val in range(10, -1):
  print(val)

print("-------------------=============================================================================--------------")
for val in range(10, 0, -1):
  print(val)

for val in range(201,9, -10):
  print(val)

for val in range(-10, -16, 1):
  print(val)

for val in range(-100, -9, 10):
  print(val , end="  ")

for val in range(-5, 6, 2):
  print(val) 

for val in range(-10, 10, ):
  print(val)

for val in range()