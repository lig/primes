from datetime import datetime


start = datetime.now()

primes = [0, 1]

for i in range(2, 10000):

    for j in primes[2:]:

        if i % j == 0:
            i = None
            break

    if i:
        primes.append(i)

stop = datetime.now()

print(stop - start)
