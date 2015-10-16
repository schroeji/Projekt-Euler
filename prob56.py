def digit_sum(x):
    erg = 0
    for i in str(x):
        erg += int(i)
    return erg
max_sum = 0
for i in range(1,100):
    for j in range(1,100):
        max_sum = max(max_sum,digit_sum(i**j))
print max_sum