import time

from django.core.cache import cache
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from bloghillel.forms import BlogForm
from bloghillel.models import Blog


@cache_page(60 * 15)
def blog_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    time.sleep(1)
    return render(request, "index.html", {"blog": blog})

def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "GET":
        form = BlogForm(instance=blog)
        return render(request, "edit_blog.html", {"blog": form})

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            cache.clear()
            return redirect(blog_view, id=id)

    return render(request, "edit_blog.html", {"blog": blog})
