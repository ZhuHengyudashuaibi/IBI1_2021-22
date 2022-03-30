import os                  #Allow working on files and directories
import pandas as pd        #Allow working with dataframes.
import matplotlib.pyplot as plt
import numpy as np

os.chdir("E:/cygwin/home/Think/IBI_2021-22/IBI1_2021-22/Practical7")
covid_data = pd.read_csv("full_data.csv")           #import csv file.
print(covid_data.iloc[9:20,[0,2]])          #Show the first and third column from row 10 to row 20
#my_column=[False,False,False,False,True,False]
#print(covid_data.iloc[0:82,my_column])      #access the data with bolean
Afganhanistan_location=covid_data.iloc[:,1]               #access the "location" colume
Afganhanistan_location=list(Afganhanistan_location)                     #convert into list type
Afganhanistan_col=[]
#for everymember in location
#if location[evermember]=""Afghanistan
#store Ture in a list
#else
#False
for i in range(len(Afganhanistan_location)):
    Afganhanistan_col.append(Afganhanistan_location[i]=='Afghanistan')
Afghanistan_totalcases=covid_data.loc[Afganhanistan_col,"total_cases"]    #access the data of the total cases of Afghanistan with bolean.
print(Afghanistan_totalcases)

China_col=[]
China_location=covid_data.iloc[:,1]
China_location=list(China_location)
for i in range(len(China_location)):
    China_col.append(China_location[i]=='China')       #accessing Chinese data
China_new_data=covid_data.loc[China_col,['new_cases','new_deaths']]  #access new cases and new deaths
China_newcases_mean=np.mean(China_new_data.iloc[:,0]);print('China_new_cases_mean_value =',China_newcases_mean) #compute the mean value
China_newdeaths_mean=np.mean(China_new_data.iloc[:,1]);print('China_new_deaths_mean_value =',China_newdeaths_mean)

plt.boxplot(China_new_data,
            vert=True,whis=0.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=False,notch=False,
            labels=['China_new_cases','China_new_deaths'])
plt.title('China_newcases and new deaths')
plt.ylabel('number')
plt.show()                        #Box plot for China's new cases and deaths

China_dates=covid_data.loc[China_col,'date']  #access China dates
plt.plot(China_dates,China_new_data.loc[:,'new_cases'],'b+')
plt.plot(China_dates,China_new_data.loc[:,'new_deaths'],'r+')
plt.xticks(China_dates.iloc[0:len(China_dates):5],rotation=-90,fontsize=5)
plt.xlabel('Dates')
plt.ylabel('numbers')
plt.title("China's new cases and new deaths versus time")
plt.show()         #output the plot of China's new cases and deaths vs time
################## Question part###############################################################
#acesss total_cases data
#access the dates of three countries
#make a plot
#adjust

location=covid_data.iloc[:,1]
Korea_col=[]
Kenya_col=[]
Colombia_col=[]
for i in range(len(location)):
    Korea_col.append(location[i]=='South_Korea')
    Kenya_col.append(location[i]=='Kenya')
    Colombia_col.append(location[i]=='Colombia')
Korea_totalcases=covid_data.iloc[Korea_col,4]
Kenya_totalcases=covid_data.iloc[Kenya_col,4]
Colombia_totalcases=covid_data.iloc[Colombia_col,4]   #access

#plot
Korea_dates=covid_data.loc[Korea_col,'date']
Kenya_dates=covid_data.loc[Kenya_col,'date']
Colombia_dates=covid_data.loc[Colombia_col,'date']

plt.plot(Korea_dates,Korea_totalcases,'b+')
plt.plot(Kenya_dates,Kenya_totalcases,'r+')
plt.plot(Colombia_dates,Colombia_totalcases,'g+')
plt.xticks(Korea_dates.iloc[0:len(Korea_dates):5],rotation=-90,fontsize=6)
plt.xlabel('Dates')
plt.ylabel('number of people')
plt.title('Total cases of South korea, Kenya and Colombia')
plt.show()




