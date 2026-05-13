def sliding_window(arr, target):
# define the function
    L = 0
# left edge of window
    window = 0  # or set(), or dict()
# track window state
    best = 0
# store the answer
    for R in range(len(arr)):
# R expands the window
        window += arr[R]
# ① add new element
        while window > target:
# ② window broke a rule
            window -= arr[L]
# remove left element
            L += 1
# shrink the window
        best = max(best, R - L + 1)
# ③ window is valid — update answer
    return best
# return the answer