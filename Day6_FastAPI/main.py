import torch
from IPython.terminal.shortcuts.filters import PassThrough
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import io
import accelerate

from ml_model import predict_price
from transformers import pipeline
app = FastAPI()

# API nhận file CSV và trả về dữ liệu đã chuẩn hóa
@app.post("/upload-csv", summary="Upload a CSV file and normalize data")
def upload_csv(file: UploadFile):
    """
        Uploads a CSV file and normalizes data using MinMaxScaler.
    """
    return {
        "filename": file.filename
    }
    # # Đọc file CSV từ request
    # content = await file.read()
    # df = pd.read_csv(io.StringIO(content.decode("utf-8")))
    #
    # # Chuẩn hóa dữ liệu (Min-Max Scaling)
    # scaler = MinMaxScaler()
    # df_scaled = pd.DataFrame(scaler.fit_transform(df.iloc[:, 1:]), columns=df.columns[1:])
    #
    # return {"message": "Dữ liệu đã chuẩn hóa", "data": df_scaled.to_dict(orient="records")}

@app.post("/echo/")
def echo_message(message: str):
    return {"message_received": message}

@app.get("/predict")
async def predict(area: float):
    price = await predict_price(area)
    return {
        "statusCode": 200,
        "message" : "Return value successfully",
        "Diện tích":area,
        "Giá dự đoán": price
    }


#Load model GPT-2 from HuggingFace by transformer lib
pipe = pipeline("text-generation", model="openai-community/gpt2")
@app.get("/generate/")
def generation(prompt: str):
    output = pipe(prompt, max_length=100, num_return_sequences=1)
    return {
        "Prompt": prompt,
        "Generated_text": output[0]["generated_text"]
    }



