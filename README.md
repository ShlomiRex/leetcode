# leetcode
My solutions to leet code questions. Includes cheat sheet of code for common patterns.

The questions & solutions are also orginized in tables by pattern category.

## Table of Contents

- [leetcode](#leetcode)
  - [Table of Contents](#table-of-contents)
  - [Problem solving](#problem-solving)
  - [Cheat Sheet / Common Patterns](#cheat-sheet--common-patterns)
  - [Common Interview Questions](#common-interview-questions)
  - [Must know questions before an interview](#must-know-questions-before-an-interview)
  - [My favorite questions (by decending order)](#my-favorite-questions-by-decending-order)
  - [Common Leetcode Patterns](#common-leetcode-patterns)
  - [Python tricks](#python-tricks)
  - [Problems by pattern / category](#problems-by-pattern--category)
    - [Dynamic programming](#dynamic-programming)
    - [Binary Tree Traversal, DFS, BFS](#binary-tree-traversal-dfs-bfs)
    - [Backtracking](#backtracking)
    - [Sliding window](#sliding-window)
    - [Two pointers](#two-pointers)
    - [Binary search](#binary-search)
    - [Matrix](#matrix)
    - [Stack](#stack)
    - [Hashmap / Hashset](#hashmap--hashset)
    - [Memorization](#memorization)
    - [Prefix pattern](#prefix-pattern)
    - [Bit manipulation](#bit-manipulation)
    - [Heap/Priority Queue](#heappriority-queue)
  - [Meta interview questions](#meta-interview-questions)
    - [Dinosour Question](#dinosour-question)
  - [Interview preparation tips from real Meta recruiter](#interview-preparation-tips-from-real-meta-recruiter)

## Problem solving

The best way to solve leetcode is first to consider the brute force approach. Then, think about how you can optimize it. If you can't think of anything or can't implement it, try to look at the solution. Don't try to solve it. This is the best way to learn leetcode patterns.

## Cheat Sheet / Common Patterns

| Name                                | Trick                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Contitinous subarray | Every time we see 'continious subarray' always think about the sliding window technique. |
| Fast & Slow pointers | Usually we see this in linked list. Slow pointer (moves 1 node at a time) and fast pointer (moves 2 nodes at a time). When fast pointer reaches the end of the linked list, the slow pointer is at middle point. Its also used to check if the linked-list is cyclic (if both pointers meet). |
| Parenthesis questions | Usually, parenthesis question requires the use of a stack. For example, checking if string has valid parenthesis, inserting into the stack open parenthesis, popping from the stack if found closing parenthesis. Check size of stack at the end.|
| Depth First Search (DFS) recursive  | Store a set of visited nodes. For each node, set 'visited'. For each child check if not visited, then call DFS on it. |
| DFS recursive - find maximum depth  | We return (1 + max(DFS(left), DFS(right)))                                                                            |
| Breadth First Search (BFS) recursive | Use a queue that is populated with current level nodes. Then pop from head of queue a node and call BFS on it.        |
| In-place merge sorted arrays | Given array nums1 and we want to merge with nums2 in non-desending order, we can traverse BACKWARDS in order to not overwrite the nums1 array. It contains '0' (zeroes) at the end so we can overwrite those. |

## Common Interview Questions

* Leetcode Blind 75 with notes: [here](https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit#gid=0)
* DFS, BFS, recursive
* DFS, BFS, iterative
* Two Sum variations
* Max sub array (kadane's algo)
* Reverse a linked list

## Must know questions before an interview

| Difficulty | Name | Description |
|------------|------|-------------|
| Medium | 215. Kth Largest Element in an Array | Can sort array and return `nums[len(nums)-k]` which is O(nlogn) or we can use max-heap (populate max-heap in O(1), then pop K roots, and the result is the k'th largest) |
| Easy | 1. Two Sum | Use hashmap to remember if a specific number is present in the current array. Do calculation: `target - nums[i]` check if this exists in the hashmap / hashset / set. Time complexity: O(n) one pass. |
| Easy | 206. Reverse Linked List | Use `prev`, `cur` pointers (sometimes I also use `next` pointer) to correctly point and change the linked list. |
| Medium | 167. Two Sum II - Input array is sorted | Use two pointers, one at the beginning and one at the end. If the sum is greater than the target, move the right pointer to the left. If the sum is less than the target, move the left pointer to the right. |

## My favorite questions (by decending order)

| Name | Difficulty | Description |
|------|------------|-------------|
| 20. Valid Parentheses | Easy | Determine if a string that contains parentheses is valid: "[{()}]". The trick is to use stack. |
| 141. Linked List Cycle | Easy | Find if linked list contains cycle by using fast and slow pointers. |
| 206. Reverse Linked List | Easy | Reverse a linked list in place. Trick: use temporary pointer to the node that we change its links. |
| 200. Number of Islands | Medium | Use DFS to traverse the matrix. For each cell, check if cell is land and mark it. Then call DFS on its neighbors. |
| 62. Unique Paths | Medium | Use dynamic programming to solve the problem. The number of ways to reach a cell is the sum of the number of ways to reach the cell above and the cell to the left. |
| 1249. Minimum Remove to Make Valid Parentheses | Medium | Use data structure of stack to keep track of open paranthesis. Similar to Leetcode 20. |
| 416. Partition Equal Subset Sum | Medium | Use backtracking. For each number, we can choose to add it to the subset or not. We keep track of all possible sums and check if we found target. Meta love this question. |
| 70. Climbing Stairs | Easy | It should be introduction to dynamic programming. The first dynamic programming question, because it teaches you a lot. |
| 129. Sum Root to Leaf Numbers | Medium | Use DFS to traverse the tree. For each node, calculate the sum of the path from the root to the current node. |
| 623. Add One Row to Tree | Medium | Use DFS to traverse the tree. For each node, check if the current level is equal to the target level. If it is, add the new nodes to the tree. |

## Common Leetcode Patterns

| Pattern                | Description                                                                                                                                 |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Sliding Window         | Used for array or string problems where a subarray or substring meets a certain condition. The window changes size or slides based on certain conditions. |
| Two Pointers           | Used in arrays or linked lists to iterate through the structure with two pointers at different speeds or positions, often to find pairs summing to a target. |
| Fast and Slow Pointers | A specific case of the two pointers technique, used especially in cycle detection problems in linked lists or arrays.                       |
| DFS (Depth-First Search)| A traversal algorithm that goes as deep as possible down one path before backtracking. Useful for tree, graph, and some combination problems. |
| BFS (Breadth-First Search)| A traversal algorithm that explores all the neighbors of a node before moving to the next level neighbors. Used in shortest path, tree, and graph problems. |
| Binary Search          | Used in sorted arrays or matrices to reduce the search space by half at every step, finding a target value more efficiently.                 |
| Dynamic Programming    | Solving complex problems by breaking them down into simpler subproblems, storing the results of these subproblems to avoid redundant work.    |
| Backtracking           | A form of recursion that involves choosing options at each step and backtracking when a path doesn't lead to a solution, often used in permutation, combination, and partitioning problems. |
| Heap/Priority Queue    | Often used in problems involving sorting, and to efficiently keep track of the kth largest/smallest element in a stream or collection.       |
| 2D Dynamic Programming | As soon as you hear 'minimize' or 'maximize' in a matrix, thats 2D dynamic programming in most cases. |

## Python tricks

1. Find substring with `find()` function.
2. Find substring, starting from the right with `rfind()` function.
3. Reverse array: `arr.reverse()`
4. Reverse string or array: `str_or_arr[::-1]` which is slice from beginning to end with negative step (so it reverses).
5. Deep copy array: `deep_copy = my_arr[:]`, that means `id(deep_copy) != id(my_arr)` which is different memory address (truly copy). You can change one and not affect the other.
6. The lookup runtime of `set()` is O(1), so you can ask: `if num in my_set` and it takes O(1). Under the hood it uses a hash table.
7. Max-heap insertion time complexity (average): O(1), worst case: O(log n), pop root (maximum element in the heap) time complexity: O(log n). Code:

    ```python
    import heapq
    heap = [] # Empty list to represent the heap
    heapq.heappush(heap, 5) # Adding elements to the heap
    max_element = heap[0] # Peek max element without removing
    max_element = heapq.heappop(heap) # Remove and return the maximum element
    ```

8. Insert text into string between two indexes: `str[:start_index] + text + str[end_index:]`

9. For matrix problems, instead of keeping track of visited cells, we can modify the matrix itself (if we can) and mark visited cells with a special character. Only works if the cells values are specific range/values.

## Problems by pattern / category

### Dynamic programming

| Difficulty | Name                                      | Main Idea |
|------------|-------------------------------------------|-----------------------------------------------------------------|
| Easy       | 70. Climbing Stairs                       | This must be the first dynamic programming leetcode question you do. Its quite interesting and simple, yet complex for the first time. |
| Medium     | 300. Longest Increasing Subsequence       | Think about the dynamic programming pattern. This pattern matches the question. dp[i] = longest strickly increasing subsequence of nums[0...i] |
| Medium     | 62. Unique Paths                          | Use dynamic programming to solve the problem. The number of ways to reach a cell is the sum of the number of ways to reach the cell above and the cell to the left. |
| Medium     | 63. Unique Paths II                       | Similar to Unique Paths, but with obstacles. Use dynamic programming to solve the problem. |
| Medium     | 2370. Longest Ideal Subsequence           | The longest ideal subsequence is the longest subsequence where the difference between adjacent elements is 1. Very, very hard question. |
| Hard       | 1289. Minimum Falling Path Sum II         | For each row, calculate the minimum falling path sum. Use DP matrix for faster calculation. The 2D-DP solution is not hard for this question. |

### Binary Tree Traversal, DFS, BFS

In DFS we usually recursivly go left, right and only then we write code to deal with the leafs first:

```python
def dfs(root):
    if not root:
        return
    # ... do something here
    dfs(root.left)
    dfs(root.right)
    # ... do something here (usually leafs)
```

General BFS code for binary tree:

```python
def bfs(root):
    queue = [root]
    while queue:
        curr_level = [] # Populate current level (tree height) with nodes of current height
        for _ in range(len(queue)):
            node = queue.pop(0)
            curr_level.append(node.val) # Instead of node.val you can also do 'node' depending on the question
            # Append children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # ... do something with curr_level
```

General BFS code for graph:

```python
def bfs(root) -> int:
    queue = [(root, 0, None)] # Current node, it's level, and parent
    while queue:
        curr, level, parent = queue.pop(0)
        print(f"Node: {curr}, level: {level}")
        # Where graph is hashmap of adjacency list (graph[u] = [v1, v2, ...] and graph[v1] = [u1, u2, ...])
        for child in graph[curr]:
            # Instead of visited set we keep track of parent (better memory complexity)
            if child != parent:
                queue.append((child, level+1, curr))
```

| Difficulty | Name | Main Idea |
|------------|-----------------------------------------------|--------------------|
| Easy       | 257. Binary Tree Paths                        | Simply return paths from root to all leafs in any order, return string. Easy.                                                                                                                                                                                                                                                    |
| Hard       | 124. Binary Tree Maximum Path Sum             | Start from leafs. Consider the base cases first of leafs. Then continue to first parent. Consider to split or not to split the path on that current node. Either take left path or right path (subproblems). My solution was 90% close to the working algorithm. Its ok to look at solutions. Don't waste hours on this problem. |
| Medium     | 2265. Count Nodes Equal to Average of Subtree | Use DFS to traverse the tree. For each node, calculate the sum of the subtree and the number of nodes in the subtree. Then calculate the average of the subtree. |
| Medium     | 1302. Deepest Leaves Sum                      | 2 variables: max level, max level sum. While DFS, update max level (check current height). If current height is equal to max level, add node value to max level sum. |
| Medium     | 102. Binary Tree Level Order Traversal        | Use BFS to traverse the tree. Use a queue to store the current level nodes. Then pop from the queue and add to the result. |
| Easy       | 404. Sum of Left Leaves                       | Use DFS to traverse the tree. For each node, check if it is a left leaf. If it is, add its value to the result. |
| Medium     | 129. Sum Root to Leaf Numbers                 | Use DFS to traverse the tree. For each node, calculate the sum of the path from the root to the current node. |
| Easy       | 112. Path Sum                                 | Use DFS to traverse the tree. For each node, subtract the node value from the target sum and call DFS on its children. OR have cumulative sum and check if equal to target. |
| Medium     | 623. Add One Row to Tree                      | Use DFS to traverse the tree. For each node, check if the current level is equal to the target level. If it is, add the new nodes to the tree. |
| Medium     | 988. Smallest String Starting From Leaf       | Use DFS to traverse the tree. For each node, calculate the string formed by the path from the root to the current node. Return the smallest string lexigraphically. |
| Easy       | 463. Island Perimeter                         | Use DFS to traverse the grid. For each cell, check if it is land. If it is, add the perimeter of the cell to the result. Just like number of islands. Use DFS to flood fill. |
| Easy       | 1971. Find if Path Exists in Graph            | General graph question (not binary tree). Use BFS to traverse the graph. For each node, check if it is the target node. If it is, return True. Else, add its neighbors to the queue. Keep track of visited nodes to avoid loops. |
| Medium     | 752. Open the Lock                            | Use BFS and a queue to traverse the graph. For each node, generate the next possible nodes and add them to the queue. No optimization can be done here, very hard question without hints. |
| Medium     | 310. Minimum Height Trees                     | Remove leafs from the tree until there are 1 or 2 nodes left. The remaining nodes are the root of the minimum height trees. Use BFS to remove leafs in batches. |
| Hard       | 834. Sum of Distances in Tree                 | Brute force BFS is fine but we get time limit exceeded. So we use special formula: `res[child] = res[parent] - count[child] + (N - count[child])` where `count[child]` is the number of nodes in the subtree rooted at child. |
| Medium     | 994. Rotting Oranges                          | Use BFS to traverse the grid. For each cell, check if it is a rotten orange. If it is, add it to the queue. Then, for each rotten orange, rot its neighbors in BFS manner (add to new queue and replace current queue with this new queue). Count steps needed to rot all oranges. Return -1 if not all oranges are rotten. |
| Easy       | 100. Same Tree                                | Use DFS to traverse the trees. For each node, check if the nodes are equal and exist. If they are, call DFS on their children. |
| Easy       | 111. Minimum Depth of Binary Tree             | Use DFS and find the minimum depth of the tree. For each node, calculate the minimum depth of the left and right subtrees. |
| Easy       | 226. Invert Binary Tree                       | Recursivly call `leftSubtree = invertTree(root.left)` and `rightSubtree = invertTree(root.right)` and swap: `root.left = rightSubtree` and `root.right = leftSubtree`. If root is None, return None. |

### Backtracking

In backtracking we think decision tree. Each step we choose to do something. We usually have a function that we call (once or more), usually recursivly. Its like iterating the tree and adding to the result, then returning the result.

* For each element, we have two choices: either pick the element or don't pick it (for example).
* At each level of the recursive tree, we make a choice for each subsequent element as we traverse down the tree.

It look something like:

```python
res = []
def backtrack(curr_solution, constraints):
    res.append(curr_solution)
    backtrack(curr_solution[:] + [choice], constraints)
backtrack([], constraints)
return res
```

Notice instead of appending to `curr_solution` we use deep copy, because `curr_solution` pointer can be accessed and modified multiple times. Its safer this way.

| Difficulty | Number | Name                         | Main Idea                                                                                                                                                                                                                                                                                                                        |
|------------|--------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Medium     | 22     | Generate Parentheses         | Its like a decision tree: each time we either add '(' or ')' such that the string matches valid parentheses. We use DFS to walk from top to bottom to the leafs, and add the leafs to the final solution. The solution is quite elegant, like 10 lines of code.|
| Medium     | 78     | Subsets         | We can choose to add an element to be added to subset or not. I use index to tell what elements to add to the subset (all elements to the left of the index are already added). |
| Medium     | 416    | Partition Equal Subset Sum   | We can choose to add an element to the subset or not. We store all the sums we have. For each num in nums, we add it to the possible sums. |
| Medium     | 39     | Combination Sum              | We start with brute force decision tree. But we want to remove duplicates (order doesn't matter), so we choose index 'i' of candidates that we can choose from. This eliminates duplicates. |

### Sliding window

The trick for sliding window is to use left, right pointers that represent the current window (think about sub-arrays). It look something like this:

```python
l, r = 0, 0
while r < len(arr):
    if <some condition>:
        r += 1
    else:
        l += 1
```

Sometimes we want to increase the left pointer until we reach a rule:

```python
while r < len(arr):
    while <some condition>:
        l += 1
    r += 1
```

You can use sliding window to get all substrings of given string:

```python
def all_substrings(s):
    substrings = []
    n = len(s)
    
    for window_size in range(1, n + 1):
        for start in range(n - window_size + 1):
            end = start + window_size
            substrings.append(s[start:end])
    
    return substrings
```

| Difficulty | Name | Description |
|------------|------------------------------------------------------------------|------------------|
| Medium     | 2958. Length of Longest Subarray With at Most K Frequency        |                  |
| Medium     | 713. Subarray Product Less Than K                                |                  |
| Hard       | 2302. Count Subarrays With Score Less Than K                     |                  |
| Medium     | 2958. Length of Longest Subarray With at Most K Frequency        |                  |
| Medium     | 2962. Count Subarrays Where Max Element Appears at Least K Times |                  |
| Easy       | 121. Best Time to Buy and Sell Stock                             | Buy and sell stock problem. Use sliding window to find the minimum price and maximum profit. We don't increment left pointer, we set it to minimum price. |

### Two pointers

We have the two pointers pattern.

1) Either one starts from the beginning and the other from the end.
2) Or both pointers start from the beginning but one pointer moves at faster pace (usually twice as fast) than the other pointer (we call this fast & slow pointers, usually we see this in linked list).

| Difficulty | Name | Description |
|------------|----------|----------|
| Easy     | 234. Palindrome Linked List        | |
| Medium   | 151. Reverse Words in a String | Using two-pointers is quite complex. But we can solve with min/max heap. |
| Medium   | 443. String Compression | Use two pointers to compress the string. |
| Easy     | 680. Valid Palindrome II | Use two pointers to check if the string is a palindrome. If the characters at the two pointers are not equal, check if the string is a palindrome by removing one of the characters. This is not quite easy. |
| Medium   | 167. Two Sum II - Input array is sorted | Use two pointers, one at the beginning and one at the end. If the sum is greater than the target, move the right pointer to the left. If the sum is less than the target, move the left pointer to the right. |
| Medium   | 15. 3Sum | Use two pointers to find the sum of three numbers that is equal to the target. Sort the array first. For each number, use two pointers to find the sum of the other two numbers. |

### Binary search

General code for binary search:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: # Check if target is present at mid
            return mid
        elif arr[mid] < target: # If target is greater, ignore left half
            left = mid + 1
        else: # If target is smaller, ignore right half
            right = mid - 1
    return -1 # If target is not present in array
```

| Difficulty | Name |
|------------|-----------------------------------------------------------------------|
| Medium     | 153. Find Minimum in Rotated Sorted Array        |

### Matrix

Usually in matrix questions, we convert the question to a graph problem. Then we can use DFS/BFS to traverse the matrix.

| Difficulty | Name | Description |
|------------|------|----------------------------------------------------------------|
| Medium | 79. Word Search | Use DFS to traverse the matrix. For each cell, check if the word can be found starting from that cell. Can be optimized by marking current cell as visited.|
| Medium | 200. Number of Islands | Use DFS to traverse the matrix. For each cell, check if the cell is land. If it is, mark it as visited and call DFS on its neighbors. Classic problem. |
| Medium | 1992. Find All Groups of Farmland | Use DFS to traverse the matrix. For each cell, check if the cell is land. If it is, mark it as visited and call DFS on its neighbors. Or just use regular for loops to traverse matrix, this is faster. |

### Stack

General code for stack in python:

```python
stack = []
stack.append(1) # Push
stack.pop() # Pop
```

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Easy | 1614. Maximum Nesting Depth of the Parentheses | Use stack to keep track of open paranthesis. For each open paranthesis, push to stack. For each closing paranthesis, pop from stack. Optimize without the use of stack, just O(1) auxulary space. |
| Easy | 1544. Make The String Great | Use stack to keep track of characters. For each character, check if the stack is empty. If not, check if the current character is the same (uppercase or lower case) as the top of the stack. If it is, pop from the stack. Otherwise, push the character to the stack. |

### Hashmap / Hashset

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Easy | 242. Valid Anagram | Use hashmap to keep track of the frequency of each character in the string. For each character in the first string, increment the frequency. For each character in the second string, decrement the frequency. If the frequency is not zero, return False. Otherwise, return True. |

### Memorization

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Easy | 1137. N-th Tribonacci Number | Use memorization to store the results of the subproblems. For each number, calculate the sum of the previous three numbers. We can also optimize, and use only 3 variables instead of a whole array. |


### Prefix pattern

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium | 560. Subarray Sum Equals K | We take the brute force approach O(n^2) and optimize it. Use prefix sum to calculate the sum of the subarray. For each subarray, calculate the sum of the subarray. If the sum is equal to the target, increment the count. |
| Medium | 1915. Number of Wonderful Substrings | Similar to prefix sum we have prefix bitmasks XOR. |

### Bit manipulation

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium | 1915. Number of Wonderful Substrings | Use prefix bitmasks XOR to calculate the XOR of the subarray. For each subarray, calculate the XOR of the subarray. If the XOR is a power of 2, increment the count. |

### Heap/Priority Queue

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium     | 692. Top K Frequent Words | Use max-heap to keep track of the frequency of each word. For each word, increment the frequency. Then, for each word in the frequency hashmap, add it to the max-heap. Pop the top K elements from the max-heap. |
| Medium     | 215. Kth Largest Element in an Array | Use max-heap to keep track of the K largest elements. For each element, add it to the max-heap. Pop the top element from the max-heap K times. |

## Meta interview questions

| Difficulty | Name | Source |
|------------|--------|------------------------------|
| Medium     | 1249. Minimum Remove to Make Valid Parentheses | [Reddit](https://www.reddit.com/r/leetcode/comments/16zr1sj/meta_ramping_up_hiring_what_to_expect/) |
| Medium     | 560. Subarray Sum Equals K | |

### Dinosour Question

You will be supplied with two data files in CSV format.

The first file contains statistics about various dinosaurs. The second file contains additional data.

Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)

Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.

Do not print any other information.

```
$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv 
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal
```

Possible solution:
```python
import csv
from math import sqrt

# Read data from dataset1.csv and dataset2.csv
def read_data(file_path):
    data = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['NAME']] = row
    return data

dataset1 = read_data("dataset1.csv")
dataset2 = read_data("dataset2.csv")

# Calculate speed for bipedal dinosaurs
g = 9.8  # gravitational constant

bipedal_dinosaurs = []
for name in dataset1:
    if name in dataset2 and dataset2[name]['STANCE'] == 'bipedal':
        leg_length = float(dataset1[name]['LEG_LENGTH'])
        stride_length = float(dataset2[name]['STRIDE_LENGTH'])
        speed = ((stride_length / leg_length) - 1) * sqrt(leg_length * g)
        bipedal_dinosaurs.append((name, speed))

# Sort bipedal dinosaurs by speed
bipedal_dinosaurs.sort(key=lambda x: x[1], reverse=True)

# Print names of bipedal dinosaurs from fastest to slowest
for dinosaur in bipedal_dinosaurs:
    print(dinosaur[0])
```

## Interview preparation tips from real Meta recruiter

7 steps to success in your coding interview:

1) Do not jump straight into coding, take a few mins to understand the problem and ask any clarifying questions (but not too long).

2) Describe your solution to your interviewer and get their thoughts on your solution.

3) Think about your algorithm(s) (sorting, divide-and-conquer, recursion...), including the complexity and approximate runtime. Ask the interviewer if it’s ok or if you should think about something more optimized. Then figure out your data structure ((Array, Stack/Queue, Hashset/Hashmap/Hashtable/Dictionary, Tree/Binary Tree, Heap, Graph, Bloom Filter, etc.) and implement.

4) Importantly, after you have finished writing your code, run through it verbally with your interviewer. This is really important at this point. Does it really do what you think it does? Make sure to read what is there, not what you think is there.

5) Test your code, put in an input to see what happens. We’re looking for you to find the bugs yourself and fix anything that comes up

6) Restate the complexity. Is it the same, or different to your initial thinking based on what you have actually coded up? Make sure you’re thinking about both space and time

7) Optimize. Proactively suggest ways to optimize to the interviewer and get their feedback to ensure what you’re trying to do is not overly complex and is correct, then code it up.
