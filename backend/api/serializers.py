from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# orm
#  serializer allow us to take json data and convert it to python object and vice versa

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


 