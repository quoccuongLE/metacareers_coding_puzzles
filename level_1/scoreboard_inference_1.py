from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  ones = 0
  twos = S[-1] // 2
  if S[-1] % 2 != 0:
    ones +=1

  for i in range(len(S) - 1, 0, -1):
    s = S[i]
    if s % 2 != 0 and (s % 2) > ones:
      ones += 2
      twos -= 1
  return ones + twos
