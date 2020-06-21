# Concatenate a list of items using Python

li = [0, 1, 2, 3, 4]

# Method 1
print("".join([str(i) for i in li]))

# Method 2
print("".join(str(i) for i in li))

# Method 3
print("".join(map(str, li)))

# Method 4
s = ""
for i in li:
    s += str(i)
print(s)