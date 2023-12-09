class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  
        self.nref = None  
        self.pref = None  

class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  
        self.end = None  

    def pop(self):
        """
        Возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None  
        val = self.start.data
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n
        """
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            count = 0
            while current:
                if count == n - 1:
                    new_node.pref = current
                    new_node.nref = current.nref
                    if current.nref:
                        current.nref.pref = new_node
                    current.nref = new_node
                    if current == self.end:
                        self.end = new_node
                    break
                current = current.nref
                count += 1

    def print(self):
        """
        Вывод на печать содержимого очереди
        """
        current = self.start
        while current:
            print(current.data, end=' -> ')
            current = current.nref
        print("None")
