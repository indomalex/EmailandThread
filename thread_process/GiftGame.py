# coding:utf-8

# 三个人互相赠送礼物和取礼物。
# 大家左手从礼物架上取礼物到传送带上，同时另一边用右手取礼物，直到礼物被取完。
# 打印出三个人各自放了什么礼物，拿了什么礼物。

import multiprocessing
import time
import random

#注意gifts它是列表，传入后本身是会得到改变的
def putGift(queue, person, gifts):
    while gifts:
        g = gifts.pop()
        print("%s往传送带上放入了礼物%s, 目前礼物架里剩有%s" % (person, g, gifts))
        queue.put(g)
        time.sleep(random.randint(1, 3))



def getGift(queue, person):
    while not queue.empty():
        g = queue.get()
        print("%s拿走了礼物%s" % (person, g))
        time.sleep(random.randint(2, 4))


if __name__ == "__main__":
    #直接操作giftsList这个列表，会出现多进程争抢的情况。所以用到了Manager来作多进程的数据共享
    giftsList = ['手机', '火钳', '熊', '牙刷', '刀', '铲铲', '烟枪', '一坨屎', '狗', '毛票']

    persons = ['张三', '李四', '王麻子']
    queue = multiprocessing.Queue(20)

    mgr = multiprocessing.Manager()
    giftBox = mgr.list()
    for g in giftsList:
        giftBox.append(g)

    #ps即Process进程
    ps = []

    for person in persons:
        left = multiprocessing.Process(target=putGift, args=(queue, person, giftBox))
        ps.append(left)

    for person in persons:
        right = multiprocessing.Process(target=getGift, args=(queue, person))
        ps.append(right)

    for p in ps:
        p.start()

    for p in ps:
        p.join()
