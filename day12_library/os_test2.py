import glob
import os

# 현재 파이썬 파일 경로 가져오기
current_path = os.path.abspath(__file__)
print(current_path)

# recursive = True: 하위폴더까지 다 검사
jpg_files = glob.glob("/Users/roxyyujin/Desktop/**/*.JPG", recursive=True)

for image in jpg_files:
    print(image)
