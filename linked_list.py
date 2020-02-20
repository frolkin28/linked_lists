from abc import ABCMeta, abstractmethod

class List(metaclass=ABCMeta):
    @abstractmethod
    def insert_to_begin(self, node):
        pass

    @abstractmethod
    def insert_to_end(self, node):
        pass

    @abstractmethod
    def insert_to_middle(self, node, index):
        pass

    @abstractmethod
    def delete_from_begin(self, node):
        pass

    @abstractmethod
    def delete_from_middle(self, node):
        pass

    @abstractmethod
    def delete_from_end(self, node):
        pass

    @abstractmethod
    def sub_from_begin(self, node):
        pass

    @abstractmethod
    def sub_from_middle(self, node):
        pass

    @abstractmethod
    def sub_from_end(self, node):
        pass

    @abstractmethod
    def sum(self, node):
        pass

    @abstractmethod
    def find(self, node):
        pass
