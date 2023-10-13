import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import load_model

# загрузка данных
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# масштабирование значений пикселя в пределах от 0 до 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# изменяем форму изображений из 2D-массивов (28x28) в 1D-массивы (784 элемента).
x_train = x_train.reshape(x_train.shape[0], 784)
x_test = x_test.reshape(x_test.shape[0], 784)

#  Преобразуем метки в векторы с однократным кодированием (one-hot encoding)
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# cоздаем последовательную модель – это контейнер для линейного стека слоев (layers) нейронной сети,
# где данные последовательно проходят через каждый слой.
# можно добавлять различные типы слоев (например, полносвязные слои, сверточные слои, рекуррентные слои и другие)
# к этой модели и настраивать их параметры.
model = Sequential()
# с двумя полносвязными слоями (512 и 768 единиц измерения соответственно) используя функцию активации ReLU
model.add(Dense(512, input_shape=(784, ), activation='relu'))
model.add(Dense(768, activation='relu'))
# Выходной уровень содержит 10 единиц измерения (для 10 классов) и использует функцию активации softmax.
model.add(Dense(10, activation='softmax'))

# компилируем модель с помощью оптимизатора Adam и категориальной функции потери перекрестной энтропии.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# обучаем модель за 2 эпохи
model.fit(x_train, y_train, epochs=10)

# оцениваем точность модели на основе тестовых данных
evaluation = model.evaluate(x_test, y_test)
print(evaluation)
print(f'tochnost {evaluation[1]*100:.2f}%')

# сохраняем модель
model.save("my_model_50.h5")