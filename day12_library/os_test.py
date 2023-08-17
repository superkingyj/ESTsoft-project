# 경로를 다루는 라이브러리
import os

if os.name == "nt":
    folder_path = "C:\\User\\Pron1"
elif os.name == "posix":
    folder_path = "/Users/roxyyujin/Desktop/직박구리"


if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"폴더 {folder_pat}를 생성했습니다.")
else:
    print(f"폴더 {folder_path}가 이미 존재합니다.")
