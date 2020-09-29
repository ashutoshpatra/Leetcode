class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d ={}
        for each in nums:
            if each in d:
                d[each] = d.get(each,0)+1
            else:
                d[each] = 1
        for each in nums:
            if d[each]==1:
                return(each)
