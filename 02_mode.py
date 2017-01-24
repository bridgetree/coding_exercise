# Create a dictionary of number frequencies

d = {}
for i in lst:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
    
# Find the key with maximum value

max = 0
mode = 0
for key, value in d.items():
    if d[key] > max:
        max = d[key]
        mode = key

print mode, max
