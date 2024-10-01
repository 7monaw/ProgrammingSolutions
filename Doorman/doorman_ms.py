import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

men = women = inside = 0

diff = int(input())
q = input()
waiting = None

for p in q:
  if abs(men - women) == diff and waiting is None:
    if (men > women and p == 'M') or (women > men and p == 'W'):
      waiting = p
      continue
  elif waiting is not None:
    if p == waiting:
      break
    else:
      if waiting == 'M':
        men += 1
      else:
        women += 1
      waiting = None


  if p == 'M':
    men += 1
  else:
    women += 1

print(men + women)
