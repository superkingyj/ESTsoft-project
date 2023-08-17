def calculation(func):
    def wrapper(*args, **kwargs):
        print("계산을 시작하겠습니다.")
        func(*args, **kwargs)
        print("계산을 완료했습니다.")

    return wrapper


@calculation
def add(a, b):
    print(a + b)


@calculation
def minus(a, b):
    print(a - b)


@calculation
def multiply(a, b):
    print(a * b)


@calculation
def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")


result_add = add(3, 5)

result_minus = minus(3, 5)

result_multiply = multiply(3, 5)

result_divide = divide(3, 5)
