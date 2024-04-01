from django.urls import path
from .views import (
    TagListCreateView,
    TagRetrieveUpdateDeleteView
)

urlpatterns = [
    path('', TagListCreateView.as_view()),
    path('<int:pk>', TagRetrieveUpdateDeleteView.as_view(),name="update-tags"),
]