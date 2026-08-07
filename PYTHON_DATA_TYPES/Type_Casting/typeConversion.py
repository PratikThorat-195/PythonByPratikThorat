# Type casting technique is the process of cenverting one possible type value to another possible type value is called Type Casting
# =============================================
# In Python Programming, we have 5 fundamental Type casting technique
# 1. int()
# 2. float()
# 3. bool()
# 4. complex()
# 5. str() 
# ============================================
# ============================================
# 1. int()
# int() is used to converting one possible type value to int type value 
# ============================================
# Example: 1. Float to Integer TYPE (Possible)
# ============================================

a = 122.34
print(a, type(a)) #------------122.34 <class 'float'>
b = int(a)
print(b, type(b)) #------------122 <class 'int'>

p = 0.98
print(p, type(p)) #------------0.98 <class 'float'>
q = int(p)
print(q, type(q)) #------------0 <class 'int'>

r = -12.09
print(r, type(r)) #----------- -12.09 <class 'float'>
x = int(r)
print(x, type(x)) #----------- -12 <class 'int'>

# ============================================
# Example: 2. Bool to Integer TYPE (Possible)
# ============================================
a = True
print(a, type(a)) #----------- True <class 'bool'>
b = int(a)
print(b, type(b)) #----------- 1 <class 'int'>

# ============================================
# Example: 2. Bool to Integer TYPE (NOT Possible)*
# ============================================
a = (2+3j)
print(a, type(a)) #----------- (2+3j) <class 'complex'>
# b = int(a)
# print(b, type(b)) #----------- TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex' 


a = " "
print(a, type(a)) 
b=bool(a)
print(b, type(b))
a=""
print(a, type(a))
b=bool(a)
print(b, type(b))





