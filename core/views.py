from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .serializers import RegisterSerializer, UserSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': serializer.data,
        })


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def user(request: Request):
    return Response({
        'data': UserSerializer(request.user).data,
    })
