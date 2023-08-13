from rest_framework import serializers


class ZohoSerializer(serializers.Serializer):
    name = serializers.ListField(required=True, allow_null=False)
    channel = serializers.CharField(required=True, allow_null=False)
    key = serializers.CharField(required=True, allow_null=False)

    # def validate(self, attrs):
    #     validated_data = super().validate(attrs=attrs)
    #     if type(validated_data['name']) != list:
    #         raise serializers.ValidationError({'name': 'name should be list'})
    #     return validated_data
