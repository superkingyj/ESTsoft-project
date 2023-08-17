a = [1,2,-3,4,5]
max_val = a[0]

for num in a:
    if max_val < num:
        max_val = num
    
print(max_val)