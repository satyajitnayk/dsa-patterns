# To solve the "347. Top K Frequent Elements" problem, we need to find the k most frequent elements in a given list of integers. Here’s a concise breakdown of the logic and steps to achieve this:

# ### Steps:

# 1. **Count Frequencies**:
#    - Use a dictionary or `collections.Counter` to count the frequency of each element in the list.

# 2. **Use a Min-Heap**:
#    - To efficiently retrieve the k most frequent elements, use a min-heap (or priority queue). The min-heap will store the elements based on their frequencies.
#    - The heap will help us maintain the top k elements efficiently. The heap size will not exceed k, so when we encounter an element with a frequency higher than the smallest in the heap, we can pop the smallest and insert the new element.

# 3. **Extract the Results**:
#    - After processing all elements, the heap will contain the k most frequent elements. Since the heap is a min-heap, you can extract elements from it to get the result.

# ### Complexity:
# - **Time Complexity**: O(N log k), where N is the number of elements in the input list. This is because inserting into and removing from the heap (which can hold up to k elements) takes O(log k).
# - **Space Complexity**: O(N) for storing the frequency count.


from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        freq_map = Counter(nums)

        # Use a min-heap to store the k most frequent elements
        min_heap = []

        # Build the heap
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))  # Push (frequency, number) into the heap
            # If the heap exceeds size k, remove the smallest frequency element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract the numbers from the heap
        return [num for freq, num in min_heap]

# Example usage
solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]

# ### Explanation of the Code:
# 1. **Counting Frequencies**: `Counter(nums)` creates a dictionary-like object where keys are elements and values are their respective counts.
# 2. **Building the Min-Heap**:
#    - For each unique number and its frequency, we push it into the heap.
#    - If the size of the heap exceeds k, we pop the smallest frequency element to maintain only the k most frequent elements.
# 3. **Returning Results**: Finally, we extract the numbers from the heap to return the top k frequent elements.

# This approach efficiently handles the problem while adhering to the constraints typically present in coding challenges.