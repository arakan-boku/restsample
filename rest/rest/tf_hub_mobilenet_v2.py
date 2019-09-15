import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import PIL.Image as Image
import base64
from io import BytesIO
from . import to_japanese_ilsvrc2012 as toj


# ImageNetデータで学習済のMobilenet（画像分類モデル）
class MobileNetImageNet():
    # Mobilenetの学習済モデルをHubから取得し、kerasモデルに変換する
    def __init__(self):
        model_url = "https://tfhub.dev/google/tf2-preview/"
        model_name = "mobilenet_v2/classification/2"
        self.IMAGE_SHAPE = (224, 224)
        self.classifier = tf.keras.Sequential([hub.KerasLayer(
            model_url + model_name, input_shape=self.IMAGE_SHAPE + (3,))])
        data_url = "https://storage.googleapis.com/download.tensorflow.org/data/"
        labels_path = tf.keras.utils.get_file(
            'ImageNetLabels.txt', data_url + 'ImageNetLabels.txt')
        self.imagenet_labels = np.array(open(labels_path).read().splitlines())

    # 分類結果のクラス名を受取り文章に編集して返す内部関数
    def __make_result_str(self, predicted_class_name):
        translator = toj.Ilsvrc2012Japanese()
        result_dict = translator.translate(predicted_class_name)
        if (result_dict['status']):
            return "この画像は" + predicted_class_name + "：日本語名（" + result_dict['class_name'] + ")です"
        else:
            return result_dict['class_name']
        
    # 画像イメージを受け取り分類を行う内部処理
    def __predict(self, target_image):
        # 実数データに255.0で割る
        target_image_array = np.array(target_image) / 255.0
        # 分類を行い結果オブジェクトを返す
        result = self.classifier.predict(target_image_array[np.newaxis, ...])
        # 最も確率の高い分類クラスを示すインデックス（数値）を得る
        predicted_class = np.argmax(result[0], axis=-1)
        # インデックスを日本語名に変換する
        predicted_class_name = self.imagenet_labels[predicted_class]
        # 日本語名を結果文字列に変換する
        return self.__make_result_str(predicted_class_name)
    
    # 画像ファイルのパス＋ファイル名を引数にとって分類結果を返す
    def predict(self, image_file_path):
        target_image = Image.open(image_file_path).resize(self.IMAGE_SHAPE)
        return self.__predict(target_image)

    # Base64にエンコードされたテキストを受け取って分類結果を返す
    def predict_from_base64(self, encoded_base64_text):
        target_image = Image.open(BytesIO(base64.b64decode(encoded_base64_text))).resize(self.IMAGE_SHAPE)
        return self.__predict(target_image)
