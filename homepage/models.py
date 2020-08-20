from django.db import models
from django.utils import timezone

"""
Back end:

One model to represent both boasts and roasts
Boolean to tell whether it's a boast or a roast
CharField to put the content of the post in
IntegerField for up votes
IntegerField for down votes
DateTimeField for submission time
Front end: 

Homepage that displays boasts and roasts, sorted by time submitted (hint --> https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by (Links to an external site.)Links to an external site.)
Buttons to filter the content by either boasts or roasts, sorted by time submitted
Upvote and downvote buttons for each boast and roast
when clicked, these buttons affect the numbers on the relevant post appropriately
Ability to sort content based on vote score (hint: you may need to calculate the vote score) 
Page to submit a boast or a roast
"""

# Create your models here.


class Boasts(models.Model):
    boasts = models.BooleanField(default=True)
    post_text = models.CharField(max_length=240)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_text
