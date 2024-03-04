# -*- coding: utf-8 -*-
from Constant import CityCode
from SqlUtil import delete_all_msg, insert_data


def dataBaseSaver(all_city_list):
    """
    保存到mysql数据库
    :param all_city_list: 保存包含35个城市的城市名，每个城市7天天气，共35*7条记录
    """
    try:
        delete_all_msg()
        for i in range(0, len(all_city_list)):
            for week in range(0, 7):
                pass
                insert_data(CityCode[all_city_list[i][week][0]], all_city_list[i][week][0],
                            all_city_list[i][week][1], all_city_list[i][week][2],
                            all_city_list[i][week][3], all_city_list[i][week][4],
                            all_city_list[i][week][5], all_city_list[i][week][6],
                            all_city_list[i][week][7], all_city_list[i][week][8],
                            all_city_list[i][week][9], all_city_list[i][week][10])
        print("数据库录入成功!")
    except:
        print("数据库录入失败!")
