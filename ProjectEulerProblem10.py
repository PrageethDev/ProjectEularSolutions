__author__ = 'prageeth'
__author__ = 'prageeth'

def primes(limit):
    numbers = range(3, limit+1, 2)
    half = (limit)//2
    initial = 4

    for step in xrange(3, limit+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            primeList = [2] + filter(None, numbers)
            return primeList


def listingPrimesAndAdding(limit):
    outPut = primes(limit)
    sumOfPrimeList = 0
    for element in outPut:
        print element
        sumOfPrimeList += element
    return sumOfPrimeList


if __name__ == '__main__':
    limit = 1000000
    sumOfPrimes = listingPrimesAndAdding(limit)
    print '   OK, Next prime is greater than ' + str(limit)
    print 'Sum of primes below ' + str(limit) + ' = ' + s