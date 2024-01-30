from rest_framework import generics, permissions

from .models import Custumer
from .serializers import CustumerSerializer


class CustumerListAPIView(generics.ListAPIView):
    serializer_class = CustumerSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Custumer.objects.all()