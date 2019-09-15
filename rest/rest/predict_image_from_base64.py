from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import tf_hub_mobilenet_v2 as mn


class PredictImageFromBase64(APIView):

    def get(self, request):
        img_quoted = request.GET.get(key="img", default="")
        encode_dic = {'!': '/', '-': '+'}
        encode_table = str.maketrans(encode_dic)
        image_unquoted = img_quoted.translate(encode_table)
        out_dict = {}
        if(len(image_unquoted) <= 20000):
            out_dict['message'] = '224×224サイズ以上の画像データが対象です。'
            out_dict['result'] = '入力が正しくないため、分類処理ができませんでした。'
            out_dict['status'] = 'Param NG'
        else:
            cl = mn.MobileNetImageNet()
            out_dict['message'] = ''
            out_dict['result'] = cl.predict_from_base64(str(image_unquoted))
            out_dict['status'] = 'Param OK'
        return Response(out_dict, status=status.HTTP_200_OK)
