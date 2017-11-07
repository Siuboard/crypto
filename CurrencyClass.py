from abc import ABCMeta, abstractmethod

class Currency(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def currency(self):
        pass

    @abstractmethod
    def history(self):
        pass
