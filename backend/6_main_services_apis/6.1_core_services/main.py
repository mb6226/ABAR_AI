from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os

app = FastAPI()

# مدل و اسکیلر را فقط یکبار بارگذاری می‌کنیم
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../models/5_LSTM/5.2_training_evaluation/lstm_model.h5'))
model = load_model(MODEL_PATH, compile=False)

class PredictRequest(BaseModel):
    prices: list  # لیست آخرین قیمت‌ها (حداقل 10 مقدار)

@app.post("/predict")
def predict(req: PredictRequest):
    if len(req.prices) < 10:
        return {"error": "حداقل 10 مقدار قیمت لازم است."}
    scaler = MinMaxScaler()
    prices_np = np.array(req.prices).reshape(-1, 1)
    prices_scaled = scaler.fit_transform(prices_np)
    X = np.array([prices_scaled[-10:]])  # فقط 10 مقدار آخر
    pred_scaled = model.predict(X)
    pred = scaler.inverse_transform(pred_scaled)
    return {"predicted_price": float(pred.flatten()[0])}

# برای اجرا: uvicorn main:app --reload
