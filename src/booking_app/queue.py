from .models import Queue


# class QueueTest():
#     FIFO = "FIFO"
#     LIFO = "LIFO"
#     STRATEGIES = [FIFO, LIFO]
#
# # создали новый объект очереди
#     def __init__(self, strategy):
#         if strategy not in self.STRATEGIES:
#             raise TypeError
#         self.strategy = strategy
#
# # при добавлении будем создали новый объект
#     def add(self, value):
#         if self.strategy == self.FIFO:
#             Queue.objects.create(value=value)
#
#     def pop(self):
#         if self.strategy == self.FIFO:
#             value = Queue.objects.order_by("id").first()
#             if value:
#                 value = value.value
#                 Queue.objects.order_by("id").first().delete()
#                 return value
#
#             return None


class UniqueQueue():
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise TypeError
        self.strategy = strategy
        self.storage = []
        self.elements_set = set()

    def add(self, value):
        if value not in self.elements_set:
            if self.strategy == self.FIFO:
                self.storage.insert(0, value)
            elif self.strategy == self.LIFO:
                self.storage.append(value)
            self.elements_set.add(value)

    #извлечение элемента из очереди
    def pop(self):
        if not self.storage:
            return None
        if self.strategy == self.FIFO:
            value = self.storage.pop()
        elif self.strategy == self.LIFO:
            value = self.storage.pop(0)
        self.elements_set.remove(value)
        return value

    def length(self):
        return len(self.storage)

    def last(self):
        if not self.storage:
            return None
        if self.strategy == self.FIFO:
            return self.storage[0]
        elif self.strategy == self.LIFO:
            return self.storage[-1]
