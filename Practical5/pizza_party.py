#Count cuts until p=64
#If p<64
#    calculate the p
#    n=n+1
#    repeat
#    print out n
#If p>=64
#   Done!

n=0
p=1
cuts=""
while p<= 64:
    n = n + 1
    p= (n**2+n+2)/2
    cuts=cuts+str(n)+","   #out put numbers of cut into a sentence

print(n)
 



