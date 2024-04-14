from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  P.sort()
  firstPos = P[0]
  optimal_final_shift = N - len(P) - firstPos
  
  return (F - 1) + optimal_final_shift + 1
