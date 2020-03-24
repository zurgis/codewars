# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

# Best Practices
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# My answer
def is_isogram(string):
    value = []
    if string == '':
        return True
        
    for i in string.lower():
        if i not in value:
            value.append(i)
        else:
            return False
        
    if value:
        return True