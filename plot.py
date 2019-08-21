import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import os

#Define variable to plot the graph
fig = plt.figure();
ax1 = fig.add_subplot(1,1,1)

# Function which has the codes to be iterated
def animate(i):
    f = open("Final.txt", "r")
    f=f.read()
#Extract the values from text file, in case of an error takes
#the value of (0,0) only for that particular frame
    split = f.split(' ');
    try:
       x = int(split[0]);
    except ValueError:
       x = 0
    except IndexError:
       x = 0
    try:
       y = int(split[1]);
    except ValueError:
       y = 0
    except IndexError:
       y = 0 
    #print(x,y)
    ax1.clear()
    ax1.set_xlim([-100, 100])
    ax1.set_ylim([-100, 100])
    ax1.plot(-x,y,'bo')
    plt.axvline(x=0)
    plt.axhline(y=0)
# if the coordinate of x and y is in the range of 10 to -10, both cross hair at x=0 and y=0 appear
# red, suggesting the marker is no longer moving 
    if x < 10 and x > -10:
       plt.axhline(color = 'red')
       plt.text(-90,-90,'X = OK',fontsize=11)
    if y < 10 and y > -10:
       plt.axvline(color = 'red')
       plt.text(-90,-80,'Y = OK',fontsize=11)
# iterates the animate,plot function and update every 1 ms
ani = animation.FuncAnimation(fig,animate,interval=1)
#display plot
plt.show()






  
    
   

         
