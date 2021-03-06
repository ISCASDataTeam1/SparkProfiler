import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 1.5 #set the value globally

#plt.rc('font', family='Helvetica')
# font = {'family' : 'Helvetica',
#         'weight' : 'normal',
#         'color'  : 'black',
#         'size'   : '12'}


plt.rc('font', family='Helvetica', size=12)

N = 3
ind = np.arange(N)  # the x locations for the groups

width = 0.23       # the width of the bars

fig = plt.figure(figsize=(3.2, 2.4))
ax = fig.add_subplot(111)
plt.subplots_adjust(left=0.19, bottom=0.11, right=0.98, top=0.87,
                    wspace=0.03, hspace=0.04)

#plt.tight_layout()

xvals = [19, 60, 0]
yvals = [22, 8, 27]
zvals = [14, 2, 28]

rects1 = ax.bar(ind, xvals, width, color='hotpink', edgecolor='black', hatch="///")
rects2 = ax.bar(ind+width, yvals, width, color='lightgreen', edgecolor='black', hatch='xxx')
rects3 = ax.bar(ind+width*2, zvals, width, color='dodgerblue', edgecolor='black', hatch='\\\\\\')

ax.set_ylabel('GC time (s)', color='black')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('YGC', 'FGC', 'ConGC'), color='black' )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Parallel', 'CMS', 'G1'),
           frameon=False, loc = "upper right", labelspacing=0.2, markerfirst=False, fontsize=10 )
ax.set_ylim(0, 100)  # The ceil
#plt.xlim(-0.3, 2.76)  # The ceil
ax.set_xlim(-0.3, 2.76)  # The ceil

#plt.title("(a) GroupBy-task-execution-time", fontsize=12)
plt.title("(b) GroupBy-task-GC-time", fontsize=12)


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


plt.show()