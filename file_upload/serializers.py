from rest_framework import serializers
from .models import FileDetails


class GetSerializer(serializers.ModelSerializer):   
      class Meta:
        model = FileDetails
        fields = ['id','first_name','last_name','email','phone','gender']