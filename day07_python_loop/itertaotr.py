number = [1,2,3,4,5]
iterator = iter(number)

print(iterator)
print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #4
print(next(iterator)) #4
print(next(iterator)) # stop Error

