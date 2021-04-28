import matplotlib.pyplot as plt
import numpy as np
 
data = np.genfromtxt('data.dat',
                     delimiter='\t')

# multiple line plots
# plt.plot( 'x_values', 'y1_values', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
# plt.plot( 'x_values', 'y2_values', data=df, marker='', color='olive', linewidth=2)
# plt.plot( 'x_values', 'y3_values', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")

data_n = 80

r = 0
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
r = 1
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='blue', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=12)
r = 2
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
r = 3
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='green', markersize=12)
r = 4
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='red', markersize=12)
r = 5
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='blue', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='blue', markersize=12)
r = 6
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='green', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='green', markersize=12)
r = 7
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='blue', markersize=12)
r = 8
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
r = 9
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='blue', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=12)
r = 10
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
r = 11
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='green', markersize=12)
r = 12
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='red', markersize=12)
r = 13
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='green', markersize=12)
r = 14
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='red', markersize=12)
r = 15
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='blue', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='blue', markersize=12)
r = 16
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='green', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='green', markersize=12)
r = 17
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='blue', markersize=12)
r = 18
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='blue', markersize=12)
r = 19
plt.plot(data[data_n*r:data_n*(r+1),0], data[data_n*r:data_n*(r+1),3], color='red', linestyle='dashed', linewidth = 3,
         marker='x', markerfacecolor='blue', markersize=12)

# show legend
plt.legend()

# show graph
plt.show()