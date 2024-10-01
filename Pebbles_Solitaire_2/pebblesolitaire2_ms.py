import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')


def getMoves(board):
  moves = []

  for i in range(len(board) - 2):
    a, b, c = board[i], board[i + 1], board[i + 2]

    if (a, b, c) == ('o', 'o', '-'):
      moves.append((i, i + 2, i + 1))
    elif (a, b, c) == ('-', 'o', 'o'):
      moves.append((i + 2, i, i + 1))

  return moves

def aux(board, cache):
  k = ''.join(board)
  if k in cache:
    return cache[k]

  moves = getMoves(board)
  count = board.count('o')

  for start, end, mid in moves:
    board[start] = '-'
    board[end] = 'o'
    board[mid] = '-'

    count = min(count, aux(board, cache))

    board[start] = 'o'
    board[end] = '-'
    board[mid] = 'o'

  cache[k] = count
  return count


n = int(input())
cache = {}

for _ in range(n):
  board = list(input())
  print(aux(board, cache))
