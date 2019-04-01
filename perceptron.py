#感知机学习算法的原始形式
"""
三个点
正实例点为：x1=(3,3),x2=(4,3)
负实例点为：x3=(1,1)
感知机模型为：f(x) = sign(w*x+b)
其中w=(w1,w2),*表示点乘
"""

import numpy as np
x = np.array([[3,3],[4,3],[1,1]])
y = np.array([[1],[1],[-1]])
w = np.zeros([1,2])
b = 0

#l1和l2分别表示用随机梯度下降法学习时的点的顺序
l1 = [0,2,2,2,0,2,2]
l2 = [0,2,2,2,1,2,2,2,0,2,2]

cnt = 0
for i in l1:
    if ((np.dot(w,x[i].T) + b) * y[i][0] <= 0):
        w = w + y[i][0] * x[i]
        b = b + y[i][0]
    cnt = cnt + 1;
    print("迭代次数：", cnt, end = "   ")
    print("误分类点：x", i+1, end = "   ")
    print("w:", w, end = "   ")
    print("b:", b)
print()

cnt = 0
w = np.zeros([1,2])
b = 0
for i in l2:
    if ((np.dot(w,x[i].T) + b) * y[i][0] <= 0):
        w = w + y[i][0] * x[i]
        b = b + y[i][0]
    cnt = cnt + 1;
    print("迭代次数：", cnt, end = "   ")
    print("误分类点：x", i+1, end = "   ")
    print("w:", w, end = "   ")
    print("b:", b)