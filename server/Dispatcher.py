# -*- coding: utf-8 -*-
import os

from Crawler import webResolver
from Saver import dataBaseSaver
from Constant import CityCode, BaseURL
from Exporter import dataBaseGetter, excelExporter


def dataSaver():
    # 爬取网页
    all_city_list = webResolver(BaseURL, CityCode)
    # 保存到数据库中
    dataBaseSaver(all_city_list)


def dataExporter(file_path, file_name):
    # 获取数据库数据
    all_city_list = dataBaseGetter()
    # 导出到Excel文件中
    excelExporter(all_city_list, os.path.join(file_path, file_name))
