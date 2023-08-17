def calculation1(func):
    def wrapper(*args, **kwargs):
        print("데코레이터1 시작")
        func(*args, **kwargs)
        print("데코레이터1 종료")

    return wrapper


def calculation2(func):
    def wrapper(*args, **kwargs):
        print("데코레이터2 시작")
        func(*args, **kwargs)
        print("데코레이터2 종료")

    return wrapper


@calculation1
@calculation2
def add(a, b):
    print(a + b)


add(3, 5)
