import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class Municipalities(APIView):

    def get(self, request):
        pref_code = request.GET.get(key="prefcode", default="13")
        headers = {'X-API-KEY': 'nomgUp7A61gOWlvNTaGVjX1u7IvakZUf9MBcwOjK'}
        params = {'prefCode': pref_code}
        resp = requests.get(
            'https://opendata.resas-portal.go.jp/api/v1/cities',
            headers=headers,
            params=params)
        return Response(resp.json(), status=resp.status_code)
