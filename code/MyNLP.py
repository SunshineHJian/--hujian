import pandas as pd
import re #清楚数字标点的标准库
import nltk #下载含有所有虚词的list
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

dataset = pd.read_csv('data/microwave.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')
# dataset = pd.read_csv('data/pacifier.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')
# nltk.download('stopwords') #list名字：stopwords 下载
from nltk.corpus import stopwords #下载之后 载入字典
from nltk.stem.porter import PorterStemmer #stem：词根 PorterStemmer： 词根函数库
corpus = [] #空list
len = len(dataset)

listc = []
k = 0
for i in range(0, len):
    try:
        review = re.sub('[^a-zA-Z]', ' ', dataset['review_body'][i])  # 去除标点，数字，去除之后用空格代替，只留下大小写字母
        review = review.lower()  # 全部转换成小写
        review = review.split()  # 将句子字符串，转换成含有不同单词的list
        ps = PorterStemmer()  # 取词根化的方程
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  # 用词根化后的结果进行循环
        # set让速度变得更快。 最后查看是否在英文的虚词字典里 ‘english’
        # 代码运行到这里 举栗子： 原来第一行review便转化成了 ['wow','love','place']
        review = ' '.join(review)  # 在每两个单词之间加上空格，并重现转化成字符串
        corpus.append(review)  # 每处理一行，变加入list
        listc.append(dataset.iloc[i, 7])
    except Exception as e:
        k += 1
        print(e)
        continue
    else:
        if(i % 500 == 0):
            print(i)

# with open("review_pa.txt", 'w+',encoding='utf-8') as f:
#     for i in range(0, len):
#         try:
#             review = re.sub('[^a-zA-Z]', ' ', dataset['review_body'][i])  # 去除标点，数字，去除之后用空格代替，只留下大小写字母
#             review = review.lower()  # 全部转换成小写
#             review = review.split()  # 将句子字符串，转换成含有不同单词的list
#             ps = PorterStemmer()  # 取词根化的方程
#             review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  # 用词根化后的结果进行循环
#             # set让速度变得更快。 最后查看是否在英文的虚词字典里 ‘english’
#             # 代码运行到这里 举栗子： 原来第一行review便转化成了 ['wow','love','place']
#             review = ' '.join(review)  # 在每两个单词之间加上空格，并重现转化成字符串
#             corpus.append(review)  # 每处理一行，变加入list
#             f.write(str(i + 1) + ",")
#             f.write(str(review) + '\n')
#             listc.append(dataset.iloc[i, 7].values)
#         except Exception as e:
#             len -= 1
#             continue
#         else:
#             print(i)
print(listc)
print(k)
len -= k
vector = 1500
cv= CountVectorizer(max_features = vector) #转化矩阵函数，只需要加一个参数 最大的列的数
X = cv.fit_transform(corpus).toarray() #生成了稀疏矩阵
y = dataset.iloc[:, 7].values
i = 0
for item in listc:
    if item >= 3:
        y[i] = 1
    else:
        y[i] = 0
    i += 1


# 开始训练
clf = GaussianNB()  # 高斯朴素贝叶斯
clf2 = BernoulliNB()  # 贝努利
clf3 = MultinomialNB()  # 多项式

acc = 0
acc2 = 0
acc3 = 0
max_len = len

print("-------开始训练-------")
clf.fit(X[:int(0.8*max_len),:], y[:int(0.8*max_len)])
clf2.fit(X[:int(0.8*max_len),:], y[:int(0.8*max_len)])
clf3.fit(X[:int(0.8*max_len),:], y[:int(0.8*max_len)])

for i in range(int(0.8*max_len),max_len):
    pre = clf.predict(X[i, :].reshape(1, vector))
    print(pre,y[i])
    if (pre == y[i]):
        acc += 1
    pre = clf2.predict(X[i, :].reshape(1, vector))
    if (pre == y[i]):
        acc2 += 1
    pre = clf3.predict(X[i, :].reshape(1, vector))
    if (pre == y[i]):
        acc3 += 1

acc = acc / (0.2*max_len)
print('Gauss acc :{0}'.format(acc))
acc2 = acc2 / (0.2*max_len)
print('Bernou acc :{0}'.format(acc2))
acc3 = acc3 / (0.2*max_len)
print('Multi acc :{0}'.format(acc3))
