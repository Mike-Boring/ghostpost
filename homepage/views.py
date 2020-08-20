from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Boasts

from homepage.forms import AddPostForm

# Create your views here.


def index(request):
    all_posts = Boasts.objects.order_by("submission_time").reverse()
    vote_count = 10
    return render(request, "index.html", {"all_posts": all_posts, "votes": vote_count})


def sorted(request):
    all_sorted = Boasts.objects.all()
    return render(request, "sorted.html", {"sorted": all_sorted})


def boasts(request):
    all_boasts = Boasts.objects.filter(
        boasts=True).order_by("submission_time").reverse()
    vote_count = 10
    return render(request, "boasts.html", {"boasts": all_boasts, "votes": vote_count})


def roasts(request):
    all_roasts = Boasts.objects.filter(
        boasts=False).order_by("submission_time").reverse()
    vote_count = 10
    return render(request, "roasts.html", {"roasts": all_roasts, "votes": vote_count})


def addpost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('boasts') == 'boast':
                new_post = Boasts.objects.create(
                    boasts=True,
                    post_text=data.get('post_text'),
                )
            else:
                new_post = Boasts.objects.create(
                    boasts=False,
                    post_text=data.get('post_text'),
                )
            # breakpoint()
            return HttpResponseRedirect(reverse("homepage"))

    form = AddPostForm()
    all_posts = Boasts.objects.all()
    return render(request, "addpost.html", {"form": form, "all_posts": all_posts})
