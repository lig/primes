from collections import deque
from datetime import datetime


start = datetime.now()

primes = deque([0, 1])

for i in range(2, 10000):

    for j in range(2, (i - 1)):

        if i % j == 0:
            i = None
            break

    if i:
        primes.append(i)

stop = datetime.now()

print(stop - start)
