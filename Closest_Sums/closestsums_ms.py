import sys
from bisect import bisect
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

cases = 0

while True:
  line = next(sys.stdin, None)

  if not line:
    break

  cases += 1
  print(f"Case {cases}:")

  n = int(line)
  nums = set()
  sums = []

  for _ in range(n):
    x = int(next(sys.stdin))

    for y in nums:
      sums.append(x + y)

    nums.add(x)

  sums.sort()

  m = int(next(sys.stdin))

  for _ in range(m):
    x = int(next(sys.stdin))
    i = bisect(sums, x)

    if i == 0:
      closest = sums[0]
    elif i == len(sums):
      closest = sums[-1]
    else:
      closest = min(sums[i - 1], sums[i], key=lambda y: abs(x - y))

    print(f"Closest sum to {x} is {closest}.")
