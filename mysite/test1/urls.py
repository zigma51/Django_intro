from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.create_view, name='create_view'),
    path('', views.list_view, name='list_view'),
    path('create', views.create_view, name='create_view'),
    path('<id>', views.detail_view, name='detail_view'),
    path('<id>/update', views.update_view, name='update_view'),
    path('<id>/delete', views.delete_view, name='delete_view'),
]