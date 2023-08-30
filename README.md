# leetcode
My solutions to leet code questions.

# Problem solving

The best way to solve leetcode is first to consider the brute force approach.

Then, think about how you can optimize it.

If you can't think of anything or can't implement it, try to look at the solution. Don't try to solve it.

This is the best way to learn leetcode patterns.

# Common Interview Questions

* Leetcode Blind 75 with notes: [here](https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit#gid=0)
* DFS, BFS, recursive
* DFS, BFS, iterative
* Two Sum variations
* Max sub array (kadane's algo)
* 

# Problems by category

## Dynamic programming

Difficulty | Number | Name                          | Main Idea    |
-----------|--------|-------------------------------|--------------|
Medium     | 300    | Longest Increasing Subsequence| Think about the dynamic programming pattern. This pattern matches the question. dp[i] = longest strickly increasing subsequence of nums[0...i] |

## Binary Tree Traversal

Difficulty | Number | Name                         | Main Idea    |
-----------|--------|------------------------------|--------------|
Easy       | 257    | Binary Tree Paths            | Simply return paths from root to all leafs in any order, return string. Easy. |
Hard       | 124    | Binary Tree Maximum Path Sum | Start from leafs. Consider the base cases first of leafs. Then continue to first parent. Consider to split or not to split the path on that current node. Either take left path or right path (subproblems). My solution was 90% close to the working algorithm. Its ok to look at solutions. Don't waste hours on this problem. |