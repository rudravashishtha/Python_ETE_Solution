# Question 13

Ram = int(input("Enter Ram age: "))
Sam = int(input("Enter Sam age: "))
Khan = int(input("Enter Khan age: "))

if Ram > Sam and Ram > Khan:
    print("Ram is eldest")
    if Sam > Khan:
        print("Khan is youngest")
    else:
        print("Sam is Youngest")
        
elif Sam > Ram and Sam > Khan:
    print("Sam is eldest")
    if Ram > Khan:
        print("Khan is youngest")
    else:
        print("Ram is Youngest")
    
    
elif Khan > Ram and Khan > Sam:
    print("Khan is eldest")
    if Ram > Sam:
        print("Sam is youngest")
    else:
        print("Ram is Youngest")
    


