import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def get_address_from_zip(request):
    zipcode = request.GET.get(key="zipcode", default="1000011")
    resp = requests.get(
        'http://zipcloud.ibsnet.co.jp/api/search?zipcode=' +
        str(zipcode) +
        '&limit=1')
    return Response(resp.json(), status=resp.status_code)
