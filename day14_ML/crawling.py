from bs4 import BeautifulSoup
import requests
import re
import datetime
from tqdm import tqdm
import sys
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}


def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9 * (num - 1)


def makeUrl(search, start_pg, end_pg):
    urls = []
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = (
            "https://search.naver.com/search.naver?where=news&sm=tab_pge&query="
            + search
            + "&start="
            + str(start_page)
        )
        print("생성url: ", url)
        urls.append(url)
        return urls
    else:
        urls = []
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = (
                "https://search.naver.com/search.naver?where=news&sm=tab_pge&query="
                + search
                + "&start="
                + str(page)
            )
            urls.append(url)
        print("생성url: ", urls)
        return urls


def news_attrs_crawler(articles, attrs):
    attrs_content = []
    for i in articles:
        attrs_content.append(i.attrs[attrs])
    return attrs_content


def articles_crawler(url):
    original_html = requests.get(i, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")

    url_naver = html.select(
        "div.group_news > ul.list_news > li div.news_area > div.news_info > div.info_group > a.info"
    )
    url = news_attrs_crawler(url_naver, "href")
    return url


def makeList(newslist, content):
    for i in content:
        for j in i:
            newslist.append(j)
    return newslist


if __name__ == "__main__":
    search = input("검색어: ")
    page_start = int(input("시작페이지?\n"))
    page_end = int(input("종료페이지\n"))

    urls = makeUrl(search, page_start, page_end)

    news_titles = []
    news_url = []
    news_contents = []
    news_dates = []

    for i in urls:
        url = articles_crawler(i)
        news_url.append(url)

    news_url_list = []
    makeList(news_url_list, news_url)

    final_urls = []

    for i in tqdm(range(len(news_url_list))):
        if "news.naver.com" in news_url_list[i]:
            final_urls.append(news_url_list[i])
        else:
            pass

    for i in tqdm(final_urls):
        news = requests.get(i, headers=headers)
        news_html = BeautifulSoup(news.text, "html.parser")

        title = news_html.select_one(
            "#ct > div.media_end_head.go_trans > div.media_end_head_title > h2"
        )
        if title == None:  # if title is None
            title = news_html.select_one("#content > div.end_ct > div > h2")

        content = news_html.select("div#dic_area")
        if not content:
            content = news_html.select("#articeBody")

        content = "".join(str(content))

        pattern1 = r"<[^>]*>"
        title = re.sub(pattern=pattern1, repl="", string=str(title))
        content = re.sub(pattern=pattern1, repl="", string=content)
        pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
        content = content.replace(pattern2, "")

        news_titles.append(title)
        news_contents.append(content)

        try:
            html_date = news_html.select_one(
                "div#ct> div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span"
            )
            news_date = html_date.attrs["data-date-time"]
        except AttributeError:
            news_date = news_html.select_one(
                "#content > div.end_ct > div > div.article_info > span > em"
            )
            news_date = re.sub(pattern=pattern1, repl="", string=str(news_date))

        news_dates.append(news_date)

    news_df = pd.DataFrame(
        {"date": news_dates, "title": news_titles, "link": final_urls, "content": news_contents}
    )
    new_df = news_df.drop_duplicates(keep="first", ignore_index=True)

    print("중복제거 행 개수: ", len(new_df))

    now = datetime.datetime.now()
    news_df.to_csv(
        "{}_{}.csv".format(search, now.strftime("%Y%m%d_%H%M%S")), encoding="utf-8-sig", index=False
    )
