from rest_framework import serializers
from .models import UserCriteria

class UserCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCriteria
        fields = '__all__'
