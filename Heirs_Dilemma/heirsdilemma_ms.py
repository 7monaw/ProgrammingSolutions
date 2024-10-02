import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def good(x):
  digits = list(map(int, str(x)))
  uniq = set(digits)

  if len(digits) != len(uniq) or 0 in uniq:
    return False

  for d in digits:
    if x % d != 0:
      return False

  return True


L, H = map(int, input().split())
total = 0

for i in range(L, H + 1):
  total += good(i)

print(total)
