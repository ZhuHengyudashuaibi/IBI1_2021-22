a= 19245301  #Total number of COVID-19 case in UK on 2022/3/7.
b= 4218520   #COVID-19 case in UK on 2021/3/7.
c=271        #COVID-19 case in UK on 2020/3/7.
d=b-c        #difference between 2021 and 2020.
e=a-b       #difference 2022 and 2021.
f= d>e     
h= d/c>e/b
print("d=",d)
print("e=",e)
print("d>e",f)  #d<e
print("Rate of 2020 is greater", h)     #Rate in 2020 is larger
#Booleans
X="Hello"; Y="World"
W=X or Y
print(W)
