import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

line = input()
text = []

for c in line:
  if c == '<':
    text.pop()
  else:
    text.append(c)

print("".join(text))
