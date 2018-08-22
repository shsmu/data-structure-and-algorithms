class Stack:

    '''实现一个栈'''
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

if __name__ == '__main__':
    s = Stack()
    for i in range(1, 10):
        s.push(i)
    for i in range(1, 10):
        print(s.pop())
