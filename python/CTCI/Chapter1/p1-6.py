# 1.6 String Compression
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become
# smaller than the orginal string, your method should return the original string. You can assume the
# string has only uppercase and lowercase letters (a-z).

# O(N)
def Compress(string):
    compressed = ""
    stack = []

    for c in string:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[0] == c:
                stack.append(c)
            else:
                compressed += stack[0] + str(len(stack))
                stack = [c]
    
    compressed += stack[0] + str(len(stack))

    if len(compressed) >= len(string):
        return string
    else:
        return compressed

if __name__ == "__main__":
    print(Compress("aabcccccaaa")) # -> a2b1c5a3, will return compressed
    print(Compress("Aa")) # -> A1a1, will return original
    print(Compress("aaaA")) # -> 3aA1, will return original
    print(Compress("aaaaaaaaaaaaaaaaaaaaaaqqqqqqqqqqqqqqqqwwwwwwwsssxxxxzzzzzdddddfffrrrrrrrrr"))