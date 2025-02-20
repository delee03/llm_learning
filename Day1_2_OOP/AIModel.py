from abc import abstractmethod
class AIModel:
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version
    @abstractmethod
    def train(self, data):
        pass
    @abstractmethod
    def predict(self, input_text):
        pass
    def genAI(self, input_text):
        return f"{5 + 3} {self.model_name} ({self.version}) generate: AI sẽ thay đổi thé giới {input_text}"