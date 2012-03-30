import time

def rt(func, *argc): # running time
    start = time.clock()
    func(*argc)
    end = time.clock()
    print '%s method takes %f seconds' %(func.__name__, end-start)
