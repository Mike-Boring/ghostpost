from django.shortcuts import render, HttpResponseRedirect, reverse, redirect

from homepage.models import Boasts

from homepage.forms import AddPostForm

from django.db.models import F, Sum


# Create your views here.


def index(request):
    all_posts = Boasts.objects.order_by("submission_time").reverse()
    # breakpoint()
    return render(request, "index.html", {"all_posts": all_posts})


def sorted(request):
    # used for reference https://stackoverflow.com/questions/47757857/ordering-a-django-queryset-by-sum-of-two-or-more-fields
    all_sorted = Boasts.objects.\
        annotate(total_count=Sum(
            F('up_votes') + F('down_votes'))
        ).\
        order_by('total_count').reverse()

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

# got a little help on upvote and downvote from studyhall, Sohail.


def upvote(request, upvote_id):
    current_post = Boasts.objects.get(id=upvote_id)
    current_post.up_votes = current_post.up_votes + 1
    current_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, downvote_id):
    current_post = Boasts.objects.get(id=downvote_id)
    current_post.down_votes = current_post.down_votes - 1
    current_post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
