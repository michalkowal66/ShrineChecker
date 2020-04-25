from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

#Plotting bar plots using data from previous exercise
#Note - it's possible to mix the plot types on a single plot - for example one set of data will be presented as bars and other as lines

plt.style.use("fivethirtyeight")

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()    #We create a counter

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))  #For each row of csv file we update the counter with a list of languages
                                                                        #We use split to change the form of data storing from one element lits
                                                                        #to n-long list of elements which were divided by ; symbol

languages = []
popularity = []
#print(language_counter) #language_counter is a dictionary containing all provided languages and number of their occurences in the form {"Language": <occurences>}
#print(language_counter.most_common(15)) #most_common shows n most common entries depending on provided argument in the function, data is stored in form of tuples

for entry in language_counter.most_common(15):
    languages.append(entry[0])
    popularity.append(entry[1])

languages.reverse()
popularity.reverse()    #Rearranging the list to show lowest values first

plt.barh(languages, popularity)

# plt.ylabel("Programming languages")  #show name of x label
plt.xlabel("Number of people who use")   #show name of y label
plt.title("Most popular languages") #show title of the graph

plt.tight_layout()

# #plt.savefig("graph.png") #saves plot to a file with specified name - saves into script's path as a default unless you specify the path "C://.../plot.png"

plt.show()