The two pointers technique is simple: instead of using nested loops (O(n²)), you place two indices on the array and move them smartly — cutting it down to O(n).
There are two main flavors:

Opposite ends — left starts at 0, right starts at the end, they move toward each other. Used when the array is sorted and you're looking for a pair.
Same direction — slow pointer marks a position, fast pointer scans ahead. Used for removing elements, finding duplicates, partitioning.
