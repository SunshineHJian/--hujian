import pymysql
import numpy as np


def get_X_Y():
    conn = pymysql.connect("localhost", "root", "hj123456", "mcm", 3306, charset="utf8mb4")
    cursor = conn.cursor()
    # where product_parent=423421857
    # sql = "select DATEdiff(review_date,'2004-6-19'),avg(scores) from hair Where product_id = 'B003V264WW'  group by DATEdiff(review_date,'2004-6-19') order by review_date ASC"
    # table = 'microwave'
    # table = 'hair'
    table = 'pacifier'
    id = 'B003CK3LDI'
    # Where product_parent = "%s" \
    sql = 'Select year(review_date),month(review_date),sum(scores) \
            From %s  \
            Where product_id = "%s" \
            Group by year(review_date),month(review_date)  \
            Order by year(review_date) ASC,month(review_date) ASC' % (table, id)
    # sql =   'Select datediff(review_date, "2002-01-01"),sum(scores) \
    #         From %s  \
    #         Where product_id = "%s" \
    #         Group by datediff(review_date,"2002-01-01")  \
    #         Order by datediff(review_date, "2002-01-01") ASC' % (table, id)
    cursor.execute(sql)
    res = cursor.fetchall()

    lens = len(res)
    X_train = np.zeros((lens, 1), dtype=int)
    y_train = np.zeros((lens, 1), dtype=float)
    for i in range(lens):
        print(res[i])
        # temp = str(res[i][0]).split('-')
        # X_train[i][0] = int(temp[0])
        # X_train[i][1] = int(temp[1])
        # X_train[i][1] = int(temp[2])
        X_train[i] = (res[i][0] - 2000) * 12 + res[i][1]
        y_train[i] = res[i][2]
        # X_train[i] = res[i][0]
        # y_train[i] = res[i][1]

    cursor.close()
    conn.close()
    return X_train,y_train, table, id



from sklearn.model_selection import train_test_split


# 加载数据集

#
# # XGBoost训练过程
# c = 0.8
# X_train, X_test, y_train, y_test =  X_train[:int(c*lens)],  X_train[int(c*lens)+1:], y_train[:int(c*lens)],  y_train[int(c*lens)+1:]
#
#
#
#
# import sklearn
# from sklearn import linear_model
# #训练模型
# lm=linear_model.LinearRegression()
# #用fit进行回归
# model=lm.fit(X_train,y_train)
#
# pre = model.predict(X_test)
#
#
# print(pre)
#
# import matplotlib.pyplot as plt
#
#
# # plot函数作图
# plt.plot(X_train, y_train, color="r", linestyle="--", marker="*", linewidth=0.5)
# plt.plot(X_test, y_test, color="r", linestyle="--", marker="*", linewidth=0.5)
# plt.plot(X_test, pre, color="b", linestyle="--", marker="*", linewidth=0.5)
# # plt.axis([1400, 1600,0,100])
# # show函数展示出这个图，如果没有这行代码，则程序完成绘图，但看不到
# plt.show()

# import seaborn
#
# #通过画图可以直观地对数据的线性关系做一个观察
# seaborn.regplot(x='PetalLengthCm',y='PetalWidthCm',data=[X_test,y_test])

# x = X_train[:,0]
#
# y = y_train[:,0]
#
# # 用3次多项式拟合
# f1 = np.polyfit(x, y, 3)
# p1 = np.poly1d(f1)
# print(p1)
#
# # 也可使用yvals=np.polyval(f1, x)
# yvals = p1(x)  # 拟合y值
#
# # 绘图
# plot1 = plt.plot(x, y, 's', label='original values')
# plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=4)  # 指定legend的位置右下角
# plt.title('polyfitting')
# plt.show()
# # plt.savefig('test.png')
#
# # encoding=utf-8
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
#
#
# # 自定义函数 e指数形式
# def func(x, a, b):
#     return a * np.exp(b / x)
#
#
# # 定义x、y散点坐标
#
# # 非线性最小二乘法拟合
# popt, pcov = curve_fit(func, x, y)
# # 获取popt里面是拟合系数
# a = popt[0]
# b = popt[1]
# yvals = func(x, a, b)  # 拟合y值
#
# print(u'系数a:', a)
# print(u'系数b:', b)
#
# # 绘图
# plot1 = plt.plot(x, y, 's', label='original values')
# plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=4)  # 指定legend的位置右下角
# plt.title('curve_fit')
# plt.show()
# plt.savefig('test2.png')


