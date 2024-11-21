coords = []
for _ in range(3):
    coords.append(tuple(map(int, input().split(" "))))

n = int(input())
apple_coords = []
for _ in range(n):
    apple_coords.append(tuple(map(int, input().split(" "))))

def area(A, B, C):
    return abs((A[0] * (B[1]-C[1]))+(B[0]*(C[1]-A[1]))+(C[0]*(A[1]-B[1]))) / 2

def isInside(A, B, C, P, area_t):
    a = area(A, B, P)
    b = area(A, C, P)
    c = area(B, C, P)
    if (a + b + c == area_t):
        return True
    else:
        return False

area_land = area(coords[0], coords[1], coords[2])
print('%.1f'%area_land)

counter = 0
for i in apple_coords:
    if isInside(coords[0], coords[1], coords[2], i, area_land) == True:
        counter+=1
print(counter)
