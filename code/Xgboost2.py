#标准的库导入
import pandas as pd
import numpy as np
from datetime import datetime
import re
import matplotlib.pylab as plt
from math import sqrt
import os

from matplotlib.pyplot import rcParams
rcParams['figure.figsize']=15,6

# 预处理和划分数据
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# 导入模型
import xgboost as xgb

#模型调参的工具
from sklearn.model_selection import cross_val_score,KFold
from sklearn.model_selection import GridSearchCV

#模型保存工具
from sklearn.externals import joblib

#Error metrics
from sklearn.metrics import mean_squared_error, r2_score

# import the data
# dataparse = lambda dates: datetime.strptime(dates, '%Y-%m-%d')
# data = pd.read_excel('xxxx/acitivedata.xlsx', pares_dates=['Day'], index_col='Day', date_parser=dataparse)
#
# # get seperate date
# ts1 = data['login']
# ts2 = data['delivery']
# ts3 = data['registration']
#
# # 数据的异常点处理
# ts3['2016-09-23'] = ts3['2016-09-22']
#
# ts2['2016-09-24'] = ts2['2016-09-17']
# ts2['2016-09-25'] = ts2['2016-09-18']
#
# ts1['2016-09-24'] = ts1['2016-09-17']
# ts1['2016-09-25'] = ts1['2016-09-18']
#
# # 将数据进行监督序列的转化
# X = ts1.as_matrix()
# # 将序列转化为监督序列
# lag = 7
#
# X_matrix = []
# y = []
# for i in range(len(X) - lag):
#     sample = []
#     for n in range(lag):
#         sample.append(X[i + n])
#
#     X_matrix.append(sample)
#     y.append(X[i + lag])
#
# # 这是最后7个点数据，来预测新的一天
# X_test_predict = []
# for i in range(lag):
#     X_test_predict.append(X[-(lag - i)])
#
# X_matrix.append(X_test_predict)
#
# XX = np.array(X_matrix)
# y = np.array(y)

import pymysql
conn = pymysql.connect("localhost", "root", "hj123456", "mcm",3306,charset="utf8mb4")
    # 创建游标对象
cursor = conn.cursor()
# sql = "select product_id, count(product_id) from pacifier group by product_id order by count(product_id) DESC"
# sql = "select product_title, count(product_title) from pacifier group by product_title order by count(product_title) DESC"
sql = "select DATEdiff(review_date,'2004-6-19') from microwave where product_parent = '423421857' group by DATEdiff(review_date,'2004-6-19') order by DATEdiff(review_date,'2004-6-19') ASC"

# sql = 'select star_rating, count(star_rating) from microwave where verified_purchase="Y" group by star_rating'

cursor.execute(sql)
res = cursor.fetchall()


lens = len(res)
X_train = np.zeros((lens,1),dtype=float)
y_train = np.zeros((lens,1),dtype=float)
for i in range(lens):
    print(res[i][0])
    X_train[i] = res[i][0] - 2558




# 定义训练数据


sql = "select avg(scores) from microwave where product_parent = '423421857' group by DATEdiff(review_date,'2004-6-19') order by DATEdiff(review_date,'2004-6-19') ASC"

cursor.execute(sql)
res = cursor.fetchall()

for i in range(lens):
    print(res[i][0])
    y_train[i] = res[i][0]



cursor.close()
conn.close()




# setup regressor
xgb_model = xgb.XGBRegressor()
# performance a grid search
tweaked_model = GridSearchCV(
    xgb_model,
    {
        'max_depth':[1,2,5,10,20],
        'n_estimators':[20,30,50,70,100],
        'learning_rate':[0.1,0.2,0.3,0.4,0.5]
    },
    cv = 3,
    verbose = 1,
    n_jobs = -1,
    scoring = 'neg_median_absolute_error',
)

tweaked_model.fit(X_train,y_train)
print('Best: %f using %s'%(tweaked_model.best_score_, tweaked_model.best_params_))


#saving and load models
def save_model(model,filename):
    return joblib.dump(model,filename)

def load_model(filename):
    return joblib.load(filename)

#四、预测新数据
save_model(tweaked_model,'XGB-model_lag=7.pkl')
model = load_model('XGB-model_lag=7.pkl')

model1 = xgb.XGBRegressor(learning_rate= 0.1, max_depth= 5, n_estimators= 100)

X_predict_test = np.zeros((365,1),dtype=float)
y_predict = np.zeros((365,1),dtype=float)

for i in range(365):
    X_predict_test = X_train[lens-1] + i

# model1.fit(X_predict,y_predict)
#
#以最后100天的数据为测试数据
X_predict = model1.predict(X_predict_test)

# plt.plot(y_train[-100:],color='blue',label='actul')
plt.plot(X_predict,color='red',label='predict')
# plt.legend(loc='best')
# plt.title('RMSE:%.4f'%np.sqrt((sum((X_predict[:-1]-y_train[-100:])**2))/len(X_predict)))
# plt.show()
# print("the next day predict is %.f"%X_predict[-1])

# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt

