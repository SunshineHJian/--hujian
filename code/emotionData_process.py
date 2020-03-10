import re
import numpy
import nltk.stem
from nltk.corpus import stopwords
# nltk.download('stopwords')

def get_Words():
    # M = dict()
    WORDS = dict()

    Two_Word = dict()
    Possibly = dict ()
    str = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@￥%……&*（）]+"
    # str = "[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~#￥%……&*（）]+"

    with open('train_txt2.csv', 'r') as f:
        txt = f.read ().splitlines ()
        for line in txt:
            temp = line.split(',')
            words = temp[2].split(' ')
            # M[temp[1]] = re.sub(str, "", words)
            i = 0
            first = re.sub(str, "", words[0])

            # 前一个单词
            for word in words:
                word = re.sub (str, "", word)
                s = nltk.stem.SnowballStemmer('english')
                word = s.stem(word)
                if word not in WORDS.keys ():
                    WORDS[word] = 1

                else:
                    WORDS[word] += 1
                if (i == 0):
                    i += 1
                    continue
        WORDS = dict(sorted (WORDS.items (), key=lambda d: d[1], reverse=True))
        i = 0
        exc = {' '}
        for item in WORDS.items():
            print(item)
            i += 1
            if(i > 200):
                break

    return WORDS




