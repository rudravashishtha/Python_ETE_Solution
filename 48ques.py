# Question 48
# (a)
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both) 

# (b)
L1 = ["bacon", "eggs"]
L2 = ["toast", "jam"]
brunch = L1
L1.append("juice")
brunch.extend(L2)

print(brunch)