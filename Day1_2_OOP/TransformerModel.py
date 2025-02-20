from AIModel import AIModel


class TransformerModel(AIModel):
    def __init__(self, model_name, version, num_layers):
        super().__init__(model_name, version)
        self.num_layers = num_layers

    def genAI(self, input_text):
        return f"Nothing to generate I'm a {self.model_name} and {self.version} {self.num_layers}"