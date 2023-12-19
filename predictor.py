import datetime
import numpy as np
import PIL.Image as Image
import matplotlib.pylab as plt
import tensorflow as tf
import tensorflow_hub as hub
import mediapipe as mp

mobilenet_v2 ="https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
classifier_model = mobilenet_v2
IMAGE_SHAPE = (224, 224)

classifier = tf.keras.Sequential([
            hub.KerasLayer(classifier_model, input_shape=IMAGE_SHAPE+(3,))
        ])

labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())

class AnimalDetector:
     def predict_animal(self, image):
         predict_image = Image.open(image).resize(IMAGE_SHAPE)
         predict_image = np.array(predict_image)/255.0
         result = classifier.predict(predict_image[np.newaxis, ...])
         predicted_class = tf.math.argmax(result[0], axis=-1)
         predicted_class_name = imagenet_labels[predicted_class]
         results = []
         detection_dict = {
                "etiqueta": predicted_class.numpy(),
                "name": predicted_class_name.title(),
                "date": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

            }
         results.append(detection_dict)
         return results