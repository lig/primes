primes = (0..10000).to_a

t = Time.now.to_i

for i in (2..10000)
  for j in (2..(i-1))
    if (primes[i] != 0) and (primes[i] % j == 0) then
      primes[i] = 0;
    end
  end
end

print (Time.now.to_i - t).to_s