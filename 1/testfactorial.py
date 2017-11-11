import multiprocessing
import math
import sys


def product(rangelist):
    start = rangelist[0]
    stop = rangelist[1]
    step = rangelist[2]
    product = 1
    for i in range(start,stop,step):
        product *= i
    return product

if __name__=="__main__":
    n = int(sys.argv[1]) 
    import time
    p = multiprocessing.Pool(2)

    print 'method1 product using for loop, consumed time' 
    t0 = time.time()
    res1 = product([1, n+1, 1])
    print time.time() - t0
    
    print 'method2 break calculation into 2 parts, consumed time'
    t0 = time.time()
    res = map(product, ([1,n+1,2], [2,n+1,2]))
    res2 = res[0] * res[1]
    print time.time() - t0
    
    print 'method3 break calculation into 2 parts with 2cpu, consumed time'
    t0 = time.time()
    res = p.map(product, ([1,n+1,2], [2,n+1,2]))
    res3 = res[0] * res[1]
    print time.time() - t0

    print 'method0 use math.factorial, for reference, consumed time'
    t0 = time.time()
    res4 = math.factorial(n)
    print time.time() - t0

    print res1==res2, res1==res3, res1==res4, 'if all True, the results are consistent, refer to the time above to compare algorithm'