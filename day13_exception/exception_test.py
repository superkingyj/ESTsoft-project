num1, num2 = 10, 0

# try:
#     result = num1 / num2
# # except ZeroDivisionError:
# #     print("0으로 나눌 수 없습니다")
# except Exception as e:
#     print(str(e))
# finally:
#     print("에러가 나든 말든 실행")


try:
    file = open("/Users/roxyyujin/Desktop/직박구리/test.txt", "r")
    text = file.read()
except FileNotFoundError as e:
    print("Error: ", e)


try:
    mylist = [1, 2, 3]
    value = mylist[3]
    print(value)
except IndexError as e:
    print("Error: ", e)


try:
    a = input("")
    result = a + 10
except TypeError as e:
    print("Error: ", e)


try:
    a = "abc123"
    a = int(a)
except ValueError as e:
    print("Error: ", e)


try:
    mydict = {"key1": 1, "key2": 2}
    print(mydict["key3"])
except KeyError as e:
    print("Error: ", e)


try:
    file = open("/Users/roxyyujin/Desktop/직박구리/결석자.txt", "r")
    file.write("준석")
except IOError as e:  # 안됨
    print("Error: ", e)
