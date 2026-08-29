def max_product_sub_arr(arr):
    n = len(arr)
    max_prod = -2 ** 32
    
    l2r = 1
    r2l = 1
    
    for i in range(n):
        # if occurs 0, reset 1
        if l2r == 0:  
            l2r = 1
        if r2l == 0:
            r2l = 1
        
        l2r *= arr[i]
        r2l *= arr[n - 1 - i]
        
        max_prod = max(l2r, r2l, max_prod)
        
    return max_prod
