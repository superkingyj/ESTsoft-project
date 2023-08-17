encoded_text = b"\xbc\xd3\xd3\xcd"

with open("codecs_list.txt", "r") as file:
    codecs = file.read().replace(",", "").replace("\n", " ").split(" ")

for codec in codecs:
    try:
        print(encoded_text.decode(codec), codec)
    except:
        pass
