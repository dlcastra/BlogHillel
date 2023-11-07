from django.urls import path
from bloghillel import views


urlpatterns = [
    path("blog/<int:id>", views.blog_view, name="blog_view"),
]
