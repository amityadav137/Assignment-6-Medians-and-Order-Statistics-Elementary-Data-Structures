(The full report from the earlier message will be added here to match README)

# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Part 1: Selection Algorithms

### 1. Implementation Overview
This part focuses on implementing two selection algorithms:
- Deterministic Algorithm (Median of Medians): Guarantees worst-case linear time complexity.
- Randomized Algorithm (Randomized Quickselect): Offers expected linear time with better average performance.

Both algorithms are designed to find the kth smallest element in an unsorted list.

### 2. Time Complexity Analysis
- **Deterministic Selection (Median of Medians)**:
  - Time: O(n)
  - Explanation: Recursively partitions the list into groups of five and chooses a good pivot.

- **Randomized Quickselect**:
  - Time: O(n) expected, O(n²) worst
  - Explanation: Uses a randomly chosen pivot.

### 3. Space Complexity
- Median of Medians: O(n)
- Quickselect: O(1) auxiliary space (in-place)

### 4. Empirical Comparison
- Test on arrays of sizes 100, 1000, and 10000 with different distributions.
- Quickselect is generally faster, but Median of Medians is more stable in worst-case conditions.

## Part 2: Elementary Data Structures

### 1. Implemented Structures
- Array and Matrix: Basic insert, delete, access
- Stack and Queue using list
- Singly Linked List with insertion, deletion, traversal

### 2. Time Complexity
| Structure | Operation           | Time    |
|-----------|---------------------|---------|
| Array     | Access              | O(1)    |
|           | Insert/Delete (end) | O(1)    |
| Stack     | Push/Pop            | O(1)    |
| Queue     | Enqueue/Dequeue     | O(1)    |
| LinkedList| Insert/Delete Head  | O(1)    |
| Matrix    | Access              | O(1)    |

### 3. Applications
- Stack: Undo systems, expression evaluation
- Queue: Scheduling tasks, print queues
- Linked List: Dynamic memory applications
- Matrix: 2D grids, games, numerical computations

### Conclusion
This assignment demonstrates practical and theoretical understanding of order statistics and foundational data structures through hands-on implementation and analysis.