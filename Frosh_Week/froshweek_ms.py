import sys
input = lambda: sys.stdin.readline().strip('\n')
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

n = int(input())
nums = []

for _ in range(n):
  nums.append(int(input()))

moves = 0

def sort(nums):
  if len(nums) <= 1:
    return nums

  global moves
  mid = len(nums) // 2

  a = sort(nums[:mid])
  b = sort(nums[mid:])

  k = 0

  i = j = 0

  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      nums[k] = a[i]
      i += 1
    else:
      nums[k] = b[j]
      j += 1
      moves += len(a) - i
    k += 1

  left, idx = (a, i) if j == len(b) else (b, j)

  for l in range(idx, len(left)):
    nums[k] = left[l]
    k += 1

  return nums

sort(nums)
print(moves)
