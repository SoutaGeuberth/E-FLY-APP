from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path('register/', views.register, name='register'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
    path("Edit/<int:DNI>", views.Edit, name='Edit'),
    path('logout/',views.exit,name='exit'),
    path("Delete/<int:DNI>", views.eliminateUser, name='Delete_user'),
]