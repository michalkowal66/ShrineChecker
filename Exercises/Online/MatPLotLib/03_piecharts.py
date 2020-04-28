from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.15, 0]    #We can pass an explode list to show
                                #which data we are highliting

plt.pie(slices, labels= labels, explode= explode, shadow= True, 
        wedgeprops= {"edgecolor": "black"}, startangle= 90, autopct= "%1.1f%%")
#Pie charts are created just like bar and line charts, we pass first
#x value, then labels. Check documentation for more arguments.

plt.title("Pie Chart")
plt.tight_layout()
plt.show()