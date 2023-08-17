def factorial(num):
    if num == 0: return 1
    else: return num * factorial(num-1)

def outter_function():
    x = 10
    
    def inner_function():
        print(x)
    
    inner_function()

# print(factorial(6))
outter_function()
    