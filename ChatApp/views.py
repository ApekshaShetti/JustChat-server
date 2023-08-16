from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializer import ServerSerailizer
from rest_framework.response import Response

class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self,request):
        category = request.query_params.get("category") # category data
        qty = request.query_params.get("qty")

        if category:
            self.queryset = self.queryset.filter(category__name = category)
        
        if qty:
            self.queryset = self.queryset[: int(qty)]
    
        serializer = ServerSerailizer(self.queryset, many=True)
        return Response(serializer.data)
            
