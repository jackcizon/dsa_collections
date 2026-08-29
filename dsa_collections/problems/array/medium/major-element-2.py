from math import ceil


def major_element_2(arr):
    m1 = None
    m2 = None
    
    c1 = 0
    c2 = 0
    
    for a in arr:
        if a == m1:
            c1 += 1
        elif a == m2:
            c2 += 1
        
        elif c1 == 0:
            m1 = a
            c1 = 1
        elif c2 == 0:
            m2 = a
            c2 = 1
        
        else:
            c1 -= 1
            c2 -= 1
            
    
    c1 = 0
    c2 = 0
    for item in arr:
        if item == m1:
            c1 += 1
        if item == m2:
            c2 += 1
    
    res = []
    if c1 > len(arr) // 3:
        res.append(m1)
    if c2 > len(arr) // 3:
        res.append(m2)
    
    return res