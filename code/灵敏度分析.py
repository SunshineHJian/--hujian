# import first_1 as fir


import pymysql
conn = pymysql.connect("localhost", "root", "hj123456", "mcm", 3306, charset="utf8mb4")
cursor = conn.cursor()
# where product_parent=423421857
# sql = "select DATEdiff(review_date,'2004-6-19'),avg(scores) from hair Where product_id = 'B003V264WW'  group by DATEdiff(review_date,'2004-6-19') order by review_date ASC"
table = 'microwave'
# table = 'hair'
# table = 'pacifier'

# Where product_parent = "%s" \
sql = 'Select sum(helpful_votes)/count(star_rating),star_rating \
        From microwave   \
        Group by star_rating  \
        Order by star_rating ASC'
# sql = 'Select year(review_date),month(review_date),avg(scores2),avg(scores) \
#         From %s  \
#         Group by year(review_date),month(review_date)  \
#         Order by year(review_date) ASC,month(review_date) ASC' % (table)
# sql = 'Select datediff(review_date, "2002-01-01"),avg(scores2),avg(scores3) \
#         From %s  \
#         Group by datediff(review_date, "2002-01-01")  \
#         Order by datediff(review_date, "2002-01-01") ASC' % (table)

# sql =   'Select datediff(review_date, "2002-01-01"),sum(scores) \
#         From %s  \
#         Where product_id = "%s" \
#         Group by datediff(review_date,"2002-01-01")  \
#         Order by datediff(review_date, "2002-01-01") ASC' % (table, id)
cursor.execute(sql)
conn.commit()
res = cursor.fetchall()
for iter in res:
    print(iter[1],iter[0])



cursor.close()
conn.close()
# import matplotlib.pyplot as plt
# star = []
# scores = []
# x = []
# for item in res:
#     year = item[0] - 2002
#     month = item[1]
#     x.append(year*12+month)
#     star.append(item[2])
#     scores.append(item[3])
#
#     # x.append(item[0])
#     # star.append(item[1])
#     # scores.append(item[2])
#
#
# plt.plot(x, star, color="k", linestyle="-", marker=".", linewidth=1.0, label='No_vine')
# plt.plot(x, scores, color="r", linestyle="-", marker=".", linewidth=1.0, label='having_vine')
#
# plt.xlabel('time/month')
# plt.ylabel('scores')
# plt.legend(loc=2)  # 指定legend的位置右下角
# # plt.title(table + id)
# plt.title(table)
# plt.savefig( table + '_vine' +'.png')
# plt.show()