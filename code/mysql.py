#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2018/10/20 10:32
# @Author  : deli Guo
# @Site   :
# @File   : test3.py
# @Software  : PyCharm
import pymysql
import pandas as pd

# 定义链接到mysql的函数，返回连接对象
# db_name是当前数据库的名字
def getcon(db_names):
    # host是选择连接哪的数据库localhost是本地数据库，port是端口号默认3306
    #user是使用的人的身份，root是管理员身份，passwd是密码。db是数据库的名称，charset是编码格式
    # conn=pymysql.connect(host="localhost", port=3306,user='root',passwd='hj123456',db_name=db_names,charset='utf8')
    conn = pymysql.connect("localhost", "root", "hj123456", db_names,3306,charset="utf8mb4")
    # 创建游标对象
    cursor1=conn.cursor()
    return conn,cursor1
# 定义读取文件并且导入数据库数据sql语句

def insertData(db_name,table_name,file_name):
    # 调用链接到mysql的函数，返回我们的conn和cursor1
    conn, cursor1 = getcon(db_name)
    # 使用pandas 读取csv文件
    df=pd.read_csv(file_name,sep= '\t',header=0,encoding="utf8")
    df = df.astype(object).where(pd.notnull(df), None)
    #使用for循环遍历df，是利用df.values，但是每条数据都是一个列表
    # 使用counts计数一下，方便查看一共添加了多少条数据
    counts = 0
    j = 0
    sql = 'insert into '+table_name +' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # sql = 'insert into ' + table_name + '(scores) values (%s)'
    print(sql)
    list = []
    for each in df.values:

        j += 1
        # if(j == 2):
        #     continue
        each[0] = str(each[0])
        each [2] =str(each[2])
        each[5] = str(each[5])

        sql2 = tuple(each)
        # print(sql2)
        list.append(sql2)

        counts+=1
        # 使用一个输出来提示一下当前存到第几条了
        if counts % 2000 == 0:
            # print(sql2)
            # cursor1.executemany(sql, list)
            # conn.commit()
            # print("commit")
            # print('成功添加了' + str(counts) + '条数据 ')
            # list = []
            try:
                cursor1.executemany(sql, list)
                conn.commit()

                # 提交sql语句执行操作
            except Exception as e :
                print(e)
                conn.rollback()
                print("rollback")
            else:

                print("commit")
                print('成功添加了' + str(counts) + '条数据 ')
                list = []

    cursor1.executemany(sql, list)
    # 提交sql语句执行操作
    conn.commit()
    print('成功添加了' + str(counts) + '条数据 ')

    # 没提交一次就计数一次
    return conn,cursor1
# 主函数
def main(db_name,table_name,file_name):
    conn, cursor1 =insertData(db_name,table_name,file_name)
    # 当添加完成之后需要关闭我们的游标，以及与mysql的连接
    cursor1.close()
    conn.close()
# 判断一下，防止再次在其他文件调用当前函数的时候会使用错误，多次调用
if __name__=='__main__':
    # main('mcm','microwave','data/microwave2.tsv')
    # main('mcm','hair','data/hair_dryer2.tsv')
    main('mcm','pacifier','data/pacifier2.tsv')
