from abc import ABC, abstractmethod

class OurContract(ABC):

    @abstractmethod
    def add(self,value):
        """This method accepts a value and adds it to the object by doing etc etc """
        pass

    @abstractmethod
    def contains(self, value):
        """Explain/describe functionality"""
        pass

    @abstractmethod
    def index_of(self, value):
        pass

    @abstractmethod
    def count(self) -> int:
        pass