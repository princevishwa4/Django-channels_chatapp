from django.urls import path
from account.views import (
    login_view,
    register_view,
    logout_view,
    update_view,
)


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('update/<int:id>', update_view, name="update"),
]