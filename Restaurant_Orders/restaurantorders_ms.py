import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')


n = int(input())

items = list(map(int, input().split()))

input()

orders = list(map(int, input().split()))
top = max(orders)

table = [[0 for _ in range(top + 1)] for _ in range(n)]

for i in range(n):
  table[i][0] = 1

  for amt in range(1, top + 1):
    table[i][amt] += table[i - 1][amt]

    if amt >= items[i]:
      table[i][amt] += table[i][amt - items[i]]


for o in orders:
  order = table[n - 1][o]

  if order == 0:
    print("Impossible")
  elif order > 1:
    print("Ambiguous")
  else:
    l = []
    amt = o
    i = n - 1

    while amt > 0:
      if amt >= items[i] and table[i][amt - items[i]] == 1:
        l.append(i + 1)
        amt -= items[i]
      else:
        i -= 1

    print(*reversed(l))
