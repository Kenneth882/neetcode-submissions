# reader.get(index) is provided by the judge and returns 2147483647 outside the hidden array.
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l=0
        #get the len using binary search; we set r value to 2147483647
        #if reader.get() does not exist and returns 2147483648, then we do l=middle+1 or r=middle-1 depending on what is returned, if 2147... is not reutnred set r to that value and do l-=1 until we get something
        r=10000
        while l<r:
            middle=(l+r)//2
            if reader.get(middle)==2147483647:
                r=middle-1
            else:
                l=middle+1
        l=0
        while l<=r:
            middle=(l+r)//2
            if reader.get(middle)==target:
                return middle
            if reader.get(middle)<target:
                l=middle+1
            else:
               r=middle-1
        return -1
