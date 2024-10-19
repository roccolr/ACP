import multiprocess
from numpy import pi
from time import sleep

def f(n, a):
    n.value = pi
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    n = multiprocess.Value('d', 0.0)
    a = multiprocess.Array('i', range(10))

    p = multiprocess.Process(target= f, args=(n,a))
    p.start()
    
    sleep(1)

    # a.sort()
    print(n.value,a[:])

    p.join()
