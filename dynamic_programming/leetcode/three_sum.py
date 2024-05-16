from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    def idxOfTwoSum(nums: List[int], target: int) -> List[List[int]]:
        res = list()
        record = dict()
        for i, x in enumerate(nums):
            if x == "#":
                continue
            diff = target - x
            if diff in record.keys():
                res.append([record[diff], i])
            else:
                record[x] = i
        return res

    triplets = list()
    two_sums_dict = dict()
    for i, x in enumerate(nums):
        # target = 0 => diff = -x
        tmp_list = ["#" for _ in range(i + 1)] + nums[i+1:]
        if -x not in two_sums_dict.keys():
            two_sums_dict[-x] = idxOfTwoSum(tmp_list, -x)

        pairs = [y + [i] for y in two_sums_dict[-x]]
        for k in pairs:
            triplet = [nums[k[0]], nums[k[1]], nums[k[2]]]
            triplet.sort()
            if triplet not in triplets:
                triplets.append(triplet)
    
    return triplets


res = threeSum([-1,0,1,2,-1,-4])
print(res)
# assert res == [[-1,-1,2],[-1,0,1]]