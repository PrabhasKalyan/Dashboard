from .models import *
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # exclude = ('intensity', 'relevance','likelihood')
        fields = "__all__"
        # def to_representation(self, instance):
        #     representation = super().to_representation(instance)
            
        #     # Handle empty strings in integer fields
        #     int_fields = ['intensity', 'relevance','likelihood']  # Replace with your actual integer field names
        #     for field in int_fields:
        #         if field in representation and representation[field] == '':
        #             representation[field] = None
            
        #     return representation
    

    
    


