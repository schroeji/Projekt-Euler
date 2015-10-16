def find_sums(cost):
    counts = {0 : 1}
    for i in range(1, cost):
        for  j in range(i, cost + 1):
            try:
                counts[j] += counts[j - i]
            except:
                counts[j] = 0
                counts[j] += counts[j - i]
    return counts[cost]
    
print find_sums(100)