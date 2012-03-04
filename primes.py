from collections import deque
from datetime import datetime


start = datetime.now()

primes = deque([0, 1])

for i in range(2, 10000):
    is_prime = True

    for j in range(2, (i - 1)):

        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)

stop = datetime.now()

print(stop - start)
