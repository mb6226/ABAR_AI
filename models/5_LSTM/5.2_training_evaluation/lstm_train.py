import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# بارگذاری داده
DATA_PATH = 'data/4_data_processing_modules/4.1_etl_processing/processed_tickdata.csv'
df = pd.read_csv(DATA_PATH)

# فقط ستون قیمت را استفاده می‌کنیم
prices = df['price'].values.reshape(-1, 1)
scaler = MinMaxScaler()
prices_scaled = scaler.fit_transform(prices)

# ساخت داده‌های ورودی/خروجی برای LSTM
def create_sequences(data, seq_length=10):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

X, y = create_sequences(prices_scaled, seq_length=10)

# ساخت مدل LSTM
model = Sequential([
    LSTM(32, input_shape=(X.shape[1], X.shape[2])),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# آموزش مدل
model.fit(X, y, epochs=10, batch_size=32)

# ذخیره مدل
model.save('lstm_model.h5')
