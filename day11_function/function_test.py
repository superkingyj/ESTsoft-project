def greet(name):
    print("반값습니다! {} 여러분!".format(name))

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def mutiply(a, b=2):
    return a*b

def sum(*args):
    total = 0
    for num in args: 
        total += num 
    return total

def character_info(name, age): 
    print("이름: ", name)
    print("나이: ", age)

greet("oreumi")

# result = add(3,4)
# result = mutiply(3, 3) 
# result = sum(1,2,3,4,5,6,7,8,9,10)
character_info(name="김유진", age=20)
# print(result)

