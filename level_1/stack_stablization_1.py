from typing import Sequence
# Write any import statements here

# def getMinimumDeflatedDiscCount(N: int, R: Sequence[int]) -> int:
#   # Write your code here
#   max_height = R[1]
#   if max_height < len(R):
#     return -1
#   minimal_ref = list(range(max_height, 1, -1))
#   delta = R - minimal_ref
#   min_val = min(delta[1:])


# def getMinimumDeflatedDiscCount(N: int, R: Sequence[int]) -> int:
#   """
#   Recursive solution !
#   You solved 20 / 33 test cases.
#   Time Limit Exceeded on 12 test cases
#   Wrong Answer on 1 test case
#   """
#   # Write your code here
#   max_size = R[-1]
#   if max_size < len(R):
#     return  -1
  
#   count = 0
#   min_size = 1
#   for idx, r in enumerate(R):
#     if idx == len(R) - 1:
#       continue

#     if r < R[idx + 1]:
#       continue
#     else:
#       if idx == 0:
#         count = 1
#       else:
#         r_sub = R[idx + 1] - 1
#         R_sub = R[:idx] + [r_sub]
#         sub_count = getMinimumDeflatedDiscCount(idx + 1, R_sub)
#         count = sub_count + 1

#   return count


def getMinimumDeflatedDiscCount(N: int, R: Sequence[int]) -> int:
  # Write your code 
  count = 0
  prev_size = R[-1]
  for i in range(N - 1, 0, -1):
    if R[i] <= i:
      return -1
    
    if prev_size > R[i-1]:
      prev_size = R[i-1]
    else:
      prev_size -=1
      count += 1
  
  return count


if __name__ == "__main__":
  N = 5
  R = [2, 5, 3, 6, 5]
  assert getMinimumDeflatedDiscCount(N, R) == 3

  N = 3
  R = [100, 100, 100]
  assert getMinimumDeflatedDiscCount(N, R) == 2

  N = 4
  R = [6, 5, 4, 3]
  assert getMinimumDeflatedDiscCount(N, R) == -1

  N = 2
  R = [6, 7]
  assert getMinimumDeflatedDiscCount(N, R) == 0
