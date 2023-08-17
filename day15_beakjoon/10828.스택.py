from functools import reduce

arr = [1, 2, 3, 4, 5]

arr_plus_one = list(map(lambda x: x + 1, arr))
arr_join = reduce(lambda x, y: str(x) + str(y), arr)
arr_odd = list(filter(lambda x: x % 2, arr))

print(arr_odd)
