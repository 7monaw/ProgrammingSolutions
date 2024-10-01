import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

while True:
  n, *perm = map(int, input().split())

  if n == 0:
    break

  res = ["'"]

  line = input()
  line = line + ' ' * ((n - len(line) % n) % n)

  for i in range(len(line) // n):
    for j in range(n):
      idx = i * n + perm[j] - 1

      res.append(line[idx])

  res.append("'")

  print("".join(res))
