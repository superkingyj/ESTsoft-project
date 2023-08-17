import sys
from itertools import permutations

N = int(sys.stdin.readline())
inputs = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))
result = 0
permu = list(permutations(map(str, range(1, 10)), 3))

def check(input_num, pernu_num, strike, boll):
    _strike, _boll = 0, 0

    for i in range(3):
        for j in range(3):
            if i == j and pernu_num[i] == input_num[j]:
                _strike += 1
            elif i != j and pernu_num[i] == input_num[j]:
                _boll += 1

    return (strike == _strike) and (boll == _boll)

for pernum_num in permu:
    flag = True

    for input_num, strike, boll in inputs:
        if not check(pernum_num, list(str(input_num)), strike, boll):
            flag = False
            break

    if flag:
        result += 1

print(result)