# import sys

# A, B, V= map(int,sys.stdin.readline().split())

# result = (V-B) / (A-B)
# print(int(result) if result.is_integer() else int(result)+1)

"""
X: 올라가는데 걸리는 시간

A*X - B*(X-1) = V
AX - BX + B = V
X(A-B) = V-B
X = (V-B) / (A-B)


"""