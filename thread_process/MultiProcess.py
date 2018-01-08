#coding:utf-8

import multiprocessing


def func1(pipe):
    pipe.send("hello from func1")
    print('func1 received message:%s' %pipe.recv())

def func2(pipe):
    pipe.send("hello from func2")
    print('func2 received message:%s' %pipe.recv())

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=func1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=func2, args=(pipe[1],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
