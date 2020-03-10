import pymysql
import numpy as np
import matplotlib.pyplot as plt

conn = pymysql.connect("localhost", "root", "hj123456", "mcm", 3306, charset="utf8mb4")
cursor = conn.cursor()

# table = 'microwave'
table = 'hair'
# table = 'pacifier'
stars = 1
# Where product_parent = "%s" \
sql = 'Select year(review_date),quarter(review_date),avg(star_rating),avg(scores2) \
        From %s  \
        Group by year(review_date),quarter(review_date)  \
        Order by year(review_date) ASC,quarter(review_date) ASC' % (table)

cursor.execute(sql)
conn.commit()
res = cursor.fetchall()
# print(res)
cursor.close()
conn.close()


star = []
scores = []
x = []
for item in res:
    year = item[0] - 2002
    month = item[1]
    x.append(year*12+month)
    star.append(item[2]*20)
    if (item[3]-float(item[2]*12))*4.5 <= 100:
        scores.append((item[3]-float(item[2]*12))*4.5)
    else:
        scores.append(100)

plt.plot(x, star, color="r", linestyle="-", marker=".", linewidth=0.5, label='star_rating')
plt.plot(x, scores, color="g", linestyle="-", marker=".", linewidth=0.5, label='review_scores')

plt.xlabel('time/month')
plt.ylabel('scores')
plt.legend(loc=1)  # 指定legend的位置右下角
# plt.title(table + id)
plt.title(table)
plt.savefig( table + '_star_' +'.png')
plt.show()

import numpy as np
lens = len(star)
vc = np.zeros((1,lens))
vb = np.zeros((1,lens))
for i in range(lens):
    vc[0][i] = star[i]
    vb[0][i] = scores[i]
a = vc
b = vb
x = np.vstack((vc,vb))
res1 = np.cov(a, b)
# res2 = np.cov(a, b, bias=True)
# res3 = np.cov(x)
print(res1)
# print(res2)
# print(res3)
res2 = np.corrcoef(a, b)

print(res2)


# def mean(x):
#   return sum(x) / len(x)
#
# # 计算每一项数据与均值的差
# def de_mean(x):
#   x_bar = mean(x)
#   return [x_i - x_bar for x_i in x]
# # 辅助计算函数 dot product 、sum_of_squares
# def dot(v, w):
#   return sum(v_i * w_i for v_i, w_i in zip(v, w))
# def sum_of_squares(v):
#   return dot(v, v)
# # 方差
# def variance(x):
#   n = len(x)
#   deviations = de_mean(x)
#   return sum_of_squares(deviations) / (n - 1)
# # 标准差
# import math
# def standard_deviation(x):
#   return math.sqrt(variance(x))
#
# # 协方差
# def covariance(x, y):
#     n = len(x)
#     return dot(de_mean(x), de_mean(y)) / (n -1)
# # 相关系数
# def correlation(x, y):
#     stdev_x = standard_deviation(x)
#     stdev_y = standard_deviation(y)
#     if stdev_x > 0 and stdev_y > 0:
#         return covariance(x, y) / stdev_x / stdev_y
#     else:
#         return 0
#
# res1 = covariance(vc, vb)
# res2 = correlation(vc, vb)
#
# print(res1,res2)
#
# import numpy as np
# # 先构造一个矩阵
# ab = np.array([vc, vb])
# # 计算协方差矩阵
# np.cov(ab)
# res2 = np.corrcoef(ab)
#
# print(res1,res2)

# print(np.mean(np.multiply((vc-np.mean(vc)),(vb-np.mean(vb))))/(np.std(vb)*np.std(vc)))
# #corrcoef得到相关系数矩阵（向量的相似程度）
# print(np.corrcoef(vc,vb))


# plt.plot(x, scores, color="g", linestyle="--", marker="*", linewidth=0.5, label='review_scores')
# plt.xlabel('time/month')
# plt.ylabel('scores')
# plt.legend(loc=2)  # 指定legend的位置右下角
# # plt.title(table + id)
# plt.title(table)
# plt.savefig(table + 'scores_' + str(stars) +'.png')
# plt.show()