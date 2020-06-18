# Combining the conquered!

After sorting 2 arrays of integers, **A** and **B**, merge **B** into **A** as one sorted array.

**Details**:
* The number of initialized elements in **A** and **B** are **m** and **n** respectively.
* You may assume that **A** has enough space to store all elements of **B** (you'll not have to resize **A**), that is, the size of **A** is at least **m+n**.

### Example

**Input**:
* **A**: `[1,2,3,0,0,0,0]`, **m:** `3`
* **B**: `[1,2,5,9]`, **n:** `4`

**Output**: `None`
* Explanation: After running the `merge` procedure, **A**
must look like `[1, 1, 2, 2, 3, 5, 9]`

# How to submit:

Complete the function `merge(A, m, B, n)` in `solution.py`