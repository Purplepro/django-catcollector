from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    ]

# urlpatterns = [
#         path('/', views.index, name='about')

#     ]


