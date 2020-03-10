import numpy as np
import pandas as pd
cnt = dict()
cnt2 = dict()

def process_data(file_name):
    df = pd.read_csv(file_name,sep='\t',header=0, encoding='utf-8')
    # mp = map()
    # i = 0
    # for item in df.head():
    #     mp[item] = i
    #     i += 1
    for item in df.values:
        if(item[1] not in cnt.keys()):
            cnt[item[1]] = 1
        else:
            cnt[item[1]] += 1

    i = 0
    for item in cnt:
        if cnt[item] > 1:
            print(item, cnt[item])
            i += 1
    data = np.zeros((i, 2), dtype=int)
    i = 0
    for item in cnt:
        if cnt[item] > 1:
            data[i][0] = item
            data[i][1] = str(cnt[item])
            i += 1
    np.savetxt(file_name + "count.csv", data, delimiter=',') #计算次数

def process_data2(file_name):
    df = pd.read_csv(file_name, sep='\t', header=0, encoding='utf-8')
    for item in df.values:
        if item[1] not in cnt2.keys():
            cnt2[item[1]] = []
            cnt2[item[1]].append(item[3])
        else:
            cnt2[item[1]].append(item[3])


if __name__=='__main__':
    # process_data('data/microwave.tsv')
    # process_data('data/hair_dryer.tsv')
    # process_data('data/pacifier.tsv')
    process_data2('data/microwave.tsv')
    process_data2('data/hair_dryer.tsv')
    process_data2('data/pacifier.tsv')
    with open("data/num.csv", "w+") as f:
        for item in cnt2:
            if len(cnt2[item]) > 1:
                print(item, cnt2[item])
                f.write(str(item))
                f.write(str(cnt2[item]))
                f.write('\n')
# main('mcm','microwave','data/microwave.tsv')
# main('mcm','hair','data/hair.dryer.tsv')
# main('mcm', 'parcifier', 'data/pacifier.tsv')