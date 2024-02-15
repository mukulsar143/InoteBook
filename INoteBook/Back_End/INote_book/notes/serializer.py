from rest_framework import serializers
from .models import *


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'username', 'title', 'descriptions']
        
        def validate(self, data):
            if Notes.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError("Not Athorized user")
            print(data)
            
            return data
    