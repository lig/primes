primes = Array.new

t = Time.now.to_f

for i in (2..10000)
  is_prime = true

  for j in (2..(i-1))
    if i % j == 0 then
      is_prime = false
      break
    end
  end

  if is_prime == true then
    primes.push(i)
  end
end

print (Time.now.to_f - t).to_s