from django.urls import path
from bloghillel import views


urlpatterns = [
    path("blog/<int:id>", views.blog_view, name="blog_view"),
    path("blog-edit/<int:id>", views.edit_blog, name="edit_blog"),
]
