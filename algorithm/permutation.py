import itertools
import benchmark

def perm1(lst):
    for p in itertools.permutations(lst):
        print p


if __name__ == '__main__':
    lst = [0,1,2]
    benchmark.rt(perm1 , lst)
