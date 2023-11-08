import time

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from bloghillel.models import Blog


@cache_page(60 * 15)
def blog_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    time.sleep(2)
    return render(request, "index.html", {"blog": blog})
