from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from . import utilities
from . import serilizers
import requests


class ApiZoho(APIView):
    def post(self, request):
        # Validate data
        serializer = serilizers.ZohoSerializer(data=request.data)
        if serializer.is_valid():
            r_data = serializer.validated_data
            try:
                # Send request ro zoho
                requests.post(
                    url=utilities.generate_url(
                        r_data['channel'],
                        r_data['key']),
                    data=json.dumps({"service": r_data["name"]}),
                    headers={'Content-Type': 'application/json'})
            except Exception as error:
                print(error)
                return Response(
                    data={"status": "not ok"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(
                    data={"status": "ok"},
                    status=status.HTTP_200_OK
                )
