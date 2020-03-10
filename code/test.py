import pandas as pd
import numpy as np
import pymysql
conn = pymysql.connect("localhost", "root", "hj123456", "mcm",3306,charset="utf8mb4")
    # 创建游标对象
cursor = conn.cursor()
# sql = "select product_id, count(product_id) from pacifier group by product_id order by count(product_id) DESC"
# sql = "select product_title, count(product_title) from pacifier group by product_title order by count(product_title) DESC"
sql = "select product_parent, count(product_parent) from hair group by product_parent order by count(product_parent) DESC"

# sql = 'select star_rating, count(star_rating) from microwave where verified_purchase="Y" group by star_rating'

cursor.execute(sql)
res = cursor.fetchall()

# for i in range(2003,2016):
#     sql = "select count(star_rating) from pacifier where star_rating = 1 and review_date like '%" + str(i) + "'"
#     cursor.execute(sql)
#     c = cursor.fetchone()
#
#     print(c)
#     res.append(c)
# print(res)





# 得到各种产品的数量
# with open("data/hair_product.csv","w+") as f:
# with open("data/pacifier_product3.csv", "w+", encoding='utf-8') as f:
with open("data/hair_product_parent.csv","w+") as f:
    for item in res:
        print(item)
        f.write(str(item))
        f.write('\n')




print('--------------------')
# df = pd.read_csv('data/microwave.tsv', sep='\t', header=0)
# for item in df.head():
#     print(item)

# sum = [0, 0, 0, 0, 0]
# cnt = [0, 0, 0, 0, 0]
# ave = [0, 0, 0, 0, 0]

# sum = np.zeros((5,1))
# cnt = np.zeros((5,1))
# ave = np.zeros((5,1), dtype=float)
#
#
# for item in df.values:
#     cnt[item[7]-1] += 1
#     sum[item[7]-1] += item[9]
#
# for i in range(5):
#     ave[i] = sum[i] / cnt[i]
#     print(ave[i], sum[i], cnt[i])