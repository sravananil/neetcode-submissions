class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key, values in seen.items():
            bucket[values].append(key)
        result = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                result.append(j)
                
                if len(result)==k :
                    break
            if len(result)==k:
                break
        return result