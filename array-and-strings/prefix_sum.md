Prefix sums is a preprocessing trick — you spend O(n) time building a table upfront so that any "sum between index i and j" question is answered in O(1) instead of O(n).
The core idea: prefix[i] stores the sum of all elements from index 0 up to i. Then any range sum [L, R] is just prefix[R] - prefix[L-1]. No loop needed.
