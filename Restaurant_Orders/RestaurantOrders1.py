import sys
sys.setrecursionlimit(150000)

def subSum(array, order, combination = [], menu_combination = []): 
    sum_combination = sum(combination)
    # print(sum(combination), combination)

    # check if the partial sum is equals to target
    if sum_combination == order:
        # print("length of combo: ", combo, len(combo))
        try:
            combo.index(sorted(combination))
        except ValueError:
            if(len(combo) >= 1):
                raise ValueError() # prematurely end the call
            else:
                combo.append(sorted(combination))
                menu_combo.append(sorted(menu_combination))

    if sum_combination >= order:
        return # if we reach the number why bother to continue
    
    for i in range(len(array)):
        n = array[i]
        # remaining = array[i+1:]
        subSum(array, order, combination + [n], menu_combination + [i+1])

_ = input()
menu = list(map(int, input().split(" ")))
_ = input()
orders = list(map(int, input().split(" ")))

for order in orders:
    combo = []
    menu_combo = []
    try:
        subSum(menu, order)
    except ValueError:
        print("Ambiguous")
        continue
    if(len(combo) == 0):
        print("Impossible")
        continue
    print(' '.join(list(map(str, menu_combo[0]))))
