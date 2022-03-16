from django.urls import path
from user.views import LoginAPIView, RegistrationAPIView, TokenRefreshAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
]


# urlpatterns = [
#     url(r'^users/?$', RegistrationAPIView.as_view()),
# +    url(r'^users/login/?$', LoginAPIView.as_view()),
# ]
