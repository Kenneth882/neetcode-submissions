class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r=m-1
        l=n-1
        curr=len(nums1)-1

        while curr>=0:
            if r==-1:
                nums1[curr]=nums2[l]
                l-=1
                curr-=1
            elif l==-1:
               return nums1
                    
            elif nums1[r]>=nums2[l]:
                nums1[curr]=nums1[r]
                r-=1
                curr-=1
            else:
                nums1[curr]=nums2[l]
                l-=1
                curr-=1
        return nums1