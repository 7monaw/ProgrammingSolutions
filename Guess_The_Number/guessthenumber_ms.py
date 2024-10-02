import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

lo, hi = 1, 1000

while True:
  mid = (lo + hi) // 2

  print(mid)
  sys.stdout.flush()

  ans = input()

  if ans == "lower":
    hi = mid - 1
  elif ans == "higher":
    lo = mid + 1
  else:
    break
