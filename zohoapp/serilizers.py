from rest_framework import serializers


class ZohoSerializer(serializers.Serializer):
    name = serializers.CharField()
    channel = serializers.CharField()
    key = serializers.CharField()

