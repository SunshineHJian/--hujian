# -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
#
# name_list = ['one_star', 'two_star', 'three_star', 'four_star', 'five_star']
# num_list = [2.1233, 1.6487, 0.8612, 0.9948, 0.6040]
# num_list1 = [4.5746, 2.0986, 2.2713, 1.9318,1.8816]
# num_list2 = [5.6169, 3.6339, 6.5373, 4.2767,6.3793]
#
# x = list(range(len(num_list)))
# total_width, n = 0.8, 3
# width = total_width / n
#
# plt.bar(x, num_list, width=width, label='pacifier', fc='r')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list1, width=width, label='hair_dryer', tick_label=name_list, fc='y')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list2, width=width, label='microwave', tick_label=name_list, fc='c')
# plt.legend()
# plt.ylabel('help_vote_frequency')
#
# # plt.grid()
# plt.savefig('help_vote.jpg')
# plt.show()

import random
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties

# font = FontProperties(fname='/Library/Fonts/Songti.ttc')


def draw():
    # 定义热图的横纵坐标
    xLabel = ['one_star', 'two_star', 'three_star', 'four_star', 'five_star']
    yLabel = ['pacifier', 'hair_dryer', 'microwave']

    # 准备数据阶段，利用random生成二维数据（5*5）
    data = [
    [2.1233, 1.6487, 0.8612, 0.9948, 0.6040],
    [4.5746, 2.0986, 2.2713, 1.9318,1.8816],
    [5.6169, 3.6339, 6.5373, 4.2767,6.3793]]


    # 作图阶段
    fig = plt.figure()
    # 定义画布为1*1个划分，并在第1个位置上进行作图
    ax = fig.add_subplot(111)
    # 定义横纵坐标的刻度
    ax.set_yticks(range(len(yLabel)))
    ax.set_yticklabels(yLabel)
    ax.set_xticks(range(len(xLabel)))
    ax.set_xticklabels(xLabel)
    # 作图并选择热图的颜色填充风格，这里选择hot
    im = ax.imshow(data, cmap=plt.cm.hot_r)
    # 增加右侧的颜色刻度条
    plt.colorbar(im)
    # 增加标题
    plt.title("help_vote frequency")
    plt.savefig('hotimg.png')
    # show
    plt.show()


d = draw()