# -*- coding: utf-8 -*-
import re
import urllib.error
import urllib.request
from bs4 import BeautifulSoup

# 正则表达式预编译
find_day = re.compile(r'<div class="day-item">(.*?)<br/>(.*?)</div>')
find_weather = re.compile(r'<div class="day-item">(.*?)</div>')
find_temperature = re.compile(r'<div class="high">(.*?)</div><div class="low">(.*?)</div>')


def webDownloader(url):
    """
    爬取指定URL的HTML页面
    :param url: 统一资源定位符（UniformResourceLocator）
    :return: 爬取的HTML页面
    """
    # User - Agent 用户代理
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / "
                      "80.0.3987.122  Safari / 537.36"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError:
        print('网页爬取失败！')
    return html


def webResolver(basis_url, city_code):
    """
    爬取页面，对页面进行解析
    :param city_code: 每个城市的城市名和对应的URL后缀
    :param basis_url: 待爬取页面的基础 URL
    :return: cityDate_list 包含需要的信息
    """

    all_city_list = []
    # 1.获取页面
    for name, code in city_code.items():
        url = basis_url + str(code)
        html = webDownloader(url)
        one_city_list = []
        # 2.解析页面
        soup = BeautifulSoup(html, "html.parser")

        # I.当天天气信息
        for first_data in soup.find_all('div', class_="pull-left day actived"):
            msg = [name]
            first_data = str(first_data)
            # i.日期
            day = re.findall(find_day, first_data)[0]
            msg.append(day[0])
            msg.append(day[1])
            # ii.天气
            for _ in range(1, 7):
                weather = re.findall(find_weather, first_data)[_]
                msg.append(weather)
            # iii.温度
            temperature = re.findall(find_temperature, first_data)[0]
            msg.append(temperature[0])
            msg.append(temperature[1])
            one_city_list.append(msg)

        # II.之后天气信息
        for after_data in soup.find_all('div', class_="pull-left day"):
            msg = [name]
            after_data = str(after_data)
            # i.日期
            day = re.findall(find_day, after_data)[0]
            msg.append(day[0])
            msg.append(day[1])
            # ii.天气
            for _ in range(1, 7):
                weather = re.findall(find_weather, after_data)[_]
                msg.append(weather)
            # iii.温度
            temperature = re.findall(find_temperature, after_data)[0]
            msg.append(temperature[0])
            msg.append(temperature[1])
            one_city_list.append(msg)

        # 3.展示爬取结果
        for _ in range(len(one_city_list)):
            print(one_city_list[_])
        print('\n')
        # 4.加入到总列表中
        all_city_list.append(one_city_list)
    return all_city_list
