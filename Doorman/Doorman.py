num = int(input())
queue = list(input())

men_counter=0
women_counter=0
idx=0
for i in range(0, len(queue)):
    if(queue[i]=="M"):
        men_counter+=1
    else:
        women_counter+=1
    idx+=1
    if(abs(women_counter-men_counter)>num+1):
        print(i-1)
        exit()
if(abs(women_counter-men_counter)>num):
    print(len(queue)-1)
else:
    print(len(queue))
