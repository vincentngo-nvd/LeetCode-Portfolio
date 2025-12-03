# 0003 - Longest Substring Without Repeating Characters

## Idea: Learning the Sliding Window Technique

This problem was a great opportunity to practice the **Sliding Window** technique, which is a powerful way to optimize problems on arrays or strings.

### Approach Summary

Instead of using two nested loops, which is slow, I used two pointers, **Left** (`l`) and **Right** (`r`), to define a "window" that moves across the string.

1.  **The Window:** The window, defined by `s[l:r+1]`, must always contain only unique characters.
2.  **Tracking:** I use a **Hash Set** to keep track of the characters currently inside the window for quick checking.
3.  **Adjustment (The "Slide"):**
    * **Expand:** I move the **Right** pointer forward (`r++`) to try and grow the window.
    * **Shrink:** If the new character at `s[r]` is already in the Hash Set (meaning it's a duplicate), I **shrink** the window from the left by moving the **Left** pointer forward (`l++`) and removing characters from the Hash Set until the duplicate is gone.
    * After each step, I calculate the length of the current window (`r - l + 1`) and save the maximum length found so far.

## Complexity

* **Time Complexity:** $O(N)$. The reason it's $O(N)$ is that both the Left and Right pointers only move forward and never go back, ensuring every character is processed only a few times.
* **Space Complexity:** $O(\Sigma)$, where $\Sigma$ is the size of the alphabet (e.g., 128 for all ASCII characters).