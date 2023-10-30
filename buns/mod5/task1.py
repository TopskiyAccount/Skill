class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data 
        self.next = None  

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.top = None  

    def pop(self):
        """
        Возвращение верхнего элемента из стека с удалением его из стека
        """
        if self.is_empty():
            return None  
        else:
            val = self.top.data  
            self.top = self.top.next
            return val

    def push(self, val):
        """
        Добавление элемента val в верхнюю часть стека
        """
        new_node = Node(val)
        new_node.next = self.top  
        self.top = new_node

    def is_empty(self):
        """
        Проверяет, пуст ли стек
        """
        return self.top is None

    def print(self):
        """
        Вывод на печать содержимого стека
        """
        current = self.top
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
