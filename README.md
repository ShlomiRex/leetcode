# leetcode
My solutions to leet code questions. Includes cheat sheet of code for common patterns.

The questions & solutions are also orginized in tables by pattern category.

## Table of Contents

- [leetcode](#leetcode)
  - [Table of Contents](#table-of-contents)
  - [Interview stages cheat sheet](#interview-stages-cheat-sheet)
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
    - [Linked List](#linked-list)
    - [Subsets](#subsets)
  - [Meta interview questions](#meta-interview-questions)
    - [Dinosour Question](#dinosour-question)
    - [Network Production Engineer Meta May 2024 - Coding Round - Q1](#network-production-engineer-meta-may-2024---coding-round---q1)
    - [Network Production Engineer Meta May 2024 - Coding Round - Q2](#network-production-engineer-meta-may-2024---coding-round---q2)
    - [Production Engineer Meta - Prep Material - Example Q1](#production-engineer-meta---prep-material---example-q1)
  - [Interview preparation tips from real Meta recruiter](#interview-preparation-tips-from-real-meta-recruiter)

## Interview stages cheat sheet

**Stage 1: Introductions**

* Have a rehearsed 30-60 second introduction regarding your education, work experience, and interests prepared.
* Smile and speak with confidence.
* Pay attention when the interviewer talks about themselves and incorporate their work into your questions later.

**Stage 2: Problem statement**

* Paraphrase the problem back to the interviewer after they have read it to you.
* Ask clarifying questions about the input such as the expected input size, edge cases, and invalid inputs.
* Quickly walk through an example test case to confirm you understand the problem.

**Stage 3: Brainstorming DS&A**

* Always be thinking out loud.
* Break the problem down: figure out what you need to do, and think about what data structure or algorithm can accomplish it with a good time complexity.
* Be receptive to any comments or feedback from the interviewer, they are probably trying to hint you towards the correct solution.
* Once you have an idea, before coding, explain your idea to the interviewer and make sure they understand and agree that it is a reasonable approach.

**Stage 4: Implementation**

* Explain your decision-making as you implement. When you declare things like sets, explain what the purpose is.
* Write clean code that conforms to your programming language's conventions.
* Avoid writing duplicate code - use a helper function or for loop if you are writing similar code multiple times.
* If you are stuck, don't panic - communicate your concerns with your interviewer.
* Don't be scared to start with a brute force solution (while acknowledging that it is brute force), then improve it by optimizing the "slow" parts.
* Keep thinking out loud and talk with your interviewer. It makes it easier for them to give you hints.

**Stage 5: Testing & debugging**

* When walking through test cases, keep track of the variables by writing at the bottom of the file, and continuously update them. Condense trivial parts like creating a prefix sum to save time.
* If there are errors and the environment supports running code, put print statements in your algorithm and walk through a small test case, comparing the expected value of variables and the actual values.
* Be vocal and keep talking with your interviewer if you run into any problems.

**Stage 6: Explanations and follow-ups**

Questions you should be prepared to answer:

* Time and space complexity, average and worst case.
* Why did you choose this data structure, algorithm, or logic?
* Do you think the algorithm could be improved in terms of complexity? If they ask you this, then the answer is usually yes, especially if your algorithm is slower than o(n).

**Stage 7: Outro**

* Have questions regarding the company prepared.
* Be interested, smile, and ask follow-up questions to your interviewer's responses.

## Problem solving

The best way to solve leetcode is first to consider the brute force approach. Then, think about how you can optimize it. If you can't think of anything or can't implement it, try to look at the solution. Don't try to solve it. This is the best way to learn leetcode patterns.

![](README-resources/flowchart.png)

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

Blind 75 is a must. Here are some of my questions that I did that I think should be learned before an interview:

| Difficulty | Name | Description |
|------------|------|-------------|
| Medium | 215. Kth Largest Element in an Array | Can sort array and return `nums[len(nums)-k]` which is O(nlogn) or we can use max-heap (populate max-heap in O(1), then pop K roots, and the result is the k'th largest) |
| Easy | 1. Two Sum | Use hashmap to remember if a specific number is present in the current array. Do calculation: `target - nums[i]` check if this exists in the hashmap / hashset / set. Time complexity: O(n) one pass. |
| Easy | 206. Reverse Linked List | Use `prev`, `cur` pointers (sometimes I also use `next` pointer) to correctly point and change the linked list. |
| Medium | 167. Two Sum II - Input array is sorted | Use two pointers, one at the beginning and one at the end. If the sum is greater than the target, move the right pointer to the left. If the sum is less than the target, move the left pointer to the right. |
| Medium | 11. Container With Most Water | Use two pointers. Consider when to increase/decrease left/right pointers. |
| Easy | 1768. Merge Strings Alternately | Traverse with a single array on two strings. Need to keep track of index and lengths of both strings. |

## My favorite questions (by decending order)

| Name | Difficulty | Description |
|------|------------|-------------|
| 20. Valid Parentheses                              | Easy     | Determine if a string that contains parentheses is valid: "[{()}]". The trick is to use stack. |
| 2816. Double a Number Represented as a Linked List | Medium   | First we reverse the linked list. We start from tail of linked list. We double every number and adding carry. Then we unreverse the loinked list. |
| 141. Linked List Cycle                             | Easy     | Find if linked list contains cycle by using fast and slow pointers. |
| 206. Reverse Linked List                           | Easy     | Reverse a linked list in place. Trick: use temporary pointer to the node that we change its links. |
| 200. Number of Islands                             | Medium   | Use DFS to traverse the matrix. For each cell, check if cell is land and mark it. Then call DFS on its neighbors. |
| 62. Unique Paths                                   | Medium   | Use dynamic programming to solve the problem. The number of ways to reach a cell is the sum of the number of ways to reach the cell above and the cell to the left. |
| 1249. Minimum Remove to Make Valid Parentheses     | Medium   | Use data structure of stack to keep track of open paranthesis. Similar to Leetcode 20. |
| 416. Partition Equal Subset Sum                    | Medium   | Use backtracking. For each number, we can choose to add it to the subset or not. We keep track of all possible sums and check if we found target. Meta love this question. |
| 70. Climbing Stairs                                | Easy     | It should be introduction to dynamic programming. The first dynamic programming question, because it teaches you a lot. |
| 129. Sum Root to Leaf Numbers                      | Medium   | Use DFS to traverse the tree. For each node, calculate the sum of the path from the root to the current node. |
| 623. Add One Row to Tree                           | Medium   | Use DFS to traverse the tree. For each node, check if the current level is equal to the target level. If it is, add the new nodes to the tree. |
| 2331. Evaluate Boolean Binary Tree                 | Easy     | For each node, evaluate the expression based on the operator. If we have value 0 it means False, if value 1 it means True, if value 2 it means OR, if value 3 it means AND. |
| 1219. Path with Maximum Gold                       | Medium   | We do backtrack on matrix: up,down,left,right we calculate current gold and we need to return maximum possible gold fom any path. So DFS on matrix. |
| 1325. Delete Leaves With a Given Value             | Medium   | Use DFS to traverse the tree. For each node, check if the node is a leaf and has the given value. If it is, return None. |

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

Dynamic programming: top-down memoization:

```python
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)
```

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

Another BFS code for binary tree (here we use deque - double ended queue library instead of regular list):

```python
from collections import deque

def fn(root):
    queue = deque([root])
    ans = 0

    while queue:
        current_length = len(queue)
        # do logic for current level

        for _ in range(current_length):
            node = queue.popleft()
            # do logic
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans
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

Iterative DFS (notice, in recursion we have stack frame, here we emulating the same thing):

```python
def dfs(root):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        # do logic
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return ans
```

Another iterative DFS:

```python
def fn(graph):
    stack = [START_NODE]
    seen = {START_NODE}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return ans
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
| Easy       | 2331. Evaluate Boolean Binary Tree            | For each node, evaluate the expression based on the operator. If we have value 0 it means False, if value 1 it means True, if value 2 it means OR, if value 3 it means AND. |
| Medium     | 1325. Delete Leaves With a Given Value        | Use DFS to traverse the tree. For each node, check if the node is a leaf and has the given value. If it is, return None. |
| Medium     | 979. Distribute Coins in Binary Tree          | Don't be fooled, it quite hard. Calculate number of spare coins (negative included) per edge of the tree, the answer is the sum of spare coins of all the edges. |

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

Another general code for backtracking:

```python
def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify the answer
        return
    
    ans = 0
    for (ITERATE_OVER_INPUT):
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state
    
    return ans
```

Another example code:

```python
letters = ['a', 'b', 'c', 'd', 'a', 'b']
words = [...]
def backtrack(candidate_index, counter):
    if candidate_index == n:
        # do something with the current solution
        return
    
    # Skip current candidate
    best = backtrack(candidate_index + 1, counter)

    # Take current candidate, only if valid
    if VALID:
        f = Counter(words[candidate_index])
        counter -= f # Modify the counter after we choose current candidate word
        best = max(best, backtrack(candidate_index + 1, counter))
        counter += f # Restore the counter
    
    return best

backtrack(0, Counter(letters))
```

Notice instead of appending to `curr_solution` we use deep copy, because `curr_solution` pointer can be accessed and modified multiple times. Its safer this way.

| Difficulty | Name | Main Idea  |
|------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Medium     | 22. Generate Parentheses                       | Its like a decision tree: each time we either add '(' or ')' such that the string matches valid parentheses. We use DFS to walk from top to bottom to the leafs, and add the leafs to the final solution. The solution is quite elegant, like 10 lines of code.|
| Medium     | 78. Subsets                                    | We can choose to add an element to be added to subset or not. I use index to tell what elements to add to the subset (all elements to the left of the index are already added). |
| Medium     | 416. Partition Equal Subset Sum                | We can choose to add an element to the subset or not. We store all the sums we have. For each num in nums, we add it to the possible sums. |
| Medium     | 39. Combination Sum                            | We start with brute force decision tree. But we want to remove duplicates (order doesn't matter), so we choose index 'i' of candidates that we can choose from. This eliminates duplicates. |
| Medium     | 1219. Path with Maximum Gold                   | We do backtrack on matrix: up,down,left,right we calculate current gold and we need to return maximum possible gold fom any path. So DFS on matrix. |
| Medium     | 131. Palindrome Partitioning                   | We can choose to add a palindrome to the current partition or not. We use index to tell what elements to add to the partition. |
| Hard       | 1255. Maximum Score Words Formed by Letters    | Regular backtracking, we keep track of count of letters that we can use. We check if we have enough letters (is valid), if so we include current candidate word. |
| Hard       | 140. Word Break II                             | We can choose to add a word to the current sentence or not. We backtrack is current sentence doesn't match the desired string. |

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

Sliding window
```python
def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans
    
    return ans
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
| Medium     | 1208. Get Equal Substrings Within Budget                         | Use sliding window to find the longest substring with at most maxCost. |

### Two pointers

We have the two pointers pattern.

1) Either one starts from the beginning and the other from the end.
2) Or both pointers start from the beginning but one pointer moves at faster pace (usually twice as fast) than the other pointer (we call this fast & slow pointers, usually we see this in linked list).

Two pointers: one input, opposite ends
```python
def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return ans
```

Two pointers: two inputs, exhaust both
```python
def fn(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if CONDITION:
            i += 1
        else:
            j += 1
    
    while i < len(arr1):
        # do logic
        i += 1
    
    while j < len(arr2):
        # do logic
        j += 1
    
    return ans
```

| Difficulty | Name | Description |
|------------|----------|----------|
| Easy     | 234. Palindrome Linked List        | |
| Medium   | 151. Reverse Words in a String | Using two-pointers is quite complex. But we can solve with min/max heap. |
| Medium   | 443. String Compression | Use two pointers to compress the string. |
| Easy     | 680. Valid Palindrome II | Use two pointers to check if the string is a palindrome. If the characters at the two pointers are not equal, check if the string is a palindrome by removing one of the characters. This is not quite easy. |
| Medium   | 167. Two Sum II - Input array is sorted | Use two pointers, one at the beginning and one at the end. If the sum is greater than the target, move the right pointer to the left. If the sum is less than the target, move the left pointer to the right. |
| Medium   | 15. 3Sum | Use two pointers to find the sum of three numbers that is equal to the target. Sort the array first. For each number, use two pointers to find the sum of the other two numbers. |
| Medium | 11. Container With Most Water | Consider when to increase left pointer and when to decrease right pointer. |

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
| Medium | 79. Word Search                          | Use DFS to traverse the matrix. For each cell, check if the word can be found starting from that cell. Can be optimized by marking current cell as visited.|
| Medium | 200. Number of Islands                   | Use DFS to traverse the matrix. For each cell, check if the cell is land. If it is, mark it as visited and call DFS on its neighbors. Classic problem. |
| Medium | 1992. Find All Groups of Farmland        | Use DFS to traverse the matrix. For each cell, check if the cell is land. If it is, mark it as visited and call DFS on its neighbors. Or just use regular for loops to traverse matrix, this is faster. |
| Medium | 529. Minesweeper                         | Given click position, you need to update the minesweeper board according the minesweeper rules. Return the board. We use of BFS/DFS to traverse adjacent cells. |
| Medium | 1219. Path with Maximum Gold             | We do backtrack on matrix: up,down,left,right we calculate current gold and we need to return maximum possible gold fom any path. So DFS on matrix. |
| Medium | 2812. Find the Safest Path in a Grid     | Very hard problem. We calculate distance matrix of thiefs cells, we want to find best safest path (maximize minimum distance to thiefs). We use BFS to calculate distance matrix. We also use max-heap. |

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

Build a prefix sum

```python
def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix
```

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium | 560. Subarray Sum Equals K | We take the brute force approach O(n^2) and optimize it. Use prefix sum to calculate the sum of the subarray. For each subarray, calculate the sum of the subarray. If the sum is equal to the target, increment the count. |
| Medium | 1915. Number of Wonderful Substrings | Similar to prefix sum we have prefix bitmasks XOR. |
| Easy   | 1608. Special Array With X Elements Greater Than or Equal X | Use prefix sum to calculate the number of elements greater than or equal to X. If the number of elements is equal to the element, return the element. Two key words: Count (frequencies), Prefix sum of frequencies |

### Bit manipulation

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium | 1915. Number of Wonderful Substrings | Use prefix bitmasks XOR to calculate the XOR of the subarray. For each subarray, calculate the XOR of the subarray. If the XOR is a power of 2, increment the count. |
| Hard   | 3068. Find the Maximum Sum of Node Values   | The main idea is `(a xor b) xor b = a`, the main observation is that we can xor ANY pair of nodes in the tree, not just directly connected nodes. We traverse deltas array in pairs to check benefit or no benefit of XORing numbers. |
| Easy   | 1863. Sum of All Subset XOR Totals          | The main idea is to calculate all possible subsets of the array and calculate the XOR of each subset. |

### Heap/Priority Queue

Find top k elements with heap:

```python
import heapq

def fn(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for num in heap]
```

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium     | 692. Top K Frequent Words | Use max-heap to keep track of the frequency of each word. For each word, increment the frequency. Then, for each word in the frequency hashmap, add it to the max-heap. Pop the top K elements from the max-heap. |
| Medium     | 215. Kth Largest Element in an Array | Use max-heap to keep track of the K largest elements. For each element, add it to the max-heap. Pop the top element from the max-heap K times. |

### Linked List

Slow, fast pointers:

```python
def fn(head):
    slow = head
    fast = head
    ans = 0

    while fast and fast.next:
        # do logic
        slow = slow.next
        fast = fast.next.next
    
    return ans
```

Reversing linked list:

```python
def fn(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 
        
    return prev
```

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Easy | 206. Reverse Linked List | Use two pointers to reverse the linked list. For each node, reverse the links. |
| Medium | 237. Delete Node in a Linked List | Given the node to be deleted, copy the value of the next node to the current node and delete the next node. |
| Medium      | 2487. Remove Nodes From Linked List | Either use right prefix pattern or use stack. |

### Subsets

To return all subsets of given array `nums`:

```python
"""
If nums == [2,4,6]
Then the output will be: [[], [2], [2, 4], [2, 4, 6], [2, 6], [4], [4, 6], [6]]
Runtime complexity: O(n * 2^n) > O(2^n)
"""
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    
    backtrack(0, [])
    return res
```

Another pattern is to use counter 

| Difficulty | Name | Description |
|------------|------|-----------------------------------------------------------------|
| Medium | 78. Subsets | Use backtracking to generate all possible subsets of the array. For each element, choose to add it to the subset or not. |
| Medium | 2597. The Number of Beatiful Subsets | Use backtracking to generate all possible subsets of the array. For each subset, check if it is a beautiful subset. |

## Meta interview questions

| Difficulty | Name | Source |
|------------|--------|------------------------------|
| Medium     | 1249. Minimum Remove to Make Valid Parentheses    | [Reddit](https://www.reddit.com/r/leetcode/comments/16zr1sj/meta_ramping_up_hiring_what_to_expect/) |
| Medium     | 560. Subarray Sum Equals K                        | |
| Medium     | 824. Goat Latin                                   | [Glassdoor](https://www.glassdoor.com/Interview/network-engineer-interview-questions-SRCH_KO0,16.htm) |
| Easy       | 283. Move Zeroes                                  | [Glassdoor](https://www.glassdoor.com/Interview/network-engineer-interview-questions-SRCH_KO0,16.htm) |
| Medium     | 15. 3Sum                                          | [Glassdoor](https://www.glassdoor.com/Interview/network-engineer-interview-questions-SRCH_KO0,16.htm) |
| Medium     | 416. Partition Equal Subset Sum                   | [Glassdoor](https://www.glassdoor.com/Interview/network-engineer-interview-questions-SRCH_KO0,16.htm) |
| Medium     | 529. Minesweeper                                  | [Glassdoor](https://www.glassdoor.com/Interview/Meta-Production-Engineer-Interview-Questions-EI_IE40772.0,4_KO5,24_IP2.htm?filter.jobTitleFTS=Production+Engineer) |
| Easy       | 680. Valid Palindrome II                          | [Glassdoor](https://www.glassdoor.com/Interview/Meta-Production-Engineer-Interview-Questions-EI_IE40772.0,4_KO5,24_IP2.htm?filter.jobTitleFTS=Production+Engineer) |

Non-leetcode questions:

| Question | Source |
|----------|--------|
| Write some code that lists the top 10 most frequent words in a file | [Glassdoor](https://www.glassdoor.com/Interview/Meta-Production-Engineer-Interview-Questions-EI_IE40772.0,4_KO5,24_IP2.htm?filter.jobTitleFTS=Production+Engineer) |


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

### Network Production Engineer Meta May 2024 - Coding Round - Q1

Write a function that returns True if a given string is polyndrome.
Polyndrome is a string that is the same when reversed if you ignore punctuations and capitalization.
Some examples of polyndromes / non-palyndromes are:

```
assert is_palindrome("Race car") == True
assert is_palindrome("") == True
assert is_palindrome(None) == True
assert is_palindrome("ab") == False
assert is_palindrome("aA") == True
assert is_palindrome("!") == True
assert is_palindrome("!!") == True # This is a case where most fail
assert is_palindrome("!!!") == True
```

I did not write it down but they also expect exclamation marks to ignore ('!'), example: "!Ract car!" is a polnydrome. I also asked the questions: "are numbers count?" example: 6a6 or A6a is polyndrome. They said yes.

My solution: I will do while loop with two-pointers and avoid characters that are not alpha-numerical. Runtime complexity: O(n)

```python
def is_palindrome(s: Optional[str]) -> bool:
    if s is None or len(s) < 2:
        return True

    l, r = 0, len(s) - 1
    while l <= r:
        # isalnum checks for spaces!
        while l < r and s[l].isalnum() == False:
            l += 1
        while r > l and s[r].isalnum() == False:
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1
    return True
```

### Network Production Engineer Meta May 2024 - Coding Round - Q2

We are going to write a CLI that passes a database of forune coockies (a text file) and print a random forune coockie to the screen (fortune coockie is just a string).

In the STDIN line by line, fortune coockies are seperated by a new line and single precentage ('%') and a new line.

Your task is to write a CLI that opens a file, parses it, extracts in some way the forunes, and prints out a random one to the screen.

Example:

```
Hello world!
%
This is the second fortune coockie text.
This is still the same fortune coockie.
% 
This is the next fortune coockie (String).
How to implement a CLI that prints a RANDOM fortune coockie to the screen?
```

Questions to ask:

* Do I know the size of the number of fortune coockies? Answer: it may be enourmesly large.

Because I don't know the length of the number of fortunes, I need to parse the entire file and check for the amount of fortunes, and then select a random integer between 0 and `len(fortunes)` and then I'll parse the file again until I reach the fortune, and then I print it.

This is two-pass approach. The interviewer saied its OK.

So another question to ask is if its OK to use a hashmap to retrive the fortune in O(1). The interviwer said OK (one pass). Then I asked the interviewer if the fortune file contains '%' at the beginning (indicating starting of next forune). He said no. "We will assume the file starts with a legitimate version of the fortune".

One pass solution:

```python
import random
def getRandomFortune(file: str):
    lst = []
    fortune = ""
    with open(file) as f:
        for line in f:
            if line == "%\n":
                lst.append(fortune)
                fortune = ""
            else:
                fortune += line
    # Last fortune doesn't have '%' at the end to indicate end so we append it
    lst.append(fortune)

    fortunes_length = len(lst)
    rand_fortune_index = random.randint(0, fortunes_length - 1) # randint includes the end point so we do minus 1
    return lst[rand_fortune_index]
```

Now the interviewer asks: "what if we decided if the size of the file exceeds available OS RAM?"

I said we do two-pass approach. First pass: count amount of fortunes. And then second pass I open the file again and read it until I reach the desired random fortune index.

Then interviewer said OK lets do this. But can you think of a way to make the second read much, much faster?

The interviewer helped me and hinted me about offsets in the file. I said I will count number of fortunes and also create list of offsets where each fortune 'i' starts.

I asked help from the interviewer I dont know the syntax how to access offset in a file. `tell()` will tell the current position of the file pointer (offset), and `seek` will allow to change the position of the offset in the file (to read it later).

My solution:

```python
def getRandomFortune(file: str):
    offset_lst = [0] # First fortune always at 0
    fortunes_length = 0

    # Create offset table
    with open(file, "r") as f:
        line = f.readline()
        while line:
            if line == "%\n":
                fortunes_length += 1
                curr_offset = f.tell()
                offset_lst.append(curr_offset)
            line = f.readline()

    # Last fortune has no '%\n' and we still need to count it
    fortunes_length += 1

    # Get in O(1) the random fortune
    fortune = ""
    rand_fortune_index = random.randint(0, fortunes_length - 1)  # randint includes the end point so we do minus 1
    with open(file, "r") as f:
        offset = offset_lst[rand_fortune_index]
        f.seek(offset)
        line = f.readline()
        while line and line != "%\n":
            fortune += line
            line = f.readline()
        return fortune
```

He likes my solution. He asked "do you have any questions for me?" I said: "yes, could you tell me more about your day-to-day tasks as production engineer? configurations? something interesting".


### Production Engineer Meta - Prep Material - Example Q1

A balanced partition is a split of an array into two parts (without reordering
any elements) such that the sum of numbers before the split equals the sum of
numbers after the split.
You are given a file containing N arrays of integers, one array per line, where
each array is represented as comma-separated integers.
For each array in the file, if the array can be partitioned in a balanced way,
return the balanced partitions.
Example Input:
```
# file.txt
1,2,3,4
1,4,5
Expected Output:
[[1,4], [5]]
```

My solution:

```python
def balance_parition(arr: List[int]):
    s = sum(arr)
    if s % 2 != 0:
        print(f"Can't parition array: {arr}")
        return None

    arr = sorted(arr) # O(n log n)
    curr_sum = 0

    left, right = [], []
    can_partition = False

    for i, n in enumerate(arr):
        curr_sum += n
        left.append(n)

        if curr_sum == (s / 2):
            # We reached middle
            can_partition = True
            right = arr[i+1:]
            break
    if can_partition:
        return [left, right]
    return None

file = 'hello.txt'
with open(file) as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            print([])
            continue
        split = line.split(',')
        arr = [int(x) for x in split]
        print(balance_parition(arr))
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
