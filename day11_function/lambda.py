def add(a,b):
    return a+b

add = lambda a, b: a+b
result = add(2,3)
print(result)

numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2, numbers))
print(squared)