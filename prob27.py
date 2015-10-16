def fill_primes(bound):
    
    for i in range(3, bound + 1, 2):
        noprime = False
        for j in range(3, int(i ** 0.5) + 1, 2):
            if(i % j == 0):
                noprime = True
                break
        if(not noprime):
            primes.append(i)

primes = [2]
fill_primes(100000)
max_count = 0
for i in range(-999,999):
    for j in range(-999,999):
        
        def f(x): return x**2 + i*x + j
        
        c = 0
        
        while(f(c) in primes):
            c = c + 1
            
        if (c > max_count):
            print(i*j)
            print(i)
            print(j)
            max_count = c
            print(max_count)
            print("--------")