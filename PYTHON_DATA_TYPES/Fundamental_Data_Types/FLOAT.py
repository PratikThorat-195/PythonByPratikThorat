# ===========================================
#  Float
# ===========================================
# Proerties
# => 'float' is one of the pre-defined class name and treated as Fundamental data type.
# => The puropse of float data type "to store Real Constant values OR floating / Double pointing values.
#    (Number with Decimal Places)
# ============================================================
# Example                             OUTPUT
# ============================================================
a =12.34
print(a, type(a))  # ----------------12.34 <class 'float'>

b = 0.9
print(b, type(b)) #------------------0.9 <class 'float'>


c= a+b
print(c,type(c)) #-------------------13.24 <class 'float'>

# ====================
# Float Data type does not allows us to reprensent / store Binary, Octal and Hexadecimal value
# ====================
# a = 0b1010.0b111 --------> Output -> invalid decimal literals

# ==================================================================================================================
# Float Data Types allows us to store scientifc notation data
# Scientific Notation = Mantisa e exponent
#                     |
#                     \/                       Exponent
#       Eqv Floating point value = Mantisa x 10 
# 
# Examples: 
# >>> a=3e2 ----------------------- 3 x 10^2
#   ------------------------------- 3 x 100 = 300.0
# -----------------------
# Example
# -----------------------
p = 3e2
print(p, type(p)) #---------------- 300.0 <class 'float'>

# ----------------------
q = 3e-2
print(q, type(q)) #---------------- 0.03 <class 'float'>

a = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009
print(a, type(a)) #---------------- 9e-279 <class 'float'>
# ===================================================================================================
# The advantage of Scientific Notation is that to take less memory space bigger floating point value.

