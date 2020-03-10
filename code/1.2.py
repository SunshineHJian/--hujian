import first_1 as fir
import numpy as np
import re
scores,dataset,table = fir.get_scores()
lens = len(dataset)
final_scores = []

for i in range(0, lens):
    try:
        star = dataset['star_rating'][i]
        SYN = dataset['vine'][i]
        if SYN == 'Y':
            if (star == 5):
                SYN = 20
            elif (star == 4):
                SYN = 10
            elif (star == 3):
                SYN = 0
            elif (star == 2):
                SYN = -10
            elif (star == 1):
                SYN = -20
        else:
            SYN = 0
        # help = dataset['helpful_votes'][i]
        final_scores.append((star * 0.1 + (scores[i][0] + 1) * 0.15 * scores[i][1] ) * 100 +SYN)
        # final_scores.append(((star * 0.1 + (scores[i][0] + 1) * scores[i][1] * 25)*100 + help + SYN*10))
        # final_scores.append(((star*0.1 + (scores[i][0]+1)*scores[i][1]*0.125)*100 + 2*help)*SYN)
    except Exception as e:
        final_scores.append(50)
        print(e)
        print(i)

# print(final_scores)
# with open("data/评论最终得分%s.csv" % table, "w+") as f:
#     for item in final_scores:
#         # print(item)
#         f.write(str(item) + '\n')


import pymysql

def getcon(db_names):
    conn = pymysql.connect("localhost", "root", "hj123456", db_names,3306,charset="utf8mb4")
    cursor1=conn.cursor()
    return conn,cursor1

def insertData(db_name,table_name):
    conn, cursor1 = getcon(db_name)
    # sql = 'insert into '+table_name +' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sql = 'update '+table_name +' set scores3 = %s where id = %s'
    print(sql)
    lists = []
    for i in range(0,lens):
        temp = []
        temp.append(str(final_scores[i]))
        # if final_scores[i] == 0:
        #     print('等于0了')
        temp.append(str(i))
        # print(temp)
        lists.append(tuple(temp))
        if i % 1000 == 0:
            try:
                cursor1.executemany(sql, lists)
            # 提交sql语句执行操作
                conn.commit()
                print('成功添加了' + str(i) + '条数据 ')
                lists = []
            except Exception as e :
                print(e)
                conn.rollback()
                print("rollback")
            else:
                lists = []
    cursor1.executemany(sql, lists)
    # 提交sql语句执行操作
    conn.commit()
    print('成功添加了' + str(i) + '条数据 ')

    # 没提交一次就计数一次
    return conn,cursor1
# 主函数
def main(db_name,table_name):
    conn, cursor1 =insertData(db_name,table_name)
    # 当添加完成之后需要关闭我们的游标，以及与mysql的连接
    cursor1.close()
    conn.close()
# 判断一下，防止再次在其他文件调用当前函数的时候会使用错误，多次调用

main('mcm',table)
# main('mcm','hair')
# main('mcm','pacifier')





