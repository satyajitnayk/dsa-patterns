# https://www.geeksforgeeks.org/problems/k-largest-elements4206/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)  # Add the new value at the end
        self.heapifyUp(len(self.heap) - 1)  # Move it up to maintain the heap property

    def heapifyUp(self, i):
        # While the inserted element is not the root and is smaller than its parent, swap them
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extractMin(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, just pop it
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.heapifyDown(0)  # Restore the heap property by moving down
        return root

    def heapifyDown(self, i):
        smallest = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        # Check if the left child is smaller than the current node
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        # Check if the right child is smaller than the smallest found so far
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and continue heapifying down
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapifyDown(smallest)

    def getMin(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


class Solution:
    def kLargest(self, arr, n, k):
        minHeap = MinHeap()

        # Build the heap with the first k elements
        for i in range(k):
            minHeap.insert(arr[i])

        # Process the rest of the array
        for i in range(k, n):
            # If the current element is greater than the root of the heap
            if arr[i] > minHeap.getMin():
                minHeap.extractMin()  # Remove the smallest
                minHeap.insert(arr[i])  # Insert the current element

        # Collect k largest elements from the heap
        res = []
        while not minHeap.isEmpty():
            res.append(minHeap.extractMin())

        return res[::-1]  # Return the result in descending order


# Example usage
arr = [12, 5, 787, 1, 23, 8, 99, 55]
n = len(arr)
k = 3
sol = Solution()
print(f"The {k} largest elements are: {sol.kLargest(arr, n, k)}")
