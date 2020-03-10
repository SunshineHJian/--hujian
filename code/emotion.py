import re
def get_emotion():
    nagative = list()
    positive = list()
    with open("emotion/负面评价词语（英文）.txt","r+") as f:
        data = f.read().splitlines()
        i = 0
        print(data)
        for items in data:
            i += 1
            if i <= 2:
                continue
            items = items.split(' ')
            for item in items:
                if item == '':
                    continue
                nagative.append(item)

    with open("emotion/负面情感词语（英文）.txt","r+") as f:
        data = f.read().splitlines()
        i = 0
        print(data)
        for items in data:
            i += 1
            if i <= 2:
                continue
            items = items.split(' ')
            for item in items:
                if item == '':
                    continue
                nagative.append(item)


    # 正面情感词
    with open("emotion/正面评价词语（英文）.txt", "r+") as f:
        data = f.read().splitlines()
        i = 0
        print(data)
        for items in data:
            i += 1
            if i <= 2:
                continue
            items = items.split(' ')
            for item in items:
                if item == '':
                    continue
                positive.append(item)

    with open("emotion/正面情感词语（英文）.txt", "r+") as f:
        data = f.read().splitlines()
        i = 0
        print(data)
        for items in data:
            i += 1
            if i <= 2:
                continue
            items = items.split(' ')
            for item in items:
                if item == '':
                    continue
                positive.append(item)


    return positive, nagative
#
res, res2 = get_emotion()
print(res)
