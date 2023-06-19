# Question 38

file = open("Report.txt", 'a') # Will create the file if not in the directory
file.close()
def count_lines():
    filename = "Report.txt"
    count = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip() # Removing unwanted spaces

            # Check if the line starts with 'I' or 'M'
            if line.startswith('I') or line.startswith('M'):
                count += 1

    print("Number of lines starting with 'I' or 'M':", count)

count_lines()



