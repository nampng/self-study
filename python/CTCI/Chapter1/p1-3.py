# 1.3 URLify
# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.

# O(N)
def Urlify(string):
    string = string.split(' ')
    seperator = '%20'
    string = seperator.join(string)
    return string

print(Urlify("Mr John Smith"))