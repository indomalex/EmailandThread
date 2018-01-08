# coding:utf-8

def sortUsingLambda(lst: list):
    lst.sort(key=lambda ct: ct[0], reverse=True)
    return lst


if __name__ == "__main__":
    list = ['c.txt', 't.txt', 'r.txt', 'a.txt', 'bb.txt', 'w.txt', 'h.txt']
    newList = sortUsingLambda(list)
    print(newList)
    print(newList[-1])