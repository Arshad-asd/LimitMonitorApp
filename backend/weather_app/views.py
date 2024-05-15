from rest_framework import generics
from .models import UserCriteria
from .serializers import UserCriteriaSerializer
from rest_framework.permissions import IsAuthenticated

class UserCriteriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserCriteria.objects.all()
    serializer_class = UserCriteriaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserCriteriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCriteria.objects.all()
    serializer_class = UserCriteriaSerializer
