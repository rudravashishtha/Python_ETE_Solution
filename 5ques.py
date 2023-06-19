# (a) Show the value of L after you run the code below?
L = ["life", "answer", 42, 0]
for thing in L:
    if thing == 0:
        L[thing] = "universe"
    elif thing == 42:
        L[1] = "everything"
        
print(L)

# (b) Show the value of L3 after you execute all the operations in the code below?
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2 # L4 = ['re', 'mi']
L3.extend(L4) # L3 = [ 'do', 're', 'mi']
L3.sort() # ['do', 'mi', 're']
del(L3[0]) # ['mi', 're']
L3.append(['fa','la']) # ['mi', 're', ['fa', 'la']]
print(L3)

