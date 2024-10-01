import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def dist(a, b):
  dx = a[0] - b[0]
  dy = a[1] - b[1]
  return dx * dx + dy * dy




while True:
  n = int(input())

  if n == 0:
    break

  houses = []

  for _ in range(n):
    houses.append(tuple(map(float, input().split())))

  lo = min(houses, key=lambda x: x[0])[0]
  hi = max(houses, key=lambda x: x[0])[0]
  f = lambda x: max(dist((x, 0), house) for house in houses)

  while (hi - lo) > 1e-5:
    c = lo + (hi - lo) / 3
    d = lo + 2 * (hi - lo) / 3

    if f(c) < f(d):
      hi = d
    else:
      lo = c

  x = (lo + hi) / 2
  dur = f(x) ** 0.5
  print(f'{x:.9f} {dur:.9f}')
  input()
