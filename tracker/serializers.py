from .models import employee,nonworker
from rest_framework import serializers


class employeeserializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
class nonworkerseralizer(serializers.ModelSerializer):
    class Meta:
        model = nonworker
        fields = '__all__'       
