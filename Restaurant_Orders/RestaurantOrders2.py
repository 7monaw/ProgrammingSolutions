## Faster DP Solution ##

import sys
sys.setrecursionlimit(1500000000)

def makeTable(menu, n, sum):
    for i in range(1, n+1):
        # subset[i][0] = 1
        for j in range(0, sum+1):
            # print(i, j)
            if(i >= 1):
                subset[i][j] += subset[i-1][j]
            if(j - menu[i-1] >= 0):
                subset[i][j] += subset[i][j - menu[i-1]]
    return subset

def backtracking(subset, i, j, string):
    # print("i", i)
    # print("j", j)
    if(j == 0 & i == 0):
        return
    if(j - menu[i-1]) < 0:
        # print("one")
        backtracking(subset, i-1, j, string)
    elif(subset[i][j - menu[i-1]] == 0):
        # print("two")
        backtracking(subset, i-1, j, string)
    elif(subset[i][j - menu[i-1]] == 1):
        # print("three")
        string.append(str(i))
        # print(string)
        backtracking(subset, i, j - menu[i-1], string)


_ = input()
menu = list(map(int, input().split(" ")))
_ = input()
orders = list(map(int, input().split(" ")))


subset = ([[0 for i in range(0, max(orders) + 1)] for i in range(0, len(menu)+1)])
subset[0][0] = 1
subset = makeTable(menu, len(menu), max(orders))
for order in orders:
    outcome = subset[len(menu)][order]

    if (outcome > 1):
        print("Ambiguous")
    elif (outcome == 1):
        out = []
        # print(subset)
        backtracking(subset, len(menu), order, out)
        out = list(map(str, sorted(list(map(int, out)))))
        print(" ".join(out))
    else:
        print("Impossible")
