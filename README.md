# leetcode
My solutions to leet code questions.

## Problem solving

The best way to solve leetcode is first to consider the brute force approach.

Then, think about how you can optimize it.

If you can't think of anything or can't implement it, try to look at the solution. Don't try to solve it.

This is the best way to learn leetcode patterns.

## Cheat Sheet

| Name                                | Trick                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
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

## My favorite questions (by decending order)

| Number | Name | Description |
|--------|------|-------------|
| 20 | Valid Parentheses | Determine if a string that contains parentheses is valid: "[{()}]". The trick is to use stack. |
| 141 | Linked List Cycle | Find if linked list contains cycle by using fast and slow pointers. |
| 206 | Reverse Linked List | Reverse a linked list in place. Trick: use temporary pointer to the node that we change its links. |

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

1. Find substring with `find()` function
2. Find substring, starting from the right with `rfind()` function
3. Reverse string: `my_str.reverse()` or `my_str_revresed = reversed(my_str)`

## Problems by category

### Dynamic programming

| Difficulty | Number | Name                           | Main Idea                                                                                                                                      |
|------------|--------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Medium     | 300    | Longest Increasing Subsequence | Think about the dynamic programming pattern. This pattern matches the question. dp[i] = longest strickly increasing subsequence of nums[0...i] |

### Binary Tree Traversal

| Difficulty | Number | Name                         | Main Idea                                                                                                                                                                                                                                                                                                                        |
|------------|--------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Easy       | 257    | Binary Tree Paths            | Simply return paths from root to all leafs in any order, return string. Easy.                                                                                                                                                                                                                                                    |
| Hard       | 124    | Binary Tree Maximum Path Sum | Start from leafs. Consider the base cases first of leafs. Then continue to first parent. Consider to split or not to split the path on that current node. Either take left path or right path (subproblems). My solution was 90% close to the working algorithm. Its ok to look at solutions. Don't waste hours on this problem. |


## Meta interview questions

| Difficulty | Name | Source                                                                                                                                                                                                                                                                                                                    |
|------------|--------|------------------------------|
| Medium     | 1249. Minimum Remove to Make Valid Parentheses | [Reddit](https://www.reddit.com/r/leetcode/comments/16zr1sj/meta_ramping_up_hiring_what_to_expect/)