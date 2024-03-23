from abc import ABC, abstractmethod

class MyException(Exception):
    pass


class SquareGenerator(ABC):
    @abstractmethod
    def sq_squared(self, start, end):
        pass
