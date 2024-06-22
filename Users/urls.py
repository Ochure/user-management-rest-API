from django.urls import path
from .views import create_user, retrieve_user, update_user, delete_user
#from django.urls import path, include

urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('retrieve/', retrieve_user, name='retrieve_user'),
    path('update/<int:pk>/', update_user, name='update_user_by_id'),
    path('update/', update_user, name='update_user_by_name'),
    path('delete/<int:pk>/', delete_user, name='delete_user_by_id'),
    path('delete/', delete_user, name='delete_user_by_name'),
]
