# Abstract Class
from abc import abstractmethod, ABC


class AIModelAbs(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, input_text):
        pass