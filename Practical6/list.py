import numpy as np
import matplotlib.pyplot as plt #import

marks=[45,36,86,57,53,92,65,45] #input the data
print(sorted(marks)) #print sorted marks

width=0.35   #width of the bars
ind=np.arange(len(marks))    #set x axis index
plt.bar(ind,marks,width)     #create the bar
plt.xlabel("Practical")      #set x lable
plt.ylabel("Marks")          #set y lable
plt.title("Mark distribution of Rob's eight practical session")   #set the title
plt.yticks(np.arange(0,100,10))                   #set the range of y axis
plt.show() #print out the plot

ava=np.average(marks)  #evaluate the average marks
if ava>=60:            #if the average value is greater than 60
    print("Pass")      #print "pass"
else:                  #else
    print("fail")      #print "fail"
#result: Rob has failed the ICA.