import time

primes = range(0,10000)

t = time.time()

for i in range(2, 10000):
    for j in range(2, (i-1)):
        if (primes[i] != 0) and (primes[i] % j == 0):
            primes[i] = 0;

print((time.time() - t))