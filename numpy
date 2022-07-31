import numpy as np
import matplotlib.pyplot as plt


x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])


A = np.array([[1,2], [3,4]])  #2차원 배열
B = np.array([[3,0],[0,6]])

A.shape #행렬의 크기 2*2 임을 알수있다

# 브로드캐스트란? 형상이 다른 배열끼리도 계산이 가능한것
A = np.array([[1,2], [3,4]])
B = np.array([3,0])

#원소접근법
A[0][1]

#1차원배열로 평탄화시킴
C = A.flatten()
#특정조건만추출
C>2

x = np.arange(0, 6, 0.1)
y = np.sin(x)

print(plt.plot(x,y))
print(plt.show())
