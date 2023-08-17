file_path = "title.txt"
file = open(file_path, 'r+', encoding="utf-8")

content = file.read()
print(content)

file.close()

file_path = "context.txt"

file = open(file_path, 'a')

file.write("Another text")

file.close()