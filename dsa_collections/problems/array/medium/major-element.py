def major_element(arr):
    major = 0
    count = 0
    
    for item in arr:
        # init case or changing major
        if count == 0:
            major = item   
        # plus
        if item == major:
            count += 1
        else: # other number
            count -= 1
    
    count = 0
    for num in arr:
        if num == major:
            count += 1

    if count > len(arr) // 2:
        return major
    else:
        return -1
            