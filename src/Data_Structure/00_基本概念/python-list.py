'''
实现 Python 里的 list
本例中通过链表实现
方法： is_empty len index append insert pop count next
参考： https://blog.csdn.net/u012485099/article/details/79440924
'''

class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next = None

class myList(object):

    def __init__(self, node=None):
        self._head = node

    '''判断列表是否为空'''
    def is_empty(self):
        return self._head == None

    '''计算列表的长度'''
    def len(self):
        # cur 游标, 用来移动遍历节点
        cur = self._head
        # count 记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    '''列表尾部添加元素'''
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    '''列表尾部删除元素'''
    def pop(self):
        cur = self._head
        pre = None
        if cur == None:
            raise IndexError('pop from empty list')
        else:
            while cur.next != None:
                pre = cur
                cur = cur.next
            pre.next = None
            return cur.elem

if __name__ == '__main__':
    li = myList()
    for i in range(1, 10):
        li.append(i)
    for i in range(0, 3):
        print(li.pop())

