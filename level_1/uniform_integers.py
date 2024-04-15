# Write any import statements here
import math

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  upper_bound = int(math.log10(B)) + 1
  lower_bound = int(math.log10(A)) + 1
  count = 0
  for digits in range(lower_bound, upper_bound + 1):
    target = (10**digits - 1) // 9
    for step in range(1, 10):
      if (step * target >= A) and ((step * target <= B)):
        count += 1 
  return count


if __name__ == "__main__":
  assert getUniformIntegerCountInInterval(75, 300) == 5
  assert getUniformIntegerCountInInterval(1, 9) == 9
  assert getUniformIntegerCountInInterval(999999999999, 999999999999) == 1
