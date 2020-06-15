
import matplotlib.pyplot as plt


x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]


plt.figure(figsize=(20,8),dpi=80)

plt.xlabel('Time(h)')
plt.ylabel('Temperature (C)')
plt.title('Temperature change during the daytime')

plt.plot(x,y)

plt.xticks(range(2,25,2))
plt.yticks(range(min(y),max(y)+2,2))

plt.show()

##plt.xlim((-1,2))
##plt.ylim((-1,3))

##plt.xlabel('I am x')
##plt.ylabel('I am y')
##plt.title('Temperature change during the daytime')

## 调整大小
##plt.figure(figsize=(20,8),dpi=80)


##轴刻度
##plt.xticks(range((2,25,5))
##plt.yticks(range(min(y),max(y)+2,2))

##new_ticks = np.linspace(-1,2,5)
##print(new_ticks)
##plt.xticks(new_ticks)
##plt.yticks([-2,-1.8,-1,1.22,3],
            ##['really bad','bad',r'$noraml\ \delta$','good','excellent'])


##gca"get current axis'
##ax = plt.gca()
##ax.spines['right'].set_color('none')
##ax.spines['top'].set_color('none')
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##ax.spines['bottom'].set_position(('data',0)) #outward, axes
##ax.spines['left'].set_position(('data',0))





