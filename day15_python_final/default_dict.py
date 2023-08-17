from collections import defaultdict

text = "나,는 사과, 를 먹기, 위해서, 사과, 를 했습니다."
word_list = list(map(lambda x: x.replace(",", ""), text.split(" ")))
my_dict = defaultdict(int)

for word in word_list:
    my_dict[word] += 1

print(my_dict)
