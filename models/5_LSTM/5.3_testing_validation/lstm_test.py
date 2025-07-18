import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

DATA_PATH = '../../data/4_data_processing_modules/4.1_etl_processing/processed_tickdata.csv'
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

model = load_model('lstm_model.h5')
preds = model.predict(X_test)
preds_rescaled = scaler.inverse_transform(preds)

# ذخیره نتایج
pd.DataFrame({'predicted_price': preds_rescaled.flatten()}).to_csv('lstm_predictions.csv', index=False)
