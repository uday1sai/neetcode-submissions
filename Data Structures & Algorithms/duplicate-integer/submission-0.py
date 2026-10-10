class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        # unq_elements=set(nums)
        # has_dup=len(nums)!=len(unq_elements)    
        # return len(nums)!=len(set(nums))        
            
        