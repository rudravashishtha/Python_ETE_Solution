# Question 17

# (a) Show the output of the following Python code?
#  d = {"john":40, "peter":45}
#  d["john"]
# b) Is tuple comparison possible? Explain how with example.

# (a)
d = {"john":40, "peter":45}
print(d["john"])


# (b)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (1, 2, 4)

print(tuple1 < tuple2)  
print(tuple2 > tuple3)  
print(tuple1 == tuple3) 
