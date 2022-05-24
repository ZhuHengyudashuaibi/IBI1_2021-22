import matplotlib.pyplot as plt   #import

paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

vs=dict(zip(paternal_age,chd))  #This code was obtained from https://blog.csdn.net/Kefenggewu_/article/details/123522854.
print(vs)                       #print the dictionary.

plt.scatter(paternal_age,chd,marker='o')  #output the plot.
plt.xlabel('paternal_age')
plt.ylabel('chd')
plt.title('Parent_age vs chd')

plt.show() #print out the plot

age=30 #creat a variable that stores the input age, for example, 30.
print(vs[age]) #output the risk of corresponding age in vs dictionary





