from django.urls import path
from .views import (
    RecipeListApiView,
    RecipeRetrieveUpdateDestroyApiView
)

urlpatterns = [
    path('', RecipeListApiView.as_view()),
    path('<int:pk>', RecipeRetrieveUpdateDestroyApiView.as_view(),name="update"),
]