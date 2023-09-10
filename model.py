from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense

model = Sequential()
vocab_size = len(word_index) + 1
model.add(Embedding(vocab_size, embedding_dim, input_length=max_length))
model.add(LSTM(units=64))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=2, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()
