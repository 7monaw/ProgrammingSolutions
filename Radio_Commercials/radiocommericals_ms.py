import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

n, p = map(int, input().split())
breaks = list(map(lambda x: int(x) - p, input().split()))

runningSum = breaks[0]
maximum = breaks[0]

for b in breaks[1:]:
  if b > runningSum + b:
    runningSum = b
  else:
    runningSum += b

  maximum = max(maximum, runningSum)

print(maximum)
