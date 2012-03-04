<?php
set_time_limit(0);
$primes = array();

for($i=0; $i<10000; $i++) {
	$primes[$i] = $i;
}
$timeStart = time();
for($i=2; $i<10000; $i++) {
	for($j=2; $j<$i; $j++) {
		if((($primes[$i]) != 0) && ($primes[$i] % $j == 0)) {
			$primes[$i] = 0;
		}
	}
}

echo (time() - $timeStart);