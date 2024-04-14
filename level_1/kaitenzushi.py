from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  window = {}
  eaten_counter = 0
  
  for d in D:
    if not d in window or (eaten_counter - window[d]) > K:
      window[d] = eaten_counter
      eaten_counter += 1
  return eaten_counter
