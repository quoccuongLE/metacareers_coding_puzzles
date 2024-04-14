from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  current = 1
  move = 0
  for nex in C:
    if current > nex:
      move += min(N + nex - current, current - nex)
    else:
      # current < nex
      move += min(nex - current, N + current - nex)
    current = nex
      
  return move
