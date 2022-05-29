from validator import *


class LinkedList:

    """
    Мой собственный связанный список.

    Параметр "length" увеличивается на единицу при инициализации
    объекта класса Node и показывает количество элементов в списке.
    """

    __head = None
    _length = 0
    name = None
    ERR_MESSAGES = {
        1: '~~~~~~~~~~~~~~~~~~~~\n    СПИСОК ПУСТ\n~~~~~~~~~~~~~~~~~~~~'
    }

    def __str__(self):
        return f'<LINKED_LIST:{self.name}>'

    class Node:

        """
        Класс "узла". Создает и хранит в своем экземпляре
        значение и ссылку на следующий элемент связанного списка

        """

        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node
            LinkedList._length += 1

    def add_at_end(self, element):
        """ Добавляет элемент в конец списка """
        if not self.__head:
            self.__head = self.Node(element)
            return element

        node = self.__head
        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(element)
        return element

    def show_list(self):
        """ Отображение списка в консоль """
        if not self.__head:
            print(self.ERR_MESSAGES[1])
            return None
        node = self.__head
        i = 0
        print(f'___________________________ \n__{self}__')
        while node.next_node:
            print(f'{i} : {node.element}___{type(node.element)},'
                  f'  ---> Следующий элемент: {node.next_node.element}___{type(node.next_node.element)}')
            i += 1
            node = node.next_node
        print(f'{i} : {node.element}___{type(node.element)}')
        print('Конец списка \n___________________________')

    def add_at_start(self, element):
        """ Добавляет элемент в начало списка """
        old_list = self.__head
        self.__head = self.Node(element)
        self.__head.next_node = old_list
        return element

    def insert_by_index(self, element, index):
        """ Добавляет элемент в список по указанному порядковому номеру index """
        index_valid = verification(length=self._length, index=index)
        if index_valid == 0:
            return self.add_at_start(element)
        i = 0
        node = self.__head
        prev_list = self.__head
        while i < index_valid:
            prev_list = node
            node = node.next_node
            i += 1
        prev_list.next_node = self.Node(element, next_node=node)
        return element

    def delete_by_index(self, index):
        """ Удаляет элемент из списка по указанному порядковому номеру index """

        '''
        Пропускается ссылка на объект с указанным индексом, НО он вполне вероятно
        остается в оперативной памяти
        '''

        index_valid = verification(length=self._length, index=index)
        i = 0
        node = self.__head
        prev_list = self.__head
        while i < index_valid:
            prev_list = node
            node = node.next_node
            i += 1
        next = node.next_node
        prev_list.next_node = next
        self._length = self._length - 1
        return index

    def count_all_elements(self):
        """ возвращает количество элементов в списке """
        node = self.__head
        count = 0
        while node:
            node = node.next_node
            count += 1
        print(f'Результат работы метода "count_all_elements": {count} элементов')
        return count

    def get_python_list(self):
        """ Сохраняет все элементы связанного списка в списке python """
        node = self.__head
        list = []
        while node:
            list.append(node.element)
            node = node.next_node
        return list

    def _delete_linked_list(self):
        """ Удаляет связанный список """
        """ Отображения нет, значения извлечь не получится, НО список вполне вероятно в памяти есть"""
        self.__head = None
        self._length = 0

    def get_content_by_index(self, index):
        """ Возвращает значение элемента по порядковому номеру index """
        index_valid = verification(length=self._length, index=index)
        node = self.__head
        i = 0
        while i < index_valid:
            node = node.next_node
            i += 1
        content = node.element
        return content


