from operator import le
from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):  # retorna uma fila vazia
        self.data = []

    def __len__(self):  # retorna o tamanho da fila
        return len(self.data)

    def enqueue(self, value):  # add novo coisa no final da fila
        self.data.append(value)

    def dequeue(self):
        # lista vazia?
        if len(self) == 0:
            raise IndexError("dequeue from empty queue")
        return self.data.pop(0)  # remove e retona o primeiro coiso da fila

    def search(self, index):
        if index < 0 or index >= len(self.data):  # limite valido
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
