import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

input()

buses = set(map(int, input().split()))

groups = []

for b in buses:
  if b - 1 in buses:
    continue

  lo = b
  hi = 0
  x = lo + 1

  while x in buses:
    hi = x
    x += 1

  if hi == 0:
    groups.append((lo,))
  elif hi == lo + 1:
    groups.append((lo,))
    groups.append((hi,))
  else:
    groups.append((lo, hi))



groups.sort()

res = []

for g in groups:
  if len(g) > 1:
    res.append(f"{g[0]}-{g[1]}")
  else:
    res.append(str(g[0]))

print(" ".join(res))
