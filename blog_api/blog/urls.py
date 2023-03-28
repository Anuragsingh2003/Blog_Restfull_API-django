from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('create/', BlogCreate.as_view(), name='blog_create'),
    path('',views.index, name='index'),
    path('update/<int:id>/', BlogUpdate.as_view(), name='blog_update'),
    path('all/', BlogList.as_view(), name='blog_list'),
    path('delete/<int:id>/', BlogDelete.as_view(), name='blog_delete'),
]