a = {"이름":"김유진", "나이": 26, "직업": "학생", "일일퀴즈성적": [10, 20, 30]}
b = {"이름":"김예진", "나이": 20, "직업": "학생", "일일퀴즈성적": [9, 19, 29]}

# key, value 가져오기
for key, val in a.items():
    print(key, val)

# key만 가져오기
for key in a.keys():
    print(key)

# value만 가져오기
for val in a.values():
    print(val)

# 데이터 한번에 추가
a.update({"a":"b", "c":"d"})


# for i in range(len(gangs)):
#     gangsa[i].update(gangsa_add_info)
    
    