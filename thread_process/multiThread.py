#coding:utf-8


import threading
import multiprocessing

import time


def func(num, sec, lst):
    while lst:
    # print("第%d号线程开始执行：%s" % (num, time.ctime()))

        print("%d号线程从列表里取出了%s,列表里还有%s" % (num, lst.pop(), lst))
    # print("第%d号线程执行完毕：%s" % (num, time.ctime()))
        time.sleep(sec)



if __name__ == "__main__":

    giftsList = ['手机', '火钳', '熊', '牙刷', '刀', '铲铲', '烟枪', '一坨屎', '狗', '毛票']
    mgr = multiprocessing.Manager()
    lst = mgr.list()
    for g in giftsList:
        lst.append(g)

    print("多线程执行开始：%s" %time.ctime())
    #下边的daemon代表“可在后台执行的线程。若主线程结束了它也能在后台完成。所以主线程不会等它”
    #daemon默认为false，代表必须在前台执行完成的线程，程序必须要等我执行完了才能结束！
    #一般情况下都设为默认false，这样不用join也行，主线程执行完了也要等它执行完程序才能退出
    td1 = threading.Thread(target=func, args=(1, 1, lst), daemon=False)
    td2 = threading.Thread(target=func, args=(2, 1, lst), daemon=False)

    td1.start()
    td2.start()

    #加上这个是阻断主线程，要等到td1,td2执行完毕了才能继续往下执行主线程
    td1.join()
    td2.join()

    print("主线程执行完毕。%s" %time.ctime())
