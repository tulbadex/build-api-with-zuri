from rest_framework import serializers
from .models import Student

class studentSerializers(serializers.ModelSerializer):

    name = serializers.CharField(max_length = 255)
    email = serializers.EmailField()
    reg_no = serializers.CharField()
    

    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        # return super().create(validated_data)
        return Student.objects.create(**validated_data)