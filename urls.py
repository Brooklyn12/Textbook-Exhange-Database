from django.urls import path,include
from . import views
urlpatterns = [
    path('users', views.AccountList.as_view()),
    path('users/<str:username>', views.AccountDetail.as_view()),
]