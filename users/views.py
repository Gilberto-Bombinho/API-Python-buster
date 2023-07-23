from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwner
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAccountOwner]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
