class Queue(object):
    '''实现一个队列'''
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        return self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

if __name__ == '__main__':
    q = Queue()
    for i in range(0, 3):
        q.enqueue(i)
    for i in range(0, 3):
        q.dequeue(i)