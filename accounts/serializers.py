from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class userSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, max_length = 50, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    
    def create(self, validated_data):
        # return super().create(validated_data)
        return User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')