
The sliding window technique is about maintaining a contiguous subarray (the "window") that you expand and shrink as you move forward — never going backward. This gives you O(n) instead of O(n²) from nested loops.

Two flavors:

Fixed size — window size k is given. Slide it forward, add the new right element, drop the old left element.
Variable size — expand the right edge freely, shrink the left edge when a condition is violated.
