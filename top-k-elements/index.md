A **heap** is a specialized tree-based data structure that satisfies the **heap property**. It is commonly used to efficiently perform operations like finding the minimum or maximum element in a dataset. Heaps are most often implemented using a binary tree structure and can be classified into two main types:

### Types of Heaps:

1. **Min-Heap**:
   - **Heap Property**: The value of each node is **greater than or equal** to the value of its parent.
   - **Root**: The root node has the **smallest** value in the heap.
   - **Example**: If you need to efficiently extract the minimum element from a dynamic set of numbers, a min-heap is used.
2. **Max-Heap**:
   - **Heap Property**: The value of each node is **less than or equal** to the value of its parent.
   - **Root**: The root node has the **largest** value in the heap.
   - **Example**: If you need to efficiently extract the maximum element, a max-heap is used.

### Key Characteristics:

- **Complete Binary Tree**: Heaps are typically implemented as complete binary trees, meaning all levels of the tree are fully filled except possibly the last, which is filled from left to right.
- **Array Representation**: Heaps can be efficiently represented using arrays, where:
  - The root is at index `0`.
  - For a node at index `i`:
    - The **left child** is at index `2i + 1`.
    - The **right child** is at index `2i + 2`.
    - The **parent** is at index `(i - 1) // 2`. (Floor operator, ex: 5 // 2 = 2, 9 // 4 = 2,...)

### Operations on a Heap:

1. **Insert (Push)**:

   - Insert a new element at the end of the heap and then "bubble up" (or "heapify up") the element to restore the heap property.
   - **Time complexity**: O(log n), where `n` is the number of elements.

2. **Extract (Pop)**:

   - Remove the root element (minimum in min-heap or maximum in max-heap) and replace it with the last element.
   - Then "bubble down" (or "heapify down") the new root to restore the heap property.
   - **Time complexity**: O(log n).

3. **Peek**:

   - Access the root element without removing it (i.e., the minimum element in a min-heap or the maximum in a max-heap).
   - **Time complexity**: O(1).

4. **Heapify**:
   - Build a heap from an unsorted array by iterating through the array and applying the heap property.
   - In a heap, the leaf nodes (nodes without children) are always valid by themselves since they do not have children to violate the heap property. Therefore, we don't need to apply the heapifyDown process to leaf nodes. Instead, we only need to apply it to internal nodes (nodes that have at least one child), starting from the last internal node and moving up towards the root.
   - **Time complexity**: O(n) for heap creation.

### Applications of Heaps:

1. **Priority Queues**: A priority queue can be implemented using a heap, where the highest (or lowest) priority element is always at the root, allowing for efficient access to it.
2. **Heap Sort**: A comparison-based sorting algorithm that uses a heap to sort elements in O(n log n) time. This is done by repeatedly extracting the root of the heap and placing it at the end of the array.
3. **Finding Top K Elements**: Heaps are used to maintain the top K largest or smallest elements in a dataset, especially in problems where you need to find the Kth largest or smallest number efficiently.
4. **Graph Algorithms**: Heaps are used in algorithms like **Dijkstra's Shortest Path** and **Prim's Minimum Spanning Tree**, where priority queues are needed to select the next node with the smallest edge weight.

### Example of Min-Heap:

For the array `[3, 2, 15, 5, 4, 45]`:

1. **Heap Construction**:
   ```
       2
      / \
     3   15
    / \   /
   5   4 45
   ```
   - The root (`2`) is the minimum element in this min-heap.

### Conclusion:

Heaps are highly efficient for dynamic datasets where you need quick access to the smallest or largest element. The heap's ability to efficiently insert and extract elements with O(log n) time complexity makes it a popular choice for various computational problems.
