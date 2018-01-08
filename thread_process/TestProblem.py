#coding:utf-8


def putGift(gifts):
    while gifts:
        gifts.pop()
        print("目前gifts里剩有%s" % gifts)


if __name__ == "__main__":
    giftBox = ['手机', '火钳', '熊', '牙刷']
    putGift(giftBox)
    print("目前giftBox里剩有%s" % giftBox)
    print("over")


    # lst = ['thradsdf', 'dfidflsd', 'thedthreadad']
    # for xx in lst:
    #     if 'thread' in xx:
    #         print("yes")
    # print("end")