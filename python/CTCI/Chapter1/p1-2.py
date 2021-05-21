# 1.2 Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

# O(N)
def CheckPerm(str1, str2):
    if len(str1) != len(str2):
        return False
    
    dict1 = {}
    dict2 = {}

    for i in range(len(str1)):
        if str1[i] in dict1:
            dict1[str1[i]] += 1
        else:
            dict1[str1[i]] = 1

        if str2[i] in dict2:
            dict2[str2[i]] += 1
        else:
            dict2[str2[i]] = 1

    for key in dict1.keys():
        if key in dict2:
            if dict1[key] != dict2[key]:
                return False
        else:
            return False

    return True

if __name__ == "__main__":
    print(CheckPerm("abc", "bac"))
    print(CheckPerm("aaa", "aaaa"))
    print(CheckPerm("taco", "cato"))
