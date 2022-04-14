from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('blogs/', views.getBlogs, name="blogs"),
    path('blogs/create', views.createBlog, name="create-blog"),
    path('blogs/<str:pk>/update', views.updateBlog, name="update-blog"),
    path('blogs/<str:pk>/delete', views.deleteBlog, name="delete-blog"),
    path('blogs/<str:pk>', views.getBlog, name="blog"),
]

