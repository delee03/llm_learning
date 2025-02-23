import torch
from IPython.terminal.shortcuts.filters import PassThrough
from fastapi import FastAPI
from pydantic import BaseModel
import accelerate
print(accelerate.__version__)
from ml_model import predict_price

app = FastAPI()

@app.post("/echo/")
def echo_message(message: str):
    return {"message_received": message}

@app.get("/predict")
def predict(area: float):
    price = predict_price(area)
    return {
        "statusCode": 200,
        "message" : "Return value successfully",
        "Diện tích":area,
        "Giá dự đoán": price
    }
from transformers import pipeline

#Load model GPT-2 from HuggingFace by transformer lib
pipe = pipeline("text-generation", model="openai-community/gpt2")
@app.get("/generate/")
def generation(prompt: str):
    output = pipe(prompt, max_length=100, num_return_sequences=1)
    return {
        "Prompt": prompt,
        "Generated_text": output[0]["generated_text"]
    }

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)

# Load model with device_map="auto" for optimized acceleration
# Load model on CPU and disable FP8 quantization
model = AutoModelForCausalLM.from_pretrained(
    model_name, token=True, device_map="auto"
)

# Define request model
class PromptRequest(BaseModel):
    prompt: str


@app.get("/generate-llama")
def generatedeepseek(prompt: str):
    #Format the message in chat format
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    # Tokenize messages
    input_text = tokenizer.apply_chat_template(messages, return_tensors="pt")
    with torch.no_grad():
         output = model.generate(input_text, max_length=100)

    # Decode and print response
    generated_text = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    return {
        "response": {
            "Prompt": prompt,
            "GenerateText": generated_text
        }
    }



