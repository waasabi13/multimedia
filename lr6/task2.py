import tensorflow as tf
import keras
from keras.models import load_model
import cv2
import numpy as np



# загружаем модель
#model = load_model("my_model.h5")
model = load_model("cnn.h5")

# загрузили изображение в оттенках серого и изменили его размер на 28x28
image_path = "test/inv_9.jpg"
img_cv = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img_cv = cv2.resize(img_cv, (28, 28))

# нормализовали изображение
image = img_cv / 255.0

# развернули изображение в одномерный вектор
#image = image.reshape(1, 784)

# получаем предсказание модели
predictions = model.predict(image)

rounded_predictions = [round(num, 3) for num in predictions[0]]
# печать предсказанных вероятностей для каждого класса
print(rounded_predictions)

# получаем индекс класса с наибольшей вероятностью (предполагается, что классы от 0 до 9)
predicted_class = np.argmax(predictions)

# выводим предсказанный класс
print("Predicted class:", predicted_class)
