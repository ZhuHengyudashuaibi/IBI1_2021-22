import numpy as np
import matplotlib.pyplot as plt #import

marks=[45,36,86,57,53,92,65,45] #input the data
print(sorted(marks)) #print sorted marks

plt.boxplot(marks,                #draw a boxplot
            notch=False,
            whis=1.3,
            patch_artist=True,
            showcaps=True,
            showfliers=True,
            showbox=True)
plt.ylabel("marks")          #set y label
plt.title("Rob's ICA marks")   #set title
plt.ylim([40,100])       #set  y limit
plt.show()          #printout the plot

ava=np.average(marks)  #evaluate the average marks
if ava>=60:            #if the average value is greater than 60
    print("Pass")      #print "pass"
else:                  #else
    print("fail")      #print "fail"
#result: Rob has failed the ICA.