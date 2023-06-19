# Question 19

class Py:
    def get_String(self, str):
        self.str = str
    def print_String(self):
        print(self.str.upper())


str = input("Enter a String: ")

p1 = Py()

p1.get_String(str)
print("String in uppercase: ", end="")
p1.print_String()
