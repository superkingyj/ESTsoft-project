file = open("byte.txt", "rb")
context = file.read()
print(context)
file.close()

file = open("byte.txt", "wb")
file.write(b"hello")
file.close()