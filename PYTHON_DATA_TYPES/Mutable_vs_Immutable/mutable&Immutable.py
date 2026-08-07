# String is immutable in Python
num = "Pratik"
print(num)
print(id(num)) # ----> 1711633420944
# num [0] = "J" # TypeError: 'str' object does not support item assignment

num = "Jratik"
print(num)
print(id(num)) # ----> 1711633421376

# ------------------------------------------------------------------------------
# Integer is immutable in python
a = 10
print(a, id(a)) # 10 140724209616280

a+=1
print(a, id(a)) # 11 140724209616312

print("=====================================================================================================")


# =======================================================================================================
# mutable 
grades = [9,18,27]
print(grades, id(grades))  # [9, 18, 27] 2316994525440
grades[0] = 5
print(grades, id(grades))  # [5, 18, 27] 2316994525440
grades.append(81)
print(grades, id(grades))  # [5, 18, 27, 81] 2316994525440

print("=====================================================================================================")

t = 5
q = t
print(t, q)
print(id(t))
print(id(q))