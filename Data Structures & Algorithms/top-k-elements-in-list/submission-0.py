class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        counter={}
        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1
        arr=[]
        for num,cnt in counter.items():
            arr.append([cnt,num])
        arr.sort()
    
        for i in range(len(arr)):
            if k==0:
              break
            else:
                res.append(arr.pop()[1])
                k-=1

        return res


        