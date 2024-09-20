num = int(input())
l = list(map(int, input().split()))
sorted_l = sorted(l)

count=0
count2=0
count3=0 #for when the 2 ints are neighbors but not the third
small_l = set()
out=""

for i in range(0, num-1):
    if(count==0 and sorted_l[i]+1==sorted_l[i+1]):
        if(count2!=0):
            out+=" "
        count+=1
        count3+=1
        out+=str(sorted_l[i])
    elif(count>0 and sorted_l[i]+1==sorted_l[i+1]):
        count+=1
        continue
    elif(sorted_l[i]+1!=sorted_l[i+1]):
        if(count>1):
            count=0
            out+=str("-")+str(sorted_l[i])
            count2+=1
        else:
            if(count2==0):
                if(count3>0):
                    count=0
                    out+=" " + str(sorted_l[i])
                    count2+=1
                    continue
                count=0
                out+=str(sorted_l[i])
                count2+=1
            else:
                count=0
                out+=" "+ str(sorted_l[i])


if(count>1):
    out+=str("-")+str(sorted_l[-1])
else:
    if(count2==0):
        out+=str(sorted_l[-1])
    else:
        out+=" "+ str(sorted_l[-1])

print(out)
