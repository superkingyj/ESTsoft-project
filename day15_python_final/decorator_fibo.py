import time
from functools import wraps, lru_cache, cached_property


def clock(func):
    @wraps(func)
    def clocked(*args, **kwrags):
        t0 = time.time()
        result = func(*args, **kwrags)  # <-- 함수 실행
        elasped = time.time() - t0  # <-- 함수가 실행된 총 시간
        name = func.__name__  # <-- 함수의 이름 =
        arg_lst = []

        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))  # <-- repr: 따옴표를 붙여줌

        if kwrags:
            pairs = [
                "%s=%r" % (k, w) for k, w in sorted(kwrags.itmes())
            ]  # <-- %s(문자), %r(문자에 따옴표 추가) 자리에 k, w를 각각 집어넣음
            arg_lst.append(", ".join(pairs))

        arg_str = ", ".join(arg_lst)
        print("[%0.8fs] %s(%s) -> %r" % (elasped, name, arg_str, result))  # <- %0.8f: 소숫점 8자리까지 출력
        return result

    return clocked


# @cached_property  # <-- 이거 왜 안됨?
@clock
@lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(6))
