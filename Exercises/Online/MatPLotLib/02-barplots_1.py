from matplotlib import pyplot as plt
import numpy as np

#Plotting bar plots using data from previous exercise
#Note - it's possible to mix the plot types on a single plot - for example one set of data will be presented as bars and other as lines

plt.style.use("ggplot")

#plt.xkcd() #plots hand drawn like graph

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]   #define list with x values

x_indexes = np.arange(len(ages_x))  #We need to create a numpy array containing indexes of all ages to subtract from or add to them bars width
                                    #to be able to see the bars not overlapping each other 
print(x_indexes)
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]  #define list with first y values
plt.bar(x_indexes - width, dev_y, width = width,
        color = "#444444", label = "All Devs")    #plot bar x vs y with certain color and label, we move the bar to the left

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]   #define another y values,
plt.bar(x_indexes, py_dev_y, width = width,
        label = "Python Devs") #plot another bar, without offset, this is the middle bar

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, width = width,
        label = "JS Devs") #plot last bar, moving it to the right by the width of the bar, so all bars are adjacent but not overlapping
                           #We could also offset the bars by a different value slightly higher than width, so there'll be a little break between the bars

plt.legend()    #inserts a legend in top-left corner, we can define labels by putting a list of strings containing respective line names

plt.xticks(ticks = x_indexes, labels = ages_x) #We use xticks to define x_indexes as points of insertion of a bar, the labels are for defining the real labels of data

plt.xlabel("Ages")  #show name of x label
plt.ylabel("Median salary (USD)")   #show name of y label
plt.title("Median salary (USD) by age") #show title of the graph

plt.tight_layout()

plt.savefig("graph.png") #saves plot to a file with specified name - saves into script's path as a default unless you specify the path "C://.../plot.png"

plt.show()