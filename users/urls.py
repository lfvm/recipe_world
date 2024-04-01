from django.urls import path
from .views import UserCreateView,UserRetrieveUpdateDelete

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('<int:id>/', UserRetrieveUpdateDelete.as_view()),
]
