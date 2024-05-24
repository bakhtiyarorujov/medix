from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
    UserRegisterSerializer,
    LoginSerializer,
    UserUpdateSerializer
)
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        first_name = user.first_name
        phone = user.phone
        profile_photo = None
        gender = user.gender
        if user.profile_photo:  # Check if avatar exists
            profile_photo = request.build_absolute_uri(user.profile_photo.url) 

        return Response({
            'access_token': str(access_token),
            'refresh_token': str(refresh),
            'full_name': str(first_name),
            'gender': str(gender),
            'phone': str(phone),
            'profile_photo': profile_photo,
        })


class UserUpdateView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user