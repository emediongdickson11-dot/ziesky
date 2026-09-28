# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.feedback_list, name='feedback_list'),
#     path('create/', views.feedback_create, name='feedback_create'),
# ]from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_create, name='feedback_create'),
    path('feedback/', views.feedback_list, name='feedback_list'),
]