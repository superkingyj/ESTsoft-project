import json

with open("password.json", "r") as f:
    # json 파일 읽는 방법
    json_data = json.load(f)

print(json_data["password"])
json_data["delivery"] = "만두만두"

with open("password.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False)
