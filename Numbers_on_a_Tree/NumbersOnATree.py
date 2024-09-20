# 1 -> 3
# 2 -> 7
# 3 -> 15
# 4 -> 31

l = list(input().split(" "))
height = int(l[0])

# Find root
root=1
h = 1
while h <= height:
    root+=2**h
    h+=1

if(len(l)==1):
    print(root)
    exit()
path = list(l[1])

index = 1
for step in path:
    if(step=="L"):
        temp = index
        index = 2*temp
        diff = index-temp
        root-=diff
    else:
        temp = index
        index = 2*temp+1
        diff = index-temp
        root-=diff
print(root)
