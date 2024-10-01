import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

line = input().split()

h, path = int(line[0]), line[1] if len(line) > 1 else ""

node = 1

for d in path:
  if d == 'L':
    node *= 2
  else:
    node *= 2
    node += 1

print(2 ** (h + 1) - node)
