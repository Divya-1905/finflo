from .models import employee,nonworker,pagenotes
from rest_framework import serializers


class employeeserializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
class nonworkerseralizer(serializers.ModelSerializer):
    class Meta:
        model = nonworker
        fields = '__all__'       
class pageserializer(serializers.ModelSerializer):
    class Meta:
        model = pagenotes
        fields = ['note']