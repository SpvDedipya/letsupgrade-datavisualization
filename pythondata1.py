import numpy as np
import pandas as pd
import seaborn as sns
from numpy.random import randn,randint,uniform,sample
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
#question 1
a=np.arange(40,50)
b=np.arange(50,60)
plt.title("Line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(a,b,"bo--",linewidth=2,markersize=10)

#question 2
days = [1,2,3,4,5,6,7] #days of d week
sales_1 = [160,150,140,145,175,165,180] #sales of company1
sales_2 = [70,90,160,150,140,145,175]  #sales of company2
plt.title("Line plot")
plt.xlabel("company 1")
plt.ylabel("company 2")
plt.plot(sales_1,sales_2,"bo--",linewidth=2,markersize=10)

#question 3
x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]
plt.subplot(3,3,1)
plt.plot(x,y1,"ro--")
plt.subplot(3,3,2)
plt.plot(x,y2,"b*--")
plt.subplot(3,3,3)
plt.plot(x,y3,"g^--")
plt.subplot(3,3,4)
plt.plot(x,y4,"g*--")
plt.subplot(3,3,5)
plt.plot(x,y5,"b^--")