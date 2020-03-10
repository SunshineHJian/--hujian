import numpy as np

import pymysql
conn = pymysql.connect("localhost", "root", "hj123456", "mcm",3306,charset="utf8mb4")
cursor = conn.cursor()

# id = "B0052G14E8"
# table = "microwave"

# id = "B003CK3LDI"
# table = "pacifier"

id = "B003V264WW"
table = "hair"

sql = 'select count(vine) from microwave where vine = "Y" '
cursor.execute(sql)
res = cursor.fetchall()

print(res)

sql =   'Select year(review_date),quarter(review_date),sum(star_rating)/count(star_rating),count(star_rating)\
        From %s  \
        Where verified_purchase="Y" and product_id = "%s" \
        Group by year(review_date),month(review_date)  \
        Order by year(review_date) ASC,quarter(review_date) ASC' %(table, id)

# sql = 'select star_rating,count(star_rating)  from microwave where verified_purchase="Y" and month(review_date) '
cursor.execute(sql)
res = cursor.fetchall()
res = list(res)
cursor.close()
conn.close()
# with open(table +'-' +id + '销量' + '.csv',"w+") as f:
#     for i in res:
#         print(i)
#         f.write(str(i[0])+'-'+str(i[1])+',')
#         f.write(str(i[2]) + ',')
#         f.write(str(i[3]) + '\n')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.zeros((3, len(res)), dtype=float)
i = 0
for item in res:
    data[0][i] = item[0] + 0.25 * item[1]
    data[1][i] = item[2]
    data[2][i] = item[3]
    i += 1

sizes = len(res)
x, y, z = data[0], data[2], data[1]
ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:sizes//3], y[:sizes//3], z[:sizes//3], c='y')  # 绘制数据点
ax.scatter(x[sizes//3+1:sizes//3*2], y[sizes//3+1:sizes//3*2], z[sizes//3+1:sizes//3*2], c='r')
ax.scatter(x[sizes//3*2+1:], y[sizes//3*2+1:], z[sizes//3*2+1:], c='g')

ax.set_ylabel('sale_amount')  # 坐标轴
ax.set_zlabel('star_rating')
ax.set_xlabel('years')
plt.savefig(table +'-' +id + '销量' + '.png')
plt.show()
#



# from matplotlib import pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = Axes3D(fig)
# # X, Y, Z = data[2], data[0], data[1]
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
#
# plt.show()