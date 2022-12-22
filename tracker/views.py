from django.shortcuts import render
from .models import employee,nonworker
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import employeeserializers,nonworkerseralizer
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import employee
class EmployeeCreate(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = employeeserializers
    def get(self,request):
        try:
            obj = employee.objects.all()
            serializer = employeeserializers(obj)
            return Response({'status':'correct','data':serializer.data})
        except:
            return Response({'staus':'cannot get'})
    def post(self,request):
        serializer = employeeserializers(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response({"status":'employee created','data':serializer.data})
        return Response({"status":"failure"})    
class NonWorkerCreate(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = nonworkerseralizer
    def get(self,request):
        try:
            data = nonworker.objects.all()
            serializer = nonworkerseralizer(data)
            return Response({'staus':'created','data':serializer.data})
        except:
            return Response({'status':'notcreate'})    
    def post(self,request):
        serializer = nonworkerseralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"staus":'nonworkercreated','data':serializer.data})
        return Response({'status':'failure'})    
        

    
    

