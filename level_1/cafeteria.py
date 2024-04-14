from typing import List
# Write any import statements here


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  count = 0
  preSeatTaken = 0
  S.append(N+1)
  for seatTaken in S:
    interval = seatTaken - preSeatTaken - 1
    if (preSeatTaken == 0) or (seatTaken == N+1):
      count += interval//(K+1)
    else:
      count += (interval - K)//(K+1)
    preSeatTaken = seatTaken
  return count
