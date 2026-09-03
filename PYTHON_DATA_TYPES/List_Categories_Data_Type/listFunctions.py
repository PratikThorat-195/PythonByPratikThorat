# List Fuctions
# ==============================================================================================================================================
# 2. insert()
# Syntax: listObject.insert(index, value)
# =>This Function is used for adding the value to list object at Specified Index 
# =>When we enter Invalid Possitive Index then the value inserted at Last/End of List object
# =>When we enter Invalid Negative Index then the value inserted at First of List object
# ---------
# Examples
# ---------
lst1 = [10, "Pratik", 23.45]
print(lst1, id(lst1))       #-------------> [10, 'Pratik', 23.45] 1592852658432

lst1.insert(2, 67.5504350)
print(lst1, id(lst1))       #-------------> [10, 'Pratik', 67.550435, 23.45] 1592852658432

lst1[-1] = "Python"
print(lst1, id(lst1))       #-------------> [10, 'Pratik', 67.550435, 'Python'] 1592852658432  

lst1.insert(-1, 2+3j)
print(lst1, id(lst1))       #-------------> [10, 'Pratik', 67.550435, (2+3j), 'Python'] 1592852658432  <--- observe it carefully

lst1.insert(10, "Pratik")
print(lst1, id(lst1))       #-------------> [10, 'Pratik', 67.550435, (2+3j), 'Python', 'Pratik'] 1592852658432 <--- placed at end

lst1.insert(-10, "Thorat")
print(lst1, id(lst1))       #-------------> ['Thorat', 10, 'Pratik', 67.550435, (2+3j), 'Python', 'Pratik'] 1592852658432 <--- placed at start


# ==============================================================================================================================================
# 3. clear()
# Syntax: listobject.clear()
# => This function is used to remove all the elements of the non-empty list object.
# => When we call clear() on empty list object then we get No Output / None
# -----------
# Examples:
# -----------
listClear = [10, "Pratik", 99.890, "Python"]
print(listClear, id(listClear), len(listClear)) # ---> [10, 'Pratik', 99.89, 'Python'] 2082596218304 4

listClear.clear()
print(listClear, id(listClear), len(listClear)) # ---> [] 2082596218304 0

print([].clear)  #---> <built-in method clear of list object at 0x0000028ABA8771C0>
# ==============================================================================================================================================

# 4. remove()
listRemove = [10, "Rossum", "Pratik", 450.33,True]
print(listRemove, id(listRemove), len(listRemove)) #---> [10, 'Rossum', 'Pratik', 450.33, True] 2699864928704 5

listRemove.remove("Rossum")
print(listRemove, id(listRemove), len(listRemove)) #---> [10, 'Pratik', 450.33, True] 2699864928704 4

listRemove.remove(10)
print(listRemove, id(listRemove), len(listRemove)) #---> ['Pratik', 450.33, True] 2699864928704 3

listRemove.remove("Pratik")
print(listRemove, id(listRemove), len(listRemove)) #---> [450.33, True] 2699864928704 2

# listRemove.remove("Thorat")
# print(listRemove) #------------------------------------> ValueError: list.remove(x): x not in list

# --------------------------------------------------------------------------
# print(listRemove)
# listRemove.remove()
#  listRemove.remove()
# ~~~~~~~~~~~~~~~~~^^
# TypeError: list.remove() takes exactly one argument (0 given)
# print(listRemove)
# --------------------------------------------------------------------------

lst2 = [12, 12, 34,48977, 83487, "Pratik","Pratik", 34, 256]
print(lst2, len(lst2), id(lst2)) #-------------[12, 12, 34, 48977, 83487, 'Pratik', 'Pratik', 34, 256] 9 2194774228352
lst2.remove(12)
print(lst2, len(lst2), id(lst2)) #-------------[12, 34, 48977, 83487, 'Pratik', 'Pratik', 34, 256] 8 2194774228352
#                                               ^                        
#  here remove method will remove first occurance of duplicate record. there for it removes first 12 element of the list
lst2.remove(34)

print(lst2, len(lst2), id(lst2)) #-------------[12, 48977, 83487, 'Pratik', 'Pratik', 34, 256] 7 2194774228352
#                                                  ^    
lst2.remove("Pratik")
print(lst2, len(lst2), id(lst2)) #-------------[12, 48977, 83487, 'Pratik', 34, 256] 6 2194774228352

# lst2.remove("Pratik", 256)
#  lst2.remove("Pratik", 256)
#    ~~~~~~~~~~~^^^^^^^^^^^^^^^
# TypeError: list.remove() takes exactly one argument (2 given)

