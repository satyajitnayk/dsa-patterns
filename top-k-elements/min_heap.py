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
    # Add the new value at the end
    self.heap.append(val);
    # Bubble up to restore the heap property
    self.heapifyUp(len(self.heap) - 1)

  def heapifyUp(self, i):
    while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
      # Swap parent and current element
      self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
      i = self.parent(i)

  # Function to remove and return the minimum element
  def extractMin(self):
    if len(self.heap) == 0:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    # Replace the root with the last element
    root = self.heap[0]
    self.heap[0] = self.heap.pop() # remove last element
    # Bubble down to restore the heap property
    self.heapifyDown(0)
    return root

  def heapifyDown(self, i):
    smallest = i
    left = self.leftChild(i)
    right = self.rightChild(i)

    # Check if left child exists and is smaller than current
    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
      smallest = left

    # Check if right child exists and is smaller than the smallest so far
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
      smallest = right

    # If the smallest element is not the current element
    if smallest != i:
      # swap
      self.heap[i], self.heap[smallest] =  self.heap[smallest], self.heap[i]
      # Recursively heapify down
      self.heapifyDown(smallest)

  # heapify method that converts an entire unsorted array into a heap, 
  # we need to iterate through the non-leaf nodes in reverse order 
  # (from the middle of the array) and apply heapifyDown to each one. 
  # This efficiently builds a valid Min-Heap in 𝑂(𝑛) time
  def heapify(self, arr):
    # Initialize the heap with the array elements
    self.heap = arr[:]
    # Start from the first non-leaf node and apply heapify down
    for i in range(len(self.heap) // 2 - 1, -1, -1):
      self.heapifyDown(i)

  def getMin(self):
    if len(self.heap) == 0:
      return None
    return self.heap[0]

  def printHeap(self):
    print("Heap:", self.heap)


# usage example
minHeap = MinHeap()
minHeap.heapify([3,1,6,5,2,4])
# minHeap.insert(3)
# minHeap.insert(1)
# minHeap.insert(6)
# minHeap.insert(5)
# minHeap.insert(2)
# minHeap.insert(4)



print("Min-Heap after insertion:")
minHeap.printHeap()

print("Extracted minimum:", minHeap.extractMin())
minHeap.printHeap()

print("Extracted minimum:", minHeap.extractMin())
minHeap.printHeap()