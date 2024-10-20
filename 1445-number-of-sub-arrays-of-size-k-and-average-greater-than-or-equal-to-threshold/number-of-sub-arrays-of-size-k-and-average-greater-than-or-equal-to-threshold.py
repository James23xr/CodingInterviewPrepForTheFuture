class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cursum = sum(arr[:k-1])
        for l in range(len(arr)-k+1):
            cursum += arr[l+k-1]
            if (cursum/k) >= threshold:
                res+=1
            cursum -= arr[l]
        return res
        