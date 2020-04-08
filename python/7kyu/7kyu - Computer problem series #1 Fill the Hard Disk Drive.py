# Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive.

# Input:
# Array of file sizes (0 <= s <= 100)
# Capacity of the HD (0 <= c <= 500)
# Output:
# Number of files that can be fully saved in the HD
# Examples:
# save([4,4,4,3,3], 12) -> 3
# # 4+4+4 <= 12, but 4+4+4+3 > 12
# save([4,4,4,3,3], 11) -> 2
# # 4+4 <= 11, but 4+4+4 > 11
# Do not expect any negative or invalid inputs.

# Best Practices
def save(sizes, hd): 
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)

# My answer
def save(sizes, hd):
    size = 0
    count = 0
    for i in sizes:
        if size + i > hd:
            break
        size += i
        count += 1
    return count