print("**************************************************************************************")
lst = [10, 20, 30, 40, 50]
print(lst, type(lst), id(lst))

del lst[::2]
print(lst, type(lst), id(lst))

del lst
# print(lst, type(lst), id(lst))

# lst3 = ["Pratik", 90, 99, 99.00]
# del lst3
# print(lst3, type(lst3), id(lst3))

lst = [10, 20,30,40,10,60, 70, 10, 30]
lst.index(10)
print(lst)

print("--------------------------------------------------------------------------------------------")
print("Deep copy")
lst4 =[10, 20, 30, 34.458, "Pratik", True]
lst5 = lst4
print(lst5, id(lst5)) # [10, 20, 30, 34.458, 'Pratik', True] 2161907761664
print(lst4, id(lst4)) # [10, 20, 30, 34.458, 'Pratik', True] 2161907761664

lst4.append("Python")
print(lst5, id(lst5)) # [10, 20, 30, 34.458, 'Pratik', True, 'Python'] 2161907761664
print(lst4, id(lst4)) # [10, 20, 30, 34.458, 'Pratik', True, 'Python'] 2161907761664

print("--------------------------------------------------------------------------------------------")

print("Shallow Copy")
lst6 = [10, 20, 34.65, "Thorat", True]
lst7 = lst6.copy()
print(lst6, id(lst6)) # [10, 20, 34.65, 'Thorat', True] 2028743197056
print(lst7, id(lst7)) # [10, 20, 34.65, 'Thorat', True] 2028743197568

lst6.append("Python") 
print(lst6, id(lst6)) # [10, 20, 34.65, 'Thorat', True, 'Python'] 2028743197056
print(lst7, id(lst7)) # [10, 20, 34.65, 'Thorat', True] 2028743197568

print("--------------------------------------------------------------------------------------------")
print("count()")
lstobj =[10, 20, 30, 40, 50,30, 40, 500, 20, 30,60, 70,80, 90, 90 ,90] 
print(lstobj, id(lstobj)) # 10, 20, 30, 40, 50, 30, 40, 500, 20, 30, 60, 70, 80, 90, 90, 90] 1564208235712
print("Count of 10 = ", lstobj.count(10)) # Count of 10 =  1
print("Count of 20 = ", lstobj.count(20)) # Count of 20 =  2
print("Count of 90 = ", lstobj.count(90)) # Count of 90 =  3
print("Count of 00 = ", lstobj.count(00)) # Count of 00 =  0

print("--------------------------------------------------------------------------------------------")
print("reverse()")
listObj = ["Pratik", "Umesh", "Thorat", 26, 15, 99.99]
print(listObj, id(listObj)) # ['Pratik', 'Umesh', 'Thorat', 26, 15, 99.99] 2650428879040
listObj.reverse()
print(listObj, id(listObj)) # [99.99, 15, 26, 'Thorat', 'Umesh', 'Pratik'] 2650428879040

print("--------------------------------------------------------------------------------------------")
print("extend()")
listObj1 =[10, 20, 30, 40, 50,]
print(listObj1, id(listObj1)) # [10, 20, 30, 40, 50] 2662803649024

listObj2 =["Pratik", "Umesh", "Thorat", 26, 15, 99.99]

listObj1.extend(listObj2)

print(listObj1, id(listObj1)) # [10, 20, 30, 40, 50, 'Pratik', 'Umesh', 'Thorat', 26, 15, 99.99] 2662803649024

listObj3 = [True,"Thorat"]

#  listObj1.extend(listObj2, listObj3)

#  print(listObj1, id(listObj1)) # TypeError: list.extend() takes exactly one argument (2 given)

#  listObj1.extend(listObj2, listObj3)
#  ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
listObj1.extend(listObj2)
listObj1.extend(listObj3)
print(listObj1) # [10, 20, 30, 40, 50, 'Pratik', 'Umesh', 'Thorat', 26, 15, 99.99, 'Pratik', 'Umesh', 'Thorat', 26, 15, 99.99, True, 'Thorat']

# you can use + operator for extend
lst10 = [10,20,30]
lst20 = [40,50,60]
lst30 = [70,80,90]

lst10=lst10+lst20+lst30
print(lst10) # [10, 20, 30, 40, 50, 60, 70, 80, 90]
lst10.reverse()
print(lst10) # [90, 80, 70, 60, 50, 40, 30, 20, 10]