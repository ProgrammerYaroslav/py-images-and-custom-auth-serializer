from django.urls import path
from user.views import CreateTokenView

app_name = "user"

urlpatterns = [
    path("login/", CreateTokenView.as_view(), name="token"),
]
