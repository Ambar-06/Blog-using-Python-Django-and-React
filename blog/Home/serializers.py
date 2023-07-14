from rest_framework import serializers

class SignUpSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.EmailField(required=True)