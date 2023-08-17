a = [1, "1", True, None, [1,2]]
b = (1, "1", True, None, [1,2])


a[1] = False
print(a)

b[1] = False
print(b)
