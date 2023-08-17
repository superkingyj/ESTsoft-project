data = []

with open("file_1.txt", "r") as f:
    for line in f.readlines():
       data.append(line.rstrip())

data.sort()
print("전체 정렬: ", data)
print("전체 개수: ", len(data))
print("중복을 제거하고 남은 개수: ", len(set(data)))