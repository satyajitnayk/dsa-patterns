class MaxHeap:
    def __init__(self):
        self.heap = []

    # Function to get the parent index
    def parent(self, i):
        return (i - 1) // 2

    # Function to get the left child index
    def leftChild(self, i):
        return 2 * i + 1

    # Function to get the right child index
    def rightChild(self, i):
        return 2 * i + 2

    # Function to insert a new value
    def insert(self, val):
        # Add the new value at the end
        self.heap.append(val)
        # Bubble up to restore the heap property
        self.heapifyUp(len(self.heap) - 1)

    # Function to heapify up (used during insert)
    def heapifyUp(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap parent and current element
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Function to remove and return the maximum element
    def extractMax(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        # Replace the root with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Remove the last element
        # Bubble down to restore the heap property
        self.heapifyDown(0)
        return root

    # Function to heapify down (used during extract)
    def heapifyDown(self, i):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        # Check if left child exists and is greater than current
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if right child exists and is greater than the largest so far
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest element is not the current element
        if largest != i:
            # Swap
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # Recursively heapify down
            self.heapifyDown(largest)

    # Function to get the maximum element
    def getMax(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    # Utility function to print the heap
    def printHeap(self):
        print("Heap:", self.heap)

# Example usage
maxHeap = MaxHeap()
maxHeap.insert(3)
maxHeap.insert(1)
maxHeap.insert(6)
maxHeap.insert(5)
maxHeap.insert(2)
maxHeap.insert(4)

print("Max-Heap after insertion:")
maxHeap.printHeap()

print("Extracted maximum:", maxHeap.extractMax())
maxHeap.printHeap()

print("Extracted maximum:", maxHeap.extractMax())
maxHeap.printHeap()
