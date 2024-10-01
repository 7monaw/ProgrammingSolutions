import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')


def getMoves(board):
  moves = set()

  for i in range(len(board) - 2):
    if (board[i], board[i + 1], board[i + 2]) == ('o', 'o', '-'):
      moves.add((i, i + 1, i + 2))

    if (board[i], board[i + 1], board[i + 2]) == ('-', 'o', 'o'):
      moves.add((i + 2, i + 1, i))

  return moves


def play(board):
  moves = getMoves(board)

  pebbles = board.count('o')

  if not moves:
    return pebbles

  for m in moves:
    board[m[0]] = '-'
    board[m[1]] = '-'
    board[m[2]] = 'o'

    pebbles = min(pebbles, play(board))

    board[m[0]] = 'o'
    board[m[1]] = 'o'
    board[m[2]] = '-'

  return pebbles

n = int(input())

for _ in range(n):
  res = play(list(input()))
  print(res)
