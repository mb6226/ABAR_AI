import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

import os
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../data/4_data_processing_modules/4.1_etl_processing/processed_tickdata.csv'))
df = pd.read_csv(DATA_PATH)
prices = df['price'].values.reshape(-1, 1)
scaler = MinMaxScaler()
prices_scaled = scaler.fit_transform(prices)

# ساخت داده‌های تست
seq_length = 10
X_test = []
for i in range(len(prices_scaled) - seq_length):
    X_test.append(prices_scaled[i:i+seq_length])
X_test = np.array(X_test)

model_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../5.2_training_evaluation/lstm_model.h5'))
model = load_model(model_path, compile=False)
preds = model.predict(X_test)
preds_rescaled = scaler.inverse_transform(preds)

# ذخیره نتایج در کنار اسکریپت
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lstm_predictions.csv')
pd.DataFrame({'predicted_price': preds_rescaled.flatten()}).to_csv(output_path, index=False)
