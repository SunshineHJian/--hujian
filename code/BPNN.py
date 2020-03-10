#! /usr/bin/python
# -*- encoding:utf8 -*-

import numpy as np
from get_XY import get_X_Y
import matplotlib.pyplot as plt

from sklearn.preprocessing import normalize

def rand(a, b):
    return (b - a) * np.random.random() + a

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class BP:
    def __init__(self, layer, iter, max_error):
        self.input_n = layer[0]  # 输入层的节点个数 d
        self.hidden_n = layer[1]  # 隐藏层的节点个数 q
        self.output_n = layer[2]  # 输出层的节点个数 l
        self.gj = []
        self.eh = []
        self.input_weights = []   # 输入层与隐藏层的权值矩阵
        self.output_weights = []  # 隐藏层与输出层的权值矩阵
        self.iter = iter          # 最大迭代次数
        self.max_error = max_error  # 停止的误差范围

        # for i in range(self.input_n + 1):
        #     tmp = []
        #     for j in range(self.hidden_n):
        #         tmp.append(rand(-0.2, 0.2))
        #     self.input_weights.append(tmp)
        #
        # for i in range(self.hidden_n + 1):
        #     tmp = []
        #     for j in range(self.output_n):
        #         tmp.append(rand(-0.2, 0.2))
        #     self.output_weights.append(tmp)
        # self.input_weights = np.array(self.input_weights)
        # self.output_weights = np.array(self.output_weights)

        # 初始化一个(d+1) * q的矩阵，多加的1是将隐藏层的阀值加入到矩阵运算中
        self.input_weights = np.random.random((self.input_n + 1, self.hidden_n))
        # 初始话一个(q+1) * l的矩阵，多加的1是将输出层的阀值加入到矩阵中简化计算
        self.output_weights = np.random.random((self.hidden_n + 1, self.output_n))

        self.gj = np.zeros(layer[2])
        self.eh = np.zeros(layer[1])

    #  正向传播与反向传播
    def forword_backword(self, xj, y, learning_rate=0.1):
        xj = np.array(xj)
        y = np.array(y)
        input = np.ones((1, xj.shape[0] + 1))
        input[:, :-1] = xj
        x = input
        # ah = np.dot(x, self.input_weights)
        ah = x.dot(self.input_weights)
        bh = sigmoid(ah)

        input = np.ones((1, self.hidden_n + 1))
        input[:, :-1] = bh
        bh = input

        bj = np.dot(bh, self.output_weights)
        yj = sigmoid(bj)

        error = yj - y
        self.gj = error * sigmoid_derivative(yj)

        # wg = np.dot(self.output_weights, self.gj)

        wg = np.dot(self.gj, self.output_weights.T)
        wg1 = 0.0
        for i in range(len(wg[0]) - 1):
            wg1 += wg[0][i]
        self.eh = bh * (1 - bh) * wg1
        self.eh = self.eh[:, :-1]

        #  更新输出层权值w，因为权值矩阵的最后一行表示的是阀值多以循环只到倒数第二行
        for i in range(self.output_weights.shape[0] - 1):
            for j in range(self.output_weights.shape[1]):
                self.output_weights[i][j] -= learning_rate * self.gj[0][j] * bh[0][i]

        #  更新输出层阀值b，权值矩阵的最后一行表示的是阀值
        for j in range(self.output_weights.shape[1]):
            self.output_weights[-1][j] -= learning_rate * self.gj[0][j]

        #  更新输入层权值w
        for i in range(self.input_weights.shape[0] - 1):
            for j in range(self.input_weights.shape[1]):
                self.input_weights[i][j] -= learning_rate * self.eh[0][j] * xj[i]

        # 更新输入层阀值b
        for j in range(self.input_weights.shape[1]):
            self.input_weights[-1][j] -= learning_rate * self.eh[0][j]
        return error

    def fit(self, X, y):

        for i in range(self.iter):
            error = 0.0
            for j in range(len(X)):
                error += self.forword_backword(X[j], y[j])
            error = error.sum()
            if abs(error) <= self.max_error:
                break

    def predict(self, x_test):
        x_test = np.array(x_test)
        tmp = np.ones((x_test.shape[0], self.input_n + 1))
        tmp[:, :-1] = x_test
        x_test = tmp
        an = np.dot(x_test, self.input_weights)
        print(an)
        bh = sigmoid(an)
        # print(bh)
        #  多加的1用来与阀值相乘
        tmp = np.ones((bh.shape[0], bh.shape[1] + 1))
        tmp[:, : -1] = bh
        bh = tmp
        # print(bh)
        bj = np.dot(bh, self.output_weights)
        # print(bj)
        yj = sigmoid(bj)
        print(yj)
        return yj

if __name__ == '__main__':
    #  指定神经网络输入层，隐藏层，输出层的元素个数
    layer = [1, 5, 1]
    # X = [
    #         [1, 1],
    #         [2, 2],
    #         [1, 2],
    #         [1, -1],
    #         [2, 0],
    #         [2, -1]
    #     ]
    # y = [[0], [0], [0], [1], [1], [1]]

    X_train, y_train,table,id = get_X_Y()

    # y_train = normalize(y_train, axis=0, norm='max')
    c = 0.8
    lens = len(X_train)
    X_train, X_pre, y_train, y_pre = X_train[:int(c * lens)], X_train[int(c * lens)-1:], y_train[:int(c * lens)], y_train[int(c * lens)-1:]
    # print([X, y])
    # x_test = [[2, 3],
    #           [2, 2]]
    #  设置最大的迭代次数，以及最大误差值
    # bp = BP(layer, 10000, 100)
    # bp.fit(X, y)
    # maxn = X[0]
    # X_pre = np.zeros((12+len(X), 1))
    # for i in range(12+len(X)):
    #     X_pre[i] = maxn + i
    # y_pre = bp.predict(X_pre)


    # plot函数作图
    plt.plot(X_train, y_train, color="r", linestyle="-", marker=".", linewidth=1, label='original values')
    plt.plot(X_pre, y_pre, color="g", linestyle="-", marker=".", linewidth=1, label='polyfit values')

    plt.xlabel('time/month')
    plt.ylabel('scores')
    plt.legend(loc=2)  # 指定legend的位置右下角
    # plt.title(table + id)
    plt.title("polyfitting")
    plt.savefig('image/pre_'+ table + id +'.png')
    plt.show()

    #
    # plt.axis([1400, 1600,0,100])
    # show函数展示出这个图，如果没有这行代码，则程序完成绘图，但看不到
