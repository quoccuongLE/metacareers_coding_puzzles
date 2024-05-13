# Write any import statements here
import math


def getArtisticPhotographCount_legacy(N: int, C: str, X: int, Y: int) -> int:
  """
  Time complexity = O(N^2)
  You solved 34 / 39 test cases.
  Time Limit Exceeded on 5 test cases
  """
  # Write your code here
  p_locs = [i for i, x in  enumerate(C) if x == "P"]
  a_locs = [i for i, x in  enumerate(C) if x == "A"]
  b_locs = [i for i, x in  enumerate(C) if x == "B"]
  count_pab = 0
  count_bap = 0

  count_pa = {a: 0 for a in a_locs}
  count_ba = {a: 0 for a in a_locs}
  count_ab = {a: 0 for a in a_locs}
  count_ap = {a: 0 for a in a_locs}

  for p in p_locs:
    for a in a_locs:
      if a - p >= X and a - p <= Y:
        count_pa[a] += 1
      elif p - a >= X and p - a <= Y:
        count_ap[a] += 1

  for b in b_locs:
    for a in a_locs:
      if b - a >= X and b - a <= Y:
        count_ab[a] += 1
      elif a - b >= X and a - b <= Y:
        count_ba[a] += 1

  count_pab = sum([x*y for x, y in zip(count_pa.values(), count_ab.values())])
  count_bap = sum([x*y for x, y in zip(count_ba.values(), count_ap.values())])
  return count_pab + count_bap


def getArtisticPhotographCount_legacy_2(N: int, C: str, X: int, Y: int) -> int:
  """
  Time complexity = O(N^2)
  You solved 29 / 39 test cases.
  Time Limit Exceeded on 10 test cases
  """
  # Write your code here
  p_locs = [i for i, x in  enumerate(C) if x == "P"]
  a_locs = [i for i, x in  enumerate(C) if x == "A"]
  b_locs = [i for i, x in  enumerate(C) if x == "B"]
  count_pab = 0
  count_bap = 0

  count_pa = {a: 0 for a in a_locs}
  count_ba = {a: 0 for a in a_locs}
  count_ab = {a: 0 for a in a_locs}
  count_ap = {a: 0 for a in a_locs}

  for a in a_locs:
    for i in range(X, Y + 1):
      if a - i in p_locs:
        count_pa[a] += 1
      if a + i in p_locs:
        count_ap[a] += 1
      if a - i in b_locs:
        count_ba[a] += 1
      if a + i in b_locs:
        count_ab[a] += 1
    

  count_pab = sum([x*y for x, y in zip(count_pa.values(), count_ab.values())])
  count_bap = sum([x*y for x, y in zip(count_ba.values(), count_ap.values())])
  return count_pab + count_bap


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  """
  Time complexity = O(N)
  """
  # Write your code here
  a_locs = [i for i, x in  enumerate(C) if x == "A"]

  prev_P_count_map = [0]
  prev_B_count_map = [0]
  P_count = 0
  B_count = 0

  for char in C:
    if char == "P":
      P_count += 1
    if char == "B":
      B_count += 1
    prev_P_count_map.append(P_count)
    prev_B_count_map.append(B_count)

  count_pab = 0
  count_bap = 0
  for a in a_locs:
    y_limit = max(0, a - Y)
    x_limit = max(0, a - X + 1)
    count_pa = prev_P_count_map[x_limit] - prev_P_count_map[y_limit]
    count_ba = prev_B_count_map[x_limit] - prev_B_count_map[y_limit]

    y_limit = min(len(C), a + Y + 1)
    x_limit = min(len(C), a + X)
    count_ap = prev_P_count_map[y_limit] - prev_P_count_map[x_limit]
    count_ab = prev_B_count_map[y_limit] - prev_B_count_map[x_limit]

    count_pab += count_pa*count_ab
    count_bap += count_ba*count_ap

  return count_pab + count_bap


if __name__ == "__main__":
  assert 1 == getArtisticPhotographCount(N=5, C="APABA", X=1, Y=2)
  assert 0 == getArtisticPhotographCount(N=5, C="APABA", X=2, Y=3)
  assert 3 == getArtisticPhotographCount(N=8, C=".PBAAP.B", X=1, Y=3)
