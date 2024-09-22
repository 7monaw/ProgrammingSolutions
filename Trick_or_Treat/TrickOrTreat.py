import sys

def ternarySearch(l, r, arr, x_minimum, dist_minimum, lr):
    # print("what are the lr:", l, r)
    lr.append([l,r])
    if(abs(l-r)>1e-12):
        mid1 = l+((r-l)/3)
        mid2 = r-((r-l)/3)
        # print("two mids:", mid1, mid2)
        max_distance1 = -100000000000000 #just to initialize distance
        max_distance2 = -100000000000000 #just to initialize distance
        min_x1 = r
        min_x2 = r

        for y1 in arr:
            distance = ((mid1-y1[0])**2+(y1[1])**2) ** (1/2)
            # print("distance1:", y1[0], distance)
            if(distance>max_distance1):
                max_distance1=distance
                min_x1 = y1[0]
        # print("min_x1:", min_x1)

        for y2 in arr:
            distance = ((mid2-y2[0])**2+(y2[1])**2) ** (1/2)
            # print("distance2:", y2[0], distance)
            if(distance>max_distance2):
                max_distance2=distance
                min_x2 = y2[0]
        # print("min_x2:", min_x2)
        
        if(max_distance1<max_distance2):
            x_minimum.append(min_x1)
            dist_minimum.append(max_distance1)
            # print(dist_minimum)
            # print("2:", l, min_x2)
            ternarySearch(l, mid2, arr, x_minimum, dist_minimum, lr)
        else:
            x_minimum.append(min_x2)
            dist_minimum.append(max_distance2)
            # print("1:", l, min_x1)
            # print(min_x1-r)
            ternarySearch(mid1, r, arr, x_minimum, dist_minimum, lr)
    return lr, min(dist_minimum[1:]), (lr[-1][0]+lr[-1][1])/2 #x_minimum[dist_minimum.index(min(dist_minimum[1:]))]

for line in sys.stdin:
    num = int(line)
    if(num == 0):
        exit()
    coords = []
    maximum = -100000000000000
    minimum = 10000000000000
    for i in range(0, num):
        coords.append(tuple(map(float, input().split(" "))))
        if(coords[i][0]<minimum):
            minimum = coords[i][0]
        elif(coords[i][0]>maximum):
            maximum = coords[i][0]
    x_minimum = [maximum]
    dist_minimum = [-1000000000000]
    lr = []
    lr, time, x = ternarySearch(minimum, maximum, coords, x_minimum, dist_minimum, lr)
    x = "%.5f"%(x)
    time = "%.5f"%(time)
    print(x, time)
    _ = input()
