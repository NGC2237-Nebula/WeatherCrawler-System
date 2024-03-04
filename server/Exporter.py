# -*- coding: utf-8 -*-
import xlwt
from SqlUtil import search_all_msg


def dataBaseGetter():
    city_msg = []
    result = search_all_msg()
    for record in result:
        city_msg.append(list(record[1:]))
    return city_msg


def excelExporter(all_city_list, file_path):
    """
    保存为本地Excel文件
    :param all_city_list: 保存包含35个城市的城市名，每个城市7天天气
    :param file_path: 保存路径
    :return: Excel文件
    """
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('最近7天天气预报', cell_overwrite_ok=True)

    # 写入标题
    title = ("城市", "星期", "日期", "白天天气", "白天风向", "白天风级", "夜间天气", "夜间风向", "夜间风级", "最高气温",
             "最低气温")
    for i in range(0, 11):
        sheet.write(0, i, title[i])

    line = 1
    for record in all_city_list:
        for column in range(0, 11):
            sheet.write(line, column, record[column])
        line = line + 1

    try:
        book.save(file_path)
        print("文件保存成功!")
    except:
        print("抱歉，文件路径不存在")
