def sliding_window(arr, k):
    window = sum(arr[0:k]) # initial window
    max_sum = window

    for i in range (k, len(arr)):
        window+= arr[i] # vul korse
        window-= arr[i-k]
        max_sum=max(max_sum, window)
    
    print(max_sum)

print(sliding_window([1,2,3,4,5,6],3))
