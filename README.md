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
  - [Problems by category](#problems-by-category)
    - [Dynamic programming](#dynamic-programming)
    - [Binary Tree Traversal, DFS, BFS](#binary-tree-traversal-dfs-bfs)
    - [Backtracking](#backtracking)
    - [Sliding window](#sliding-window)
    - [Two pointers](#two-pointers)
    - [Binary search](#binary-search)
  - [Meta interview questions](#meta-interview-questions)
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

## My favorite questions (by decending order)

| Name | Difficulty | Description |
|------|------------|-------------|
| 20. Valid Parentheses | Easy | Determine if a string that contains parentheses is valid: "[{()}]". The trick is to use stack. |
| 141. Linked List Cycle | Easy | Find if linked list contains cycle by using fast and slow pointers. |
| 206. Reverse Linked List | Easy | Reverse a linked list in place. Trick: use temporary pointer to the node that we change its links. |
| 1249. Minimum Remove to Make Valid Parentheses | Medium | Use data structure of stack to keep track of open paranthesis. Similar to Leetcode 20. |
| 70. Climbing Stairs | Easy | It should be introduction to dynamic programming. The first dynamic programming question, because it teaches you a lot. |

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

## Problems by category

### Dynamic programming

| Difficulty | Number | Name                           | Main Idea                                                                                                                                      |
|------------|--------|--------------------------------|-----------------------------------------------------------------|
| Easy       | 70     | Climbing Stairs                | This must be the first dynamic programming leetcode question you do. Its quite interesting and simple, yet complex for the first time. |
| Medium     | 300    | Longest Increasing Subsequence | Think about the dynamic programming pattern. This pattern matches the question. dp[i] = longest strickly increasing subsequence of nums[0...i] |

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

General BFS code:

```python
def bfs(root):
    queue = [root]
    while queue:
        curr_level = [] # Populate current level (tree height) with nodes of current height
        for _ in range(len(queue)):
            node = queue.pop(0)
            curr_level.append(node.val) # Instead of node.val you can also do 'node' depending on the question
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # ... do something with curr_level
```

| Difficulty | Name | Main Idea |
|------------|-----------------------------------------------|--------------------|
| Easy       | 257. Binary Tree Paths                        | Simply return paths from root to all leafs in any order, return string. Easy.                                                                                                                                                                                                                                                    |
| Hard       | 124. Binary Tree Maximum Path Sum             | Start from leafs. Consider the base cases first of leafs. Then continue to first parent. Consider to split or not to split the path on that current node. Either take left path or right path (subproblems). My solution was 90% close to the working algorithm. Its ok to look at solutions. Don't waste hours on this problem. |
| Medium     | 2265. Count Nodes Equal to Average of Subtree | Use DFS to traverse the tree. For each node, calculate the sum of the subtree and the number of nodes in the subtree. Then calculate the average of the subtree. |
| Medium     | 1302. Deepest Leaves Sum                      | 2 variables: max level, max level sum. While DFS, update max level (check current height). If current height is equal to max level, add node value to max level sum. |
| Medium     | 102. Binary Tree Level Order Traversal        | Use BFS to traverse the tree. Use a queue to store the current level nodes. Then pop from the queue and add to the result. |

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

| Difficulty | Name |
|------------|------------------------------------------------------------------|
| Medium     | 2958. Length of Longest Subarray With at Most K Frequency        |
| Medium     | 713. Subarray Product Less Than K                                |
| Hard       | 2302. Count Subarrays With Score Less Than K                     |
| Medium     | 2958. Length of Longest Subarray With at Most K Frequency        |
| Medium     | 2962. Count Subarrays Where Max Element Appears at Least K Times |

### Two pointers

We have the two pointers pattern.

1) Either one starts from the beginning and the other from the end.
2) Or both pointers start from the beginning but one pointer moves at faster pace (usually twice as fast) than the other pointer (we call this fast & slow pointers, usually we see this in linked list).

| Difficulty | Name |
|------------|-----------------------------------------------------------------------|
| Easy     | 234. Palindrome Linked List        |

### Binary search

| Difficulty | Name |
|------------|-----------------------------------------------------------------------|
| Medium     | 153. Find Minimum in Rotated Sorted Array        |

## Meta interview questions

| Difficulty | Name | Source |
|------------|--------|------------------------------|
| Medium     | 1249. Minimum Remove to Make Valid Parentheses | [Reddit](https://www.reddit.com/r/leetcode/comments/16zr1sj/meta_ramping_up_hiring_what_to_expect/)

## Interview preparation tips from real Meta recruiter

7 steps to success in your coding interview:

1) Do not jump straight into coding, take a few mins to understand the problem and ask any clarifying questions (but not too long).

2) Describe your solution to your interviewer and get their thoughts on your solution.

3) Think about your algorithm(s) (sorting, divide-and-conquer, recursion...), including the complexity and approximate runtime. Ask the interviewer if it’s ok or if you should think about something more optimized. Then figure out your data structure ((Array, Stack/Queue, Hashset/Hashmap/Hashtable/Dictionary, Tree/Binary Tree, Heap, Graph, Bloom Filter, etc.) and implement.

4) Importantly, after you have finished writing your code, run through it verbally with your interviewer. This is really important at this point. Does it really do what you think it does? Make sure to read what is there, not what you think is there.

5) Test your code, put in an input to see what happens. We’re looking for you to find the bugs yourself and fix anything that comes up

6) Restate the complexity. Is it the same, or different to your initial thinking based on what you have actually coded up? Make sure you’re thinking about both space and time

7) Optimize. Proactively suggest ways to optimize to the interviewer and get their feedback to ensure what you’re trying to do is not overly complex and is correct, then code it up.
