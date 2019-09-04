from td20 import tf_hub_mobilenet_v2 as mn
import base64


def base64encode(file_name):
    target_file = file_name
    with open(target_file, 'rb') as f:
        data = f.read()
    encoded_base64_text = base64.b64encode(data)
    return encoded_base64_text


cl = mn.MobileNetImageNet()
ans = cl.predict_from_base64(base64encode('test.jpg'))
print(ans)
# print(base64encode('test.jpg'))
