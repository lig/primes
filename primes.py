from datetime import datetime

primes = range(0, 10000)

start = datetime.now()

for i in range(2, 10000):
    for j in range(2, (i - 1)):
        if (primes[i] != 0) and (primes[i] % j == 0):
            primes[i] = 0

stop = datetime.now()

print(stop - start)
