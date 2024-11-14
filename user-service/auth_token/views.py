from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class GetTokenApiView(TokenObtainPairView):
    pass

class RefreshTokenApiView(TokenRefreshView):
    pass