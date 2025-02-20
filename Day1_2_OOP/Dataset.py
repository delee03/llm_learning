class Dataset:
    def __init__(self):
        self.__data = [] #Private attribute trong Python (Enscapsulation)
    def add_data(self, text):
        if isinstance(text, str):
            self.__data = text
        else:
            print("Chỉ nhận dữ liệu dạng chuỗi")
    def show_data(self):
        return self.__data
