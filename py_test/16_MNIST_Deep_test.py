import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('./model/16-0.0250.hdf5')

import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('img2/2.PNG').convert("L")
plt.imshow(img)
plt.show()
width, height = img.size
print(width, height)
img_resize = img.resize((28, 28))

test = np.array(img_resize).reshape(1, 28, 28, 1).astype('float32') / 255
predictData = model.predict(test)
print(np.argsort(np.max(predictData, axis = 0))[-1])
# print(np.argsort(np.max(predictData, axis = 0))[-2])