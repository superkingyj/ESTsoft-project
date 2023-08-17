from datetime import datetime, timedelta

current_time = datetime.now()
print("전체 시간: ", current_time)

formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
print("형식 시간: ", formatted_time)

day_before = current_time - timedelta(days=1)
print("일년 전: ", day_before)
