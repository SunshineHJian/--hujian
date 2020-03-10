import pymysql
conn = pymysql.connect("localhost", "root", "hj123456", "mcm",3306,charset="utf8mb4")

cursor = conn.cursor()
table = "microwave"
id = '423421857'

# sql =   'Select year(review_date),quarter(review_date),avg(star_rating),count(star_rating),avg(scores)  \
#         From %s  \
#         Where verified_purchase="Y" and product_parent = "%s" \
#         Group by year(review_date),month(review_date)  \
#         Order by year(review_date) ASC,quarter(review_date) ASC' %(table, id)
sql = 'Select a.customer_id, a.star_rating, b.star_rating, a.helpful_votes,b.helpful_votes,a.vine  \
      From hair as a inner join pacifier as b\
      on a.customer_id = b.customer_id '

cursor.execute(sql)
res = cursor.fetchall()
i = 0
for item in res:
    print(item)
    i += 1
print(i)

cursor.close()
conn.close()