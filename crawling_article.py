"""
크롤러 만들기
1. input JSON 읽기 -> URL, 파일명 // 완료
2. 제목, 본문 크롤링
3. 크롤링 결과(text) 저장 // 완료
This is dev branch!
"""
# -*- coding: utf-8 -*-

import os
import json


def read_article_data(path):
    """ 뉴스 기사의 정보가 있는 [path]파일을 읽음 """
    with open(path) as fin:
        return json.load(fin).get('news')


def crawler(url):
    """ 크롤링 해서 결과 return """
    pass
    return '크롤링 완료!'


def save_article_data(path, text):
    """ [text]의 내용을 [path]에 저장 """
    with open(path, 'w') as fout:
        fout.writelines(text)


def main():
    path_in_json = '/Users/ask4git/Desktop/crawling_url_list.json'
    path_out_dir = '/Users/ask4git/Desktop/crawling_result'

    # read input data
    news = read_article_data(path_in_json)

    # crawling
    for article_info in news:
        text = crawler(article_info.get('url'))
        file_name = article_info.get('filename')

        path_out = os.path.join(path_out_dir, file_name)
        # path_out = path_out_dir + '/' + file_name
        # path_out = f'{path_out_dir}/{file_name}'

        save_article_data(path_out, text)
        # save_article_data(path_out, crawler(article_info.get('url')))


if __name__ == '__main__':
    main()


# import json
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import requests
#
# path = r'C:\Users\cubana\python101\COVID-19\news\news.json'
#
# def open_json_file(path):
#     with open(path) as json_file:
#         json_data = json.load(json_file)
#     return json_data
#
# def url_list():
#     b = []
#     for a in open_json_file(path)["news"]:
#         b.append(a["url"])
#     return b
#
#
# base_url = 'https://www.fda.gov/news-events/press-announcements/coronavirus-covid-19-update-daily-roundup-september-3-2020'
# con = requests.get(base_url)
# soup = BeautifulSoup(con.content, 'lxml')
# for
# print(soup)