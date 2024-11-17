import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import MeanAbsoluteError
from tensorflow.keras.optimizers import Adam

def Gen_data(num_samples):
    x=np.random.rand(num_samples,50,1)
    return x

x_train,y_train=Gen_data(100)
x_test,y_test=Gen_data(100)

epochs=10
batch_size=32
learning_rate=0.1

model=Sequential()
model.add(LSTM(64,input_shape=(seq_length,input_dim)))
model.compile(optimizer=Adam(learning_rate))