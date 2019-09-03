import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class Prefectures(APIView):

    def get(self, request):
        headers = {'X-API-KEY': 'nomgUp7A61gOWlvNTaGVjX1u7IvakZUf9MBcwOjK'}
        resp = requests.get(
            'https://opendata.resas-portal.go.jp/api/v1/prefectures',
            headers=headers)
        return Response(resp.json(), status=resp.status_code)
