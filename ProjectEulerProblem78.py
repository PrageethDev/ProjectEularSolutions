__author__ = 'prageeth'

def pentagonalNumGenerator():
    n = 0
    while 1:
        n += 1
        yield int(0.5*n*(3*n-1))
        yield int(0.5*-n*(3*-n-1))


calculatedPartitionContainer = {0:1,}

def partitioning():
    iterator = pentagonalNumGenerator()
    pentagonals = [iterator.next() for num in range(10000)]

    for leastValue in xrange(1,1000000):
        noOfPartitions = 0
        flip,plus = 1,1
        for j in pentagonals:
            x = leastValue - j
            if x < 0: break
            if plus: noOfPartitions += calculatedPartitionContainer[x]
            else: noOfPartitions -= calculatedPartitionContainer[x]

            flip ^= 1
            if flip: plus ^=1

        print leastValue
        calculatedPartitionContainer[leastValue] = noOfPartitions

        if not noOfPartitions % 1000:
            if not noOfPartitions % 1000000:
                print "Least value of p(n) divisible by 1 million = ", leastValue
                print "No. of partitions it has = ", noOfPartitions
                exit()


if __name__ == '__main__':
    partitioning()