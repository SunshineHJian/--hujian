from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import pandas as pd
data = pd.read_csv('data/microwave.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')
# data = pd.read_csv('data/pacifier.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')
# data = pd.read_csv('data/hair_dryer.tsv', delimiter = '\t', quoting = 3, encoding='utf-8')
comment = data.get('review_body')
def trans_CN(text):
    word_list = text.split(' ')
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

text = ""
for item in comment:
    text = text + str(item)

text = trans_CN(text)
# print(text)
mask = np.array(image.open("ciyun2.jpg"))
wordcloud = WordCloud(
    mask=mask,
    font_path="C:\\Windows\\Fonts\\msyh.ttc",
    background_color="white"
).generate(text)

image_produce = wordcloud.to_image()
# wordcloud.to_file("image/microwave.png")
wordcloud.to_file("image/microwave.png")
image_produce.show()


