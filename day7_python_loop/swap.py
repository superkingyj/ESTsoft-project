# 방법 1
a = [1,2,3,4,5]
n = len(a)

for i in range(n//2):
    a[i], a[n-1-i] = a[n-1-i], a[i]

# 방법 2
a = [1,2,3,4,5]
a = a[::-1]

# 방법 3
a = [1,2,3,4,5]
a.reverse()

print(a)
