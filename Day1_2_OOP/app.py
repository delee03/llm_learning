
from AIModel import AIModel
from TransformerModel import TransformerModel
from Dataset import Dataset

# conAI = AIModel("GPT_4", "4.0")
#
# #In kết quả method generate
# # print(conAI.genAI("Hãy nháy theo câu này"))
#
# conAIThuHai = TransformerModel("DeepSeek", "R1", "671B")
# print(conAIThuHai.genAI("Inheritance in Python"))
#
# dataset1 = Dataset()
# # dataset1.add_data(123)
# dataset1.add_data("Don't you know I always try harder every single day")
# data = dataset1.show_data()
# print(data)
from AIModelAbs import AIModelAbs
#Abstraction in Python with decorater @abstractmethod
print("Abstraction in Python with decorater @abstractmethod############")

class GPTModel(AIModelAbs):
    # def __init__(self, model_name, version):
    #     super().__init__(model_name, version) # trừ khi mình đang muốn override lại các attribute của AIModel còn không thì không cần dùng super() này
    def train(self, data):
        print(f"Hiện tại GPT Model đang được Fuderr huấn luyện với {data}...")

    def predict(self, input_text):
        return f"GPT dự đoán: {input_text} là một câu hỏi"
#Sử dụng abstract gọi các class con
gpt1 = GPTModel()
gpt1.train("Dữ liệu huấn luyện GPT")
# question1 = gpt1.predict("Tôi yêu lập trình")
# print(question1)