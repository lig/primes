primes = []
t = Time.now.to_f

(2..10000).each() { |i|
  k = Math.sqrt(i).to_i()
  j = 2
  until j > k || (i % j).zero? do  j += 1 end
  primes.push(i) if j > k
}

print (Time.now.to_f - t).to_s
