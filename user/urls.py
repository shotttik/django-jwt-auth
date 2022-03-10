from django.urls import path
from user.views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]


# urlpatterns = [
#     url(r'^users/?$', RegistrationAPIView.as_view()),
# +    url(r'^users/login/?$', LoginAPIView.as_view()),
# ]
