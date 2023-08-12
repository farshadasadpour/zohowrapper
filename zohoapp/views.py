from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serilizers
class ApiZoho(APIView):
    def post(self,request):
        serializer = serilizers.ZohoSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        return Response(data={"status":data},status=status.HTTP_200_OK)