# -*- coding: utf-8 -*-
import pymysql


def init_conn():
    conn = pymysql.connect(
        host="127.0.0.1",  # 数据库的IP地址
        user="root",  # 数据库用户名称
        password="root",  # 数据库用户密码
        db="db_study",  # 数据库名称
        port=3306,  # 数据库端口名称
        charset="utf8"  # 数据库的编码方式
    )
    return conn


def execute_with_bool(sql_str, args=()):
    conn = init_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_str, args)
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(e)
        return False
    finally:
        cursor.close()


def execute_with_tuple(sql_str, args=()):
    conn = init_conn()
    cursor = conn.cursor()
    results = []
    try:
        cursor.execute(sql_str,args)
        results = cursor.fetchall()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cursor.close()
    return results


def insert_data(city_id, city_name, week, data, day_weather, day_windDirect, day_windScale, night_weather,
                night_windDirect, night_windScale, max_temperature, min_temperature):
    return execute_with_bool(
        "insert into weather(city_id,city_name,week,data,day_weather,day_windDirect,day_windScale,night_weather,"
        "night_windDirect,night_windScale,max_temperature,min_temperature) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (city_id, city_name, week, data, day_weather, day_windDirect, day_windScale, night_weather, night_windDirect,
         night_windScale, max_temperature, min_temperature))


def delete_all_msg():
    return execute_with_bool("delete from weather")


def search_all_msg():
    return execute_with_tuple("select * from weather")


def search_by_id(city_id, week):
    return execute_with_tuple("select * from weather where city_id = %s and week = %s", (city_id, week))