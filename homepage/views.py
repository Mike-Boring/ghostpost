from django.shortcuts import render

from homepage.models import Boasts

# Create your views here.


def index(request):
    all_posts = Boasts.objects.all()
    return render(request, "index.html", {"all_posts": all_posts})
