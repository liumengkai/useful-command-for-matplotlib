import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,50)     #这段话表示将0~2*pi分成五十个小段
plt.plot(x,np.sin(x))   #如果没有第一个参数x，图形的x坐标默认为数组的索引
plt.show() #显示图形
x=np.linspace(0,4*np.pi,100)
plt.plot(x,np.sin(x),x,np.sin(2*x))         #同时在图像上画出两个
plt.show()
#自定义图像的外观
#基本图像外观定义如下 蓝色 - 'b' 绿色 - 'g' 红色 - 'r' 青色 - 'c' 品红 - 'm' 黄色 - 'y' 黑色 - 'k'
#白色 - 'w' 线： 直线 - '-' 虚线 - '--' 点线 - ':' 点划线 - '-.' 常用点标记 点 - '.' 像素 - ',' 圆 - 'o' 方形 - 's' 三角形 - '^'
x=np.linspace(0,2*np.pi,50)
plt.plot(x,np.sin(x),'r-o',x,np.cos(x),'g--')
plt.show()
#使用子图可以在一个窗口绘制多张图，subplot()函数表示
x=np.linspace(0,2*np.pi,50)
plt.subplot(2,1,1)             #subplot()函数  （行，列，活动区域）
plt.plot(x,np.sin(x),'-o')     #这里切记不能进行绘制图像的操作plt.show()，最后再进行绘制图像，否则会分别将两张图出现在不同的figure中
plt.subplot(2,1,2)
plt.plot(x,np.cos(x),'-o')
plt.show()
#绘制散点图

x=np.linspace(0,2*np.pi,50)
plt.scatter(x,np.sin(x))
plt.show()