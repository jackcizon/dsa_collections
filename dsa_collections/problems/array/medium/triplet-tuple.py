def triplet_tuple(arr):
    small = 2 ** 32 - 1
    medium = 2 ** 32 - 1
    
    for a in arr:
        if a <= small:
            small = a
        elif a <= medium:
            medium = a
        else:
            return [small, medium, a]
    
    return []
