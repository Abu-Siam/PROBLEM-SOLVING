# Build — O(n)
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

# Query any range [L, R] — O(1)
range_sum = prefix[R+1] - prefix[L]
