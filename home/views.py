from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class HandleFileUplaod(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer  = FileListSerializers(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'message':"File Upload Successfully"})
            return ResourceWarning({'status':400,'message':"Something went wrong",data:serializer.errors})
        except Exception as e:
            print(e)


