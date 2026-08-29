class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res=[0]*len(nums)
        total=len(nums)
        for i in range(len(nums)):
            res[(i+k)%total]=nums[i]
        nums[:]=res
        