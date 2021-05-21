# 1.1 Is Unique
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# O(N)
def HasDuplicate(input_string):
    char_dict = {}
    for char in input_string:
        if char in char_dict:
            return True
        else:
            char_dict[char] = 1
        
    return False

# No dictionary
# O(N^2)
def HasDuplicate2(input_string):
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string)):
            print(f"Search - {input_string[i]} and {input_string[j]}")
            if input_string[i] == input_string[j]:
                print(f"Found - {input_string[i]} and {input_string[j]}")
                return True
    return False

if __name__ == "__main__":
    print()
    print(HasDuplicate2("abc"))
    print()
    print(HasDuplicate2("aabc"))
    print()
    print(HasDuplicate2("abcc"))
    print()
    # print(HasDuplicate2("qwertyuiopasdfghjklzxcvbnmq"))