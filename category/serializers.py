from  rest_framework import serializers
from .models import *




class FileSerializer(serializers.ModelSerializer):
     class Meta:
          model = File
          fields = ['id', 'file_name', 'file_type', 'size', 'created_at']


