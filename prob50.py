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

def find_cons_prime(bound):
    fill_primes(bound)
    max_cons = 0
    max_index = 0
    for i in range(0,len(primes)):
        print(i)
        cons = 1
        asum = primes[i]
        for j in range(i + 1,len(primes)):
            asum = asum + primes[j]
            cons = cons + 1
            if(asum > 1000000):
                break
            if(asum in primes):
                if(cons > max_cons):
                    max_cons = cons
                    max_index = i
    return (max_index,max_cons)

(start,length) = find_cons_prime(1000000)
print(start)
print(length)
print(sum([primes[i] for i in range(start,length + start )]))

