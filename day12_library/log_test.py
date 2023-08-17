import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(message)s", filename="log.txt")

cnt = 0
while cnt < 5:
    logging.info("수업을 잘 듣고 있는지 감시중입니다...")
    time.sleep(3)
    cnt += 1

logging.error("수업 안듣는 교육생을 발견!")
