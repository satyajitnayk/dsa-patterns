# Build a min-heap of size k by adding elements and replacing the root 
# (smallest) if new elements are larger. After processing all elements, 
# the root of the heap holds the kth largest element.

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        for i in range(k,len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return minHeap[0]

arr = [3, 2, 1, 5, 6, 4]
k = 2
sol = Solution()
print(f"The {k}th largest element is: {sol.findKthLargest(arr, k)}")

# Time complexity: O(k) for hepify + (n-k)O(log k) = O(n log k)