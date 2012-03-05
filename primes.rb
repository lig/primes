primes = Array.new

t = Time.now.to_f

for i in (2..10000)
  k = Math.sqrt(i).to_i()

  for j in (2..(i-1))

    break if j > k

    if i % j == 0 then
      i = nil
      break
    end
  end

  if i then
    primes.push(i)
  end
end

print (Time.now.to_f - t).to_s