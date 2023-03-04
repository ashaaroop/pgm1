
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.detailview.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cbvdelete'),
]