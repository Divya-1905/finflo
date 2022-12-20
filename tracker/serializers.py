from .models import employee
from rest_framework import serializers


class employeeserializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'