# 0217 - Contains Duplicate

## Idea: Using a Hash Set for O(1) Lookup

The goal is to quickly find if any value appears at least twice in an array.

### Approach Summary

The most efficient approach is to use a **Hash Set** (Python's `set`). This allows for nearly instant checks (**O(1)** time complexity) for existence.

1.  **Tracking:** Initialize an empty Hash Set (`seen`).
2.  **Iterate:** Loop through each number in the input array.
3.  **Check:** For each number, check if it's already in the `seen` set.
    * If **yes**, a duplicate is found, return `True`.
    * If **no**, add the number to the `seen` set and continue.
4.  **Result:** If the entire array is processed without finding duplicates, return `False`.

## Complexity

* **Time Complexity:** **O(N)**. We iterate through the array once. Hash Set operations are O(1) on average.
* **Space Complexity:** **O(N)**. In the worst case, the Hash Set stores all N unique elements.