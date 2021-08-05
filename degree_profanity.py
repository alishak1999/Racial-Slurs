import matplotlib.pyplot as plt
import numpy as np

tweets = open('tweets.txt', 'r')    # file with tweets
slurs = open('slurs.txt', 'r')      # file with slurs

# adding all contents of slurs.txt to a list for easy inference
slur_list = []
for s in slurs:
    slur_list = s.split()


x_axis = []     # tweet number
y_axis = []     # count of profanity

count_tweet = 0
for t in tweets:
    count_tweet += 1    # maintains count of tweet number
    # x_label = "Tweet "+str(count_tweet)
    
    count_slur = 0      # maintains count of slurs for every tweet
    
    # counting the number of slurs per tweet
    word = t.split()
    for w in word:
        if w in slur_list:
            count_slur += 1
    # print(str(word)+": "+str(count_slur))

    x_axis.append(str(count_tweet))     # appending tweet number, converting to str to avoid appearing as a range on x-axis
    y_axis.append(count_slur)           # no. of slurs per tweet gets appended as numeric value

X = np.array(x_axis)    # defining the x axis for the plot
Y = np.array(y_axis)    # defining the y axis for the plot

plt.bar(X, Y)                               # plotting a bar chart
plt.xlabel("Tweet Number")                  # setting x-axis label
plt.ylabel("No. of explicit words")         # setting y-axis label
plt.show()                                  # display the plot