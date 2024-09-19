
from django.urls import path,include

from . import views


urlpatterns = [
       path('',views.index,name='all_book'),
    path('edit/<int:pk>',views.update,name='edit'),
    path('create/',views.create_book,name='create'),
    path('delete/<int:id>',views.delete,name='delete'),
    

    
]