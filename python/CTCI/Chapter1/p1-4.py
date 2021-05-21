# 1.4 Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase tha is the same forwards or backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words. You can ignore casing and non-letter characters.

# O(N)
def PalinPerm(string):
    c_dict = {}
    string = string.replace(" ", "")
    string = string.lower()
    print(string)
    for c in string:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1
    
    odd = False

    for key in c_dict.keys():
        if c_dict[key] % 2 != 0:
            if odd == False:
                odd = True
            else:
                return False
    
    return True

print(PalinPerm("Tact Coa"))