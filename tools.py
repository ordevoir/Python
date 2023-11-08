from copy import deepcopy

class Node():
    def __init__(self, value):
        self.value = value
        self.link = None

class LinkedList():
    def __init__(self, sequence=None):
        self.__headLink = None
        self.length = 0
        self.tail = None
        if sequence:
            for item in sequence:
                self.append(item)

    def append(self, value):
        """ добавить эелемент в конец списка """
        node = Node(value)
        if self.__headLink == None:   # если список пустой
            self.__headLink = node
        else:                       # иначе линкуем в конец
            self.tail.link = node
        self.tail = node
        self.length += 1

    def get(self, position):
        """ получить элемент """
        if position < self.length:
            currentNode = self.__headLink
            for i in range(position):
                currentNode = currentNode.link
            return currentNode.value
        else:
            raise IndexError('Index is out of range')
            # print('index out of range')

    def insert(self, position, value):
        """ вставить элемент """
        if position <= self.length:
            node = Node(value)
            currentNode = self.__headLink
            for i in range(position-1):
                currentNode = currentNode.link
            node.link = currentNode.link
            currentNode.link = node
            if position == self.length:
                self.tail = node
            self.length += 1
        else:
            print('index out of range')

    def pop(self, position=-1):
        """ удалить эелемент, находящися на заданной позиции; 
            если позиция не указана, то будет удален последний элемент """
        currentNode = self.__headLink
        if position == -1:
            if self.length == 1:
                value = self.__headLink.value
                self.__init__()
                return value
            while currentNode.link.link != None:
                currentNode = currentNode.link
            value = currentNode.link.value
            currentNode.link = None
            self.tail = currentNode
            self.length -= 1
            return value

        elif position == 0:
            value = self.__headLink.value
            self.__headLink = self.__headLink.link
            self.length -= 1
            return value

        elif position < self.length:
            for i in range(position-1):
                currentNode = currentNode.link
            value = currentNode.link.value
            currentNode.link = currentNode.link.link
            self.length -= 1
            return value
        else:
            print('index out of range')
            
    def change(self, position, value):
        """ изменить значение элемента в позиции position"""
        if position < self.length:
            currentNode = self.__headLink
            for i in range(position):
                currentNode = currentNode.link
            currentNode.value = value
        else:
            print('index out of range')

    def search(self, value):
        """ получить индекс первого элемента со значением value """
        currentNode = self.__headLink
        position = 0
        while currentNode != None:
            if currentNode.value == value:
                return position
            currentNode = currentNode.link
            position += 1
        print('there is no element with value', value)
        return None

    def clear(self):
        """ очистить список """
        self.__headLink = None
        self.length = 0
        self.tail = None

    def extend(self, otherList):
        """ присоединение другого списка """
        if isinstance(otherList, LinkedList):
            currentNode = self.__headLink
            while currentNode.link != None:
                currentNode = currentNode.link
            currentNode.link = otherList.__headLink
            self.tail = otherList.tail
            self.length += otherList.length
        elif isinstance(otherList, (list,  tuple)):
            for item in otherList:
                self.append(item)
    
    def __add__(self, otherList):
        """ определяем поведение оператора + для объектов данного класса """
        newList = deepcopy(self)
        newList.extend(otherList)
        return newList
        
    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.change(index, value)
        
    def __repr__(self):
        currentNode = self.__headLink
        text = '['
        while currentNode != None:
            if isinstance(currentNode.value, str):
                text += "'" + currentNode.value + "'"
            else:
                text += str(currentNode.value)
            currentNode = currentNode.link
            text += ', '
        text = text[:-2] + ']'
        if self.length == 0:
            text = '[]'
        return text