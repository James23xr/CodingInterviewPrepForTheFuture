import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = []
        # Initialize the heap with the first element in nums2 paired with all elements in nums1
        for i in range(min(len(nums1), k)):  # Only need the first k elements from nums1
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        result = []
        # Extract the smallest pairs
        while k > 0 and min_heap:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        return result
        