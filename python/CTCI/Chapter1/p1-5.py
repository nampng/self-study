# 1.5 One Away
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# Example
# pale, ple -> True
# pales, pale -> True
# pale, bale -> True
# pale, bake -> False

# O(N)
def OneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    dict1 = {} 
    dict2 = {}

    for c in str1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1

    for c in str2:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1

    diff = 0

    if len(str1) > len(str2):
        for key in dict1.keys():
            if diff > 1:
                return False
            if key in dict2:
                if dict1[key] != dict2[key]:
                    diff += abs(dict1[key] - dict2[key])
            else:
                diff += dict1[key]
    else:
        for key in dict2.keys():
            if diff > 1:
                return False
            if key in dict1:
                if dict2[key] != dict1[key]:
                    diff += abs(dict2[key] - dict1[key])
            else:
                diff += dict2[key]

    if diff < 2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(OneAway("pale", "ple"))
    print(OneAway("pales", "pale"))
    print(OneAway("pale", "bale"))
    print(OneAway("pale", "bake"))
    print(OneAway("paless", "pale"))