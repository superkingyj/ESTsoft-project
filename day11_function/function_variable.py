global_var = 100

def my_func():
    global global_var 
    
    local_var = 50
    global_var += 50
    print("전역 변수: ", global_var)
    print("지역 변수: ", local_var)

def get_person():
    return "yujin", 25, "yujin0707@gmail.com"

def type_hint(a:int, b:int) -> int:
    """
    Keyword arguments: a, b
    argument -- a값, b값 
    Return: return_description
    """
    return a+b
    
def 

# my_func()

# name, age, email = get_person()
# print(name, age, email)

