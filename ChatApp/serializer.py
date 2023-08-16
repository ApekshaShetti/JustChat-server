from rest_framework import serializers
from .models import Server, Category

class ServerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"

    