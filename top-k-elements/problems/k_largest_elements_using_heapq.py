# https://www.geeksforgeeks.org/problems/k-largest-elements4206/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
import heapq

class Solution:
    def kLargest(self, arr, n, k):
        # Initialize a min heap with the first k elements
        minHeap = arr[:k]
        heapq.heapify(minHeap)  # O(k) time to build a heap
        
        # Process the remaining elements in the array
        for i in range(k, n):
            if arr[i] > minHeap[0]:  # Compare with the smallest element in the heap
                heapq.heappop(minHeap)  # Remove the smallest element
                heapq.heappush(minHeap, arr[i])  # Push the current element into the heap
        
        # The heap contains the k largest elements in min-heap order
        return sorted(minHeap, reverse=True)  # Sort in descending order

# Example usage
arr = [12, 5, 787, 1, 23, 8, 99, 55]
n = len(arr)
k = 3
sol = Solution()
print(f"The {k} largest elements are: {sol.kLargest(arr, n, k)}")
