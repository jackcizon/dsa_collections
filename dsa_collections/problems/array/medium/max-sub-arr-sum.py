# Maximum Subarray Sum
# Kadane's Algorithm

def kadane(arr):
    local_max = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        local_max = max(arr[i], local_max + arr[i])
        max_sum = max(local_max, max_sum)
    
    return max_sum
