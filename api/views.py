from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Codes
from .serializer import CodesSerializer


# Create your views here.
class CodesView(viewsets.ModelViewSet):
    queryset = Codes.objects.all()
    serializer_class = CodesSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
