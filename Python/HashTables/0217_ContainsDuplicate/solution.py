#Python/HashTables/0217_ContainsDuplicate
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  

        for n in nums:
            if n in seen:
                return True
            
            seen.add(n)
            
        return False

if __name__ == "__main__":
    solver = Solution()
    
    print(solver.containsDuplicate([1, 2, 3, 1])) 
    
    print(solver.containsDuplicate([1, 2, 3, 4]))