# Question 12

def get_permutations(s):
    if len(s) == 1:
        return [s]
    
    permutations = []
    for i in range(len(s)):
        first_char = s[i]
        remain_chars = s[:i] + s[i+1:]
        sub_perms = get_permutations(remain_chars)
        for sub_perm in sub_perms:
            permutations.append(first_char + sub_perm)
        
    return permutations

# s = input("Enter a string: ")

# print(get_permutations(s))

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

