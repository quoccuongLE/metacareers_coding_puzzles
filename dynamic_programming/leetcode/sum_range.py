class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sums = []
        val = 0
        for x in nums:
            val += x
            self.prefix_sums.append(val)

    def sumRange(self, left: int, right: int) -> int:
        right_val = self.prefix_sums[right]
        left_val = self.prefix_sums[left - 1] if left > 0 else 0
        return right_val - left_val

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(2, 5))
