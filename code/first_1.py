import pandas as pd
import re #清楚数字标点的标准库
from textblob import TextBlob
import  emotion
from nltk.corpus import stopwords  # 下载之后 载入字典
from nltk.stem.porter import PorterStemmer  # stem：词根 PorterStemmer： 词根函数库


positive, negative = emotion.get_emotion()
positive = tuple(positive)
negative = tuple(negative)

table = "microwave"

# dataset = pd.read_csv('data/hair_dryer.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')
# dataset = pd.read_csv('data/pacifier.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')

dataset = pd.read_csv('data/microwave.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')

def get_scores():

    corpus = []  # 空list
    lens = len(dataset)

    listc = []
    mp = dict()
    k = 0
    sum = 0
    scorce = []
    sum_count = 0
    for i in range(0, lens):
        try:
            # if dataset['star_rating'][i] != 5:
            #     continue
            review = re.sub('[^a-zA-Z]', ' ', dataset['review_headline'][i] + dataset['review_body'][i])  # 去除标点，数字，去除之后用空格代替，只留下大小写字母
            review = review.lower()  # 全部转换成小写
            review = review.split()  # 将句子字符串，转换成含有不同单词的list
            ps = PorterStemmer()  # 取词根化的方程
            review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]  # 用词根化后的结果进行循环
            # set让速度变得更快。 最后查看是否在英文的虚词字典里 ‘english’
            # 代码运行到这里 举栗子： 原来第一行review便转化成了 ['wow','love','place']

            for item in review:
                if item not in positive and item not in negative:
                    continue
                if item not in mp:
                    mp[item] = 1
                else:
                    mp[item] += 1
            review = ' '.join(review)  # 在每两个单词之间加上空格，并重现转化成字符串

            # 情感分析
            blob = TextBlob(review)
            # ans = -1
            temp_sum = 0
            temp_c = 0
            lens2 = len(blob.sentences)
            if(len != 0):
                for item in blob.sentences:
                    # print(item.sentiment)
                    # print(item.sentiment.polarity)
                    temp_sum += item.sentiment.polarity
                    temp_c += item.sentiment.subjectivity
            if temp_sum != 0:
                temp_list = []
                temp_list.append(temp_sum / lens2)
                temp_list.append(temp_c / lens2)
                scorce.append(temp_list)
            else:
                scorce.append([-2, 0.75])
            # print(temp_sum)
            if lens2 != 0:
                sum += temp_sum / lens2

            corpus.append(review)  # 每处理一行，变加入list
            listc.append(dataset.iloc[i, 7])
        except Exception as e:
            k += 1
            scorce.append([-2, 0.75])
            print(e)
            continue
        else:
            sum_count += 1
            if (i % 500 == 0):
                print(i)


    ave = sum / lens
    print(ave, len(scorce), lens)

    with open("data/评论得分%s.csv" % table, "w+") as f:
        for item in scorce:
            # print(item)
            if item[0] != -2:
                f.write(str(item[0]) + ',' + str(item[1]) + '\n')
            else:
                f.write(str(ave) + ',0.75\n')
                item[0] = ave
                item[1] = 0.75

    with open("data/词频统计%s.csv" % table, "w+") as f:
    # 输出频率最高的情感单词
        mp = sorted(mp.items(), key=lambda d: d[1], reverse=True)
        for item in mp:
            print(item, end='\n')
            # print(mp[item])
            f.write(str(item)+',' +'\n')
    return scorce, dataset, table
