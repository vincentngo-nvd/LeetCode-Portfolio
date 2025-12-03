#Python/Arrays/0001_Two_Sum/solution.py
from typing import List, Optional

def TwoSum(nums: List[int], target: int) -> Optional[List[int]]:
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i

    return None

if __name__ == "__main__":
    print(TwoSum([2, 7, 11, 15], 9))