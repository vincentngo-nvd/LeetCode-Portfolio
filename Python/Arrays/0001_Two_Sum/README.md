# 0001 - Two Sum

## Idea: Using a Hash Map for Speed

This problem asks us to find two numbers that sum up to a specific target.

### Approach Summary

The brute-force method (checking every pair of numbers) is too slow ($O(N^2)$). To solve it efficiently, I used a **Hash Map** (Python Dictionary) in a single pass.

1.  **Why Hash Map?** Hash Maps provide **very fast lookup time** ($O(1)$). This allows us to search for the required number instantly.
2.  **How it works:** As I iterate through the list, for each number (let's call it $X$), I calculate the required partner number, or **Complement** (which is $Target - X$).
3.  **Check and Store:**
    * I check if the **Complement** is already in the Hash Map. If it is, I found the solution and return the indices.
    * If not, I store the current number $X$ and its index in the Hash Map for future checks.

## Complexity

* **Time Complexity:** $O(N)$. I only need to iterate through the array once.
* **Space Complexity:** $O(N)$, as the Hash Map might store all elements in the worst case.
