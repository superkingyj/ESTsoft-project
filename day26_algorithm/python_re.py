# first = "HELLO"
# print(first[1])

# for i in reversed(range(len(first))):
#     print(first[i])

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][1])

# i = 2
# while i < 5:
#     print(i)
#     if i % 2 == 0:
#         break

string_list = ["Good", "Mornig", "Oreumi"]

# # 1번
# sent = ""
# for i in string_list:
#     sent += i + " "
# print(sent)

# 2번
# sent = string_list[0]
# for i in string_list[1:]:
#     sent += " " + i

# 3번
print(*string_list)
