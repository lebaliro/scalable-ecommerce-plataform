from django.contrib.auth.models import User
from django.http import Http404

from users.serializers import UserSerializer
from utils import response_patterns

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK


class UserCreateApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialiazer = UserSerializer(data=request.data)

        if serialiazer.is_valid():
            serialiazer.save()
            return Response(
                data=response_patterns.response_user_create_success,
                status=HTTP_201_CREATED
            )


class UserDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        response_patterns.response_user_detail['data'] = serializer.data
        response = response_patterns.response_user_detail
        
        return Response(
            data= response,
            status=HTTP_200_OK
        )
