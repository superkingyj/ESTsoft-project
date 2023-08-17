from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

URL = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query="


def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9 * (num - 1)


def makeUrl(search, start_pg, end_pg):
    global URL
    urls = []

    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = URL + search + "&start=" + str(start_page)
        urls.append(url)
        print("생성 url: ", url)
        return urls
    else:
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = URL + search + "&start=" + str(page)
        return urls


def input_start():
    # 사용자 입력
    search = input("검색할 단어: ")

    page_start = int(input("시작 페이지: "))
    print(f"시작할 페이지 : {page_start}")

    page_end = int(input("종료 페이지: "))
    print(f"종료할 페이지 : {page_end}")

    # 네이버 url 생성
    search_urls = makeUrl(search, page_start, page_end)

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    naver_urls = []

    for i in search_urls:
        driver.get(i)
        time.sleep(1)

        # a태그 안에 info 클래스를 가져오기
        a = driver.find_elements(By.CSS_SELECTOR, "a.info")

        for i in a:
            i.click()

            # 첫번째 탭 열기
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)

            url = driver.current_url
            print(url)

            # 네이버 뉴스만 추가
            if "news.naver.com" in url:
                naver_urls.append(url)

            # 탭 닫기
            driver.close()

            # 검색 탭으로 돌아가기
            driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
    # input_start()
    search = "나비"

    naver_urls = [
        "https://sports.news.naver.com/news.nhn?oid=442&aid=0000163350",
        "https://n.news.naver.com/mnews/article/001/0014045673?sid=103",
        "https://n.news.naver.com/mnews/article/366/0000913600?sid=101",
        "https://n.news.naver.com/mnews/article/025/0003290622?sid=102",
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }

    payload = {"param1": "1", "param2": "2"}

    titles = []
    contents = []

    for url in naver_urls:
        original_html = requests.get(url, params=payload, headers=headers)
        html = BeautifulSoup(original_html.text, "html.parser")
        # print(html)

        title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
        title = "".join(str(title))

        pattern1 = r"<[^>]*>"  # ^: 전부다 아닌 것만 찾기
        title = re.sub(pattern=pattern1, repl="", string=title)
        titles.append(title)

        content = html.select("div#dic_area")
        content = "".join(str(content))
        content = re.sub(pattern=pattern1, repl="", string=content)
        pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
        content = content.replace(pattern2, "")
        contents.append(content)

print(titles)
print(contents)

news_df = pd.DataFrame({"title": title, "link": naver_urls, "content": contents})
news_df.to_csv(f"NaverNews_{search}.csv", index=False, encoding="utf-8-sig")
