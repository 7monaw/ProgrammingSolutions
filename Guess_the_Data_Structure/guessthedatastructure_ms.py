import sys
import heapq
from collections import deque
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

n = 0

possible = {"stack": [], "queue": deque(), "priority queue": []}

for line in sys.stdin:
  if n == 0:
    n = int(line)
    possible = {"stack": [], "queue": deque(), "priority queue": []}
  else:
    op, x = map(int, line.split())

    if op == 1:
      if "stack" in possible:
        possible["stack"].append(x)
      if "queue" in possible:
        possible["queue"].append(x)
      if "priority queue" in possible:
        heapq.heappush(possible["priority queue"], -x)
    else:
      if "stack" in possible:
        if not possible["stack"] or possible["stack"].pop() != x:
          del possible["stack"]
      if "queue" in possible:
        if not possible["queue"] or possible["queue"].popleft() != x:
          del possible["queue"]
      if "priority queue" in possible:
        if not possible["priority queue"] or heapq.heappop(possible["priority queue"]) != -x:
          del possible["priority queue"]

    n -= 1

    if n == 0:
      if len(possible) == 1:
        print(next(iter(possible)))
      elif len(possible) > 1:
        print("not sure")
      else:
        print("impossible")
