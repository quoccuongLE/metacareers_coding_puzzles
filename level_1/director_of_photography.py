# Write any import statements here
import math


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  p_locs = [i for i, x in  enumerate(C) if x == "P"]
  a_locs = [i for i, x in  enumerate(C) if x == "A"]
  b_locs = [i for i, x in  enumerate(C) if x == "B"]
  
  count = 0
  for a in a_locs:
    for p in p_locs:
      if not (abs(p - a) >= X and abs(p - a) <= Y):
        continue
      for b in b_locs:
        if (b - a)*(p - a) > 0:
          continue
        if abs(a - b) >= X and abs(a - b) <= Y:
          count += 1
  return count


if __name__ == "__main__":
  assert 1 == getArtisticPhotographCount(N=5, C="APABA", X=1, Y=2)
  assert 0 == getArtisticPhotographCount(N=5, C="APABA", X=2, Y=3)
  assert 3 == getArtisticPhotographCount(N=8, C=".PBAAP.B", X=1, Y=3)
