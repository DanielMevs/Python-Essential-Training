def allPrimesUpTo(num):
    primes = [2]

    for number in range(3, num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor == 0:
                break
            if factor > sqrtNum:
                primes.append(number)
                break
    
    return primes