import time

def rt(func, n):
    start = time.clock()
    func(n)
    end = time.clock()
    print '%s method need last %f seconds' %(func.__name__, end-start)
