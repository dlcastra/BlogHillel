from django.shortcuts import render, get_object_or_404
from bloghillel.models import Blog


def blog_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, "index.html", {"blog": blog})
