# 0001 - Two Sum

## 💡 Approach: Using a Hash Map (Two-pass/One-pass)

The most efficient solution utilizes a **Hash Map** to store the numbers we have already iterated through along with their **index**.

For each number $num$ in the array, we calculate the required **complement**:
$$complement = target - num$$

1.  **Check:** We check if the $complement$ already exists in the Hash Map. If it does, we have found the pair and return their indices: $[hash\_map[complement], current\_index]$.
2.  **Store:** If the complement is not found, we add the current $num$ and its index $i$ to the Hash Map: $hash\_map[num] = i$.

## ⏱ Complexity Analysis (Optimal Solution)

* **Time Complexity:** $O(N)$ - We iterate through the list only once. Hash Map lookups and insertions take an average $O(1)$ time.
* **Space Complexity:** $O(N)$ - In the worst-case scenario, the Hash Map will store all $N$ elements.
