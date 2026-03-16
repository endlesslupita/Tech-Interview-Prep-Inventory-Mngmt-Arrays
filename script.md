# Interview Script: Duplicate Zeros In-Place

---

## Introduction

Hi, my name is [Name], and today I'll be solving the Inventory Management array problem.
The task is to duplicate each zero in an array in-place, shifting remaining elements
to the right and truncating at the original length.

---

## Clarifying Questions

Before I start coding, I want to ask a few clarifying questions.

**Can the array be empty?**
I'll assume yes, and my solution should handle that gracefully without errors.

**Should I modify the array in-place, or can I return a new one?**
The problem says in-place, so I won't allocate a second array.

**Is it guaranteed that elements are non-negative integers?**
Based on the inventory scenario, I'll assume so.

**What happens to elements pushed beyond the original length?**
They are discarded — the array length stays fixed. So if a zero near the end
would require its duplicate to go out of bounds, the duplicate is simply lost.

---

## Naive Solution

My first approach is straightforward: scan left to right. When I find a zero,
I insert a duplicate zero immediately after it, then remove the last element
to keep the array the same length.

```
inventory = [4, 0, 1, 3, 0, 2, 5, 0]

Step 1: check=0, value=4, not zero, move right
Step 2: check=1, value=0 → pop last, insert 0 at index 2, skip to check=3

[4, 0, 0, 1, 3, 0, 2, 5]
         ^check=3

Step 3: check=3, value=1, not zero
Step 4: check=4, value=3, not zero
Step 5: check=5, value=0 → pop last, insert 0 at index 6, skip to check=7

[4, 0, 0, 1, 3, 0, 0, 2]
                     ^check=7

Step 6: check=7, but 7 < (8-1)=7 is False → loop ends

Result: [4, 0, 0, 1, 3, 0, 0, 2]  ✓
```

I use a `while` loop instead of `for` because I need manual control over the
index — after inserting a zero, I advance by 2 to skip the duplicate. A `for`
loop's counter would be overridden by the `range` iterator even if you reassign
`i` inside the loop body.

`list.insert(index, value)` places the new value *at* that index, pushing the
existing element right. So I increment `check` first, then call `insert(check, 0)` —
equivalent to `insert(original_check + 1, 0)`.

I `pop()` before `insert()` — either order produces the same result, but popping
first avoids holding a temporarily oversized list.

I stop at index `len - 2` (second-to-last) because a zero at the final position
would only produce a duplicate that falls outside the array bounds — nothing
to do.

```python
def zero_duplicate(inventory):
    check = 0
    while check < (len(inventory) - 1):
        if inventory[check] == 0:
            inventory.pop()
            check += 1
            inventory.insert(check, 0)
            check += 1
        else:
            check += 1
    return inventory
```

**Complexity:**
- Time: O(n²) — the outer loop is O(n), and each `insert` shifts up to n elements
- Space: O(1) — no extra memory allocated, modified in-place

---

## Optimized Solution

The naive solution is O(n²) because each `insert` shifts elements right one by one.
The key insight for the optimized version is: if we already know where each element
will end up, we can write it directly there — no shifting needed.

The strategy is a two-pointer approach moving right to left.

**Step 1 — Forward pass:** Simulate the result without modifying anything.
Count how many positions each element will occupy (1 for non-zero, 2 for zero).
When the running count reaches the array length, we've found the last element
that fits. That becomes our read pointer `left`.

**Special case:** If the running count would exceed the array length by landing
on a zero (count + 2 > length), that zero fits only once — set a flag and
count it as 1.

```
inventory = [4, 0, 1, 3, 0, 2, 5, 0],  length = 8

Forward pass (count positions):
  4  → count=1
  0  → count=3  (takes 2 spots)
  1  → count=4
  3  → count=5
  0  → count=7  (takes 2 spots)
  2  → count=8  → STOP, left=5

left=5 (value 2), right=7 (last index)
```

**Step 2 — Backward pass:** Move right to left. For each element at `left`,
write it to `right`. If it's a zero (and not flagged), write it twice.

```
Backward pass:

left=5 (2),  right=7:  write 2        → [..., ..., ..., ..., ..., ..., ..., 2]
left=4 (0),  right=6:  write 0, 0     → [..., ..., ..., ..., ..., 0,  0,  2]
left=3 (3),  right=4:  write 3        → [..., ..., ..., 3,  3,  0,  0,  2]
left=2 (1),  right=3:  write 1        → [..., ..., 0,  1,  3,  0,  0,  2]
left=1 (0),  right=2:  write 0, 0     → [..., 0,  0,  1,  3,  0,  0,  2]
left=0 (4),  right=0:  write 4        → [4,  0,  0,  1,  3,  0,  0,  2]

Result: [4, 0, 0, 1, 3, 0, 0, 2]  ✓
```

```python
def zero_duplicate_optimized(inventory):
    count = 0
    left = 0
    flag = 0
    list_length = len(inventory)
    right = list_length - 1

    while count < list_length:
        if inventory[left] == 0:
            if count + 2 > list_length:
                flag = 1
                count += 1
            else:
                count += 2
        else:
            count += 1
        left += 1

    # The forward loop increments `left` one extra time after the condition becomes
    # false. Subtract 1 to correct for the over-increment.
    if left != 0:
        left -= 1

    # right = list_length - 1, so an empty list gives right = -1, skipping the
    # backward pass entirely and avoiding an index error.
    if right >= 0:
        while left >= 0:
            if inventory[left] == 0 and flag == 0:
                inventory[right] = 0
                right -= 1
                inventory[right] = 0
            else:
                inventory[right] = inventory[left]
                flag = 0
            right -= 1
            left -= 1

    return inventory
```

**Complexity:**
- Time: O(n) — two linear passes, no shifting
- Space: O(1) — only a handful of index variables, no extra array

---

## Trade-Off Summary

| Version   | Time   | Space | Notes                              |
|-----------|--------|-------|------------------------------------|
| Naive     | O(n²)  | O(1)  | Simple, easy to reason about       |
| Optimized | O(n)   | O(1)  | Faster, but requires careful logic |

The optimized version is worth the added complexity in performance-critical
contexts. For small arrays, the naive solution is easier to read and maintain.

---

## Tests

I wrote pytest unit tests covering:
- Normal cases: zero in middle, zero at end (flag case), multiple zeros
- Edge cases: empty list, single element, no zeros, all zeros, zero at start, single zero

All tests pass for both implementations.
