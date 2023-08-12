from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from . import serilizers
import requests


class ApiZoho(APIView):
    def post(self, request):
        serializer = serilizers.ZohoSerializer(data=request.data)
        if serializer.is_valid():
            r_data = serializer.validated_data
            # print(r_data["name"])
            # print(r_data["channel"])
            # print(r_data["key"])
            requrl = f"https://cliq.zoho.com/company/767068114/api/v2/bots/{r_data['channel']}/incoming?zapikey={r_data['key']}"

            g = requests.post(url=requrl ,data=json.dumps({"service": r_data["name"]}), headers={'Content-Type': 'application/json'})
            print(g)

            return Response(data={"status": r_data}, status=status.HTTP_200_OK)
