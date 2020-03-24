# You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Example:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

# Note
# consecutive strings : follow one after another without an interruption

# Best Practices
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

'''
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
'''

# My answer
def longest_consec(strarr, k):
    if k <= 0 or len(strarr) < k:
        return ""
    else:
        longest = index = 0
        for i in range(len(strarr)):
            length = sum([len(x) for x in strarr[i: i + k]])
            if length > longest:
                longest = length
                index = i
                
        return ''.join(strarr[index: index + k])