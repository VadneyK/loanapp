from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers # new
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Application
from .permissions import IsOwnerOrReadOnly
from .serializers import ApplicationSerializer, UserSerializer


@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'applications': reverse('application-list', request=request, format=format)
    })

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,) # new

class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,) # new

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